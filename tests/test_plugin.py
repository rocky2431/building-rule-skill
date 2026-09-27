"""Exercise hook boundaries and package paths consumed by native hosts."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "building-rules"


class PluginChecks(unittest.TestCase):
    def run_hook(self, host, event, plugin=PLUGIN):
        return subprocess.run(
            [sys.executable, str(plugin / "hooks/activate.py"), "--host", host],
            input=event if isinstance(event, str) else json.dumps(event),
            text=True, capture_output=True, cwd=ROOT, timeout=5,
        )

    def test_supported_context_and_relocation(self):
        with tempfile.TemporaryDirectory() as directory:
            relocated = Path(directory) / "plugin with spaces"
            shutil.copytree(PLUGIN, relocated)
            cases = [("codex", "SessionStart"), ("claude", "SubagentStart"),
                     ("zcode", "SessionStart"), ("kimi", "UserPromptSubmit")]
            for host, name in cases:
                with self.subTest(host=host):
                    result = self.run_hook(host, {"hook_event_name": name, "source": "resume"}, relocated)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    context = result.stdout
                    if host != "kimi":
                        output = json.loads(context)["hookSpecificOutput"]
                        self.assertEqual(output["hookEventName"], name)
                        context = output["additionalContext"]
                    core = (relocated / "skills/building-rules/references/core.md").read_text()
                    self.assertIn(core, context)
                    self.assertIn(str(relocated / "skills/building-rules/SKILL.md"), context)

    def test_unsupported_and_malformed_events_do_not_inject(self):
        events = ["not json", [], {"hook_event_name": []}, {"hook_event_name": "Stop"},
                  {"hook_event_name": "SessionStart", "source": "unknown"},
                  {"hook_event_name": "SessionStart", "source": []}]
        for event in events:
            with self.subTest(event=event):
                result = self.run_hook("codex", event)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, "")
        for host, name in [("kimi", "SessionStart"), ("zcode", "SubagentStart")]:
            result = self.run_hook(host, {"hook_event_name": name, "source": "startup"})
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")

    def test_missing_core_is_visible_and_nonblocking(self):
        with tempfile.TemporaryDirectory() as directory:
            relocated = Path(directory) / "plugin"
            shutil.copytree(PLUGIN, relocated)
            (relocated / "skills/building-rules/references/core.md").unlink()
            result = self.run_hook("claude", {"hook_event_name": "SessionStart", "source": "startup"}, relocated)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")
            self.assertIn("could not be loaded", result.stderr)

    def test_native_command_routes_each_host(self):
        hooks = json.loads((PLUGIN / "hooks/hooks.json").read_text())["hooks"]
        command = hooks["SessionStart"][0]["hooks"][0]["command"]
        for variable in ["PLUGIN_ROOT", "CLAUDE_PLUGIN_ROOT", "ZCODE_PLUGIN_ROOT"]:
            env = {k: v for k, v in os.environ.items()
                   if k not in {"PLUGIN_ROOT", "CLAUDE_PLUGIN_ROOT", "ZCODE_PLUGIN_ROOT"}}
            env[variable] = str(PLUGIN)
            result = subprocess.run(
                ["/bin/sh", "-c", command], env=env, text=True,
                input=json.dumps({"hook_event_name": "SessionStart", "source": "compact"}),
                capture_output=True, timeout=5,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["hookSpecificOutput"]["hookEventName"], "SessionStart")

    def test_native_package_paths(self):
        for name in [".codex-plugin/plugin.json", ".claude-plugin/plugin.json",
                     ".zcode-plugin/plugin.json", "kimi.plugin.json"]:
            manifest = json.loads((PLUGIN / name).read_text())
            self.assertEqual(manifest["name"], PLUGIN.name)
            self.assertEqual(manifest["version"], "0.1.0")
        codex = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
        claude = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(codex["name"], claude["name"])
        for source in [codex["plugins"][0]["source"]["path"], claude["plugins"][0]["source"]]:
            self.assertEqual((ROOT / source).resolve(), PLUGIN)
        self.assertTrue((PLUGIN / "skills/building-rules/SKILL.md").is_file())
        kimi = json.loads((PLUGIN / "kimi.plugin.json").read_text())
        for folder in kimi["skills"]:
            self.assertTrue((PLUGIN / folder / "building-rules/SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
