"""Ship the reviewed 25 November 2026 front page to the harness.

``entry.png`` next to this file is the finished, reviewed picture.  This
entry point does nothing creative: it places an exact copy of that file
in the directory the harness reads (``MAKEFUN_OUTPUT_DIR``, falling back
to ``/output``).  No network, no clock, no randomness, so every run
publishes the same bytes.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


def fingerprint(path: Path) -> str:
    """SHA-256 of a file, streamed in 64 KiB blocks."""
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        while True:
            block = stream.read(65536)
            if not block:
                break
            hasher.update(block)
    return hasher.hexdigest()


def publish() -> int:
    base = Path(__file__).resolve().parent
    picture = base / "entry.png"
    if not picture.is_file():
        print("missing entry image: %s" % picture, file=sys.stderr)
        return 1

    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / "entry.png"
    shutil.copyfile(picture, target)

    if target.stat().st_size != picture.stat().st_size:
        print("size mismatch after copy", file=sys.stderr)
        return 1
    if fingerprint(target) != fingerprint(picture):
        print("content mismatch after copy", file=sys.stderr)
        return 1
    print("published %s (%d bytes, sha256 %s)"
          % (target, target.stat().st_size, fingerprint(target)))
    return 0


if __name__ == "__main__":
    raise SystemExit(publish())
