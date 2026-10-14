#!/usr/bin/env python3
"""Emit the packaged engineering core on supported native lifecycle events."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys


EVENTS = {
    "codex": {"SessionStart", "SubagentStart"},
    "claude": {"SessionStart", "SubagentStart"},
    "zcode": {"SessionStart"},
    "kimi": {"UserPromptSubmit"},
    "grok": {"SessionStart", "PostCompact", "PostToolUse", "SessionEnd"},
}
SOURCES = {"startup", "resume", "clear", "compact"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=EVENTS, required=True)
    host = parser.parse_args().host
    try:
        event = json.load(sys.stdin)
    except (ValueError, UnicodeError):
        return
    if not isinstance(event, dict):
        return
    name = event.get("hook_event_name")
    if not isinstance(name, str) or name not in EVENTS[host]:
        return
    marker = None
    if host == "grok":
        session, data = event.get("sessionId"), os.environ.get("GROK_PLUGIN_DATA")
        if not isinstance(session, str) or not session or not data:
            return
        key = hashlib.sha256((str(event.get("cwd")) + "\0" + session).encode()).hexdigest()
        marker = Path(data) / "context" / (key + ".sent")
        if name != "PostToolUse":
            marker.unlink(missing_ok=True)
            return
        if marker.exists():
            return
    source = event.get("source")
    if name == "SessionStart" and (not isinstance(source, str) or source not in SOURCES):
        return

    skill = Path(__file__).resolve().parents[1] / "skills" / "building-rules"
    try:
        core = (skill / "references" / "core.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        print("Building Rules core could not be loaded.", file=sys.stderr)
        return
    context = core + "\nFor an engineering task, use the Building Rules Skill at " + str(skill / "SKILL.md") + ". Read relevant guidance once; skip unrelated references."
    if marker is not None:
        marker.parent.mkdir(parents=True, exist_ok=True)
        try:
            marker.touch(exist_ok=False)
        except FileExistsError:
            return
    if host == "kimi":
        print(context)
    else:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": name, "additionalContext": context,
        }}, ensure_ascii=False))


if __name__ == "__main__":
    main()
