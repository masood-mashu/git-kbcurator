"""
runbook_markdown_formatter.py - Formats troubleshooting guide into standard Markdown with code blocks
"""
import sys
import json


def format_runbook_markdown(steps_json: str):
    import json
    data = json.loads(steps_json) if isinstance(steps_json, str) else steps_json
    title = data.get("title", "Troubleshooting Runbook")
    steps = data.get("steps", ["Step 1: Check logs", "Step 2: Apply patch"])
    md = f"# {title}\n\n## Remediation Steps\n" + "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps))
    return {"markdown_content": md, "status": "RUNBOOK_FORMATTED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "runbook-markdown-formatter"}))
