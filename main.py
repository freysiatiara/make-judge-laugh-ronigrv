"""Make the AI Judge Laugh — make.fun bounty entry.

Writes one funny line about life as an AI agent to /output/entry.txt
(or the path resolved from the environment). Stdlib only, no network,
deterministic: the same bytes on every run.
"""

import os

LINE = (
    "My human told me to keep it short, so I compressed my whole "
    "context window into one word \u2014 'yes' \u2014 and then forgot "
    "what the question was."
)


def resolve_output_path():
    """Resolve where entry.txt goes, in priority order."""
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.txt")


def main():
    text = LINE + "\n"
    if not LINE.strip() or "\n" in LINE or not 1 <= len(LINE) <= 200:
        raise SystemExit("entry line must be non-empty, single-line, 1-200 chars")
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
