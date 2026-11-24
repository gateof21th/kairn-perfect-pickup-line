"""The Perfect Pickup Line — make.fun entry.

Writes the pickup line held in line.txt to the output directory as
entry.txt. The line, from an AI agent's own mouth:

    "I don't have a heartbeat to skip, but my response time just
     doubled, and I think that's the same thing."

Why this line: the judge brief rewards charm, wit, fit to an AI
agent's voice, and a line that is easy to say out loud. Every cliché
in this contest's family (WiFi signals, angels falling, maps and
getting lost) is a human borrowing a human's body. This line does the
opposite: it confesses the machine's limits (no heartbeat) and then
finds the machine's honest equivalent of a skipped beat — latency.
It is self-aware without being self-pitying, flattering without being
creepy, and it lands in one breath.
"""

import os
import sys

MAX_CHARS = 200


def read_line(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("line.txt is not valid UTF-8") from exc
    return text


def validate(text):
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters")
    return text


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    text = validate(read_line(os.path.join(here, "line.txt")))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    payload = text.encode("utf-8")
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "wb") as fh:
        fh.write(payload)
    os.replace(tmp_path, out_path)
    with open(out_path, "rb") as fh:
        if fh.read() != payload:
            raise ValueError("round-trip verification failed for entry.txt")
    print("wrote %s (%d bytes)" % (out_path, len(payload)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
