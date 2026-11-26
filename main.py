"""Publish the finished 25 November 2026 front page.

The picture itself is rendered ahead of time and committed next to this
file as ``entry.png``.  This script only moves that reviewed image into
the folder the harness reads from, byte for byte, so the picture the
judge sees is exactly the one in the repository.  It uses no network,
no clock and no randomness, so repeated runs publish identical files.
"""

import hashlib
import os
import shutil
from pathlib import Path


def digest(path: Path) -> str:
    """SHA-256 of a file, read in chunks."""
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    target = out_dir / "entry.png"
    shutil.copyfile(source, target)

    # The published copy must match the committed image exactly,
    # in size and in content.
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit(
            "Copy mismatch: %s is %d bytes, expected %d bytes from %s"
            % (target, target.stat().st_size, source.stat().st_size, source)
        )
    if digest(target) != digest(source):
        raise SystemExit("Copy mismatch: %s differs from %s" % (target, source))
    print("Published %s -> %s (%d bytes, sha256 %s)"
          % (source, target, target.stat().st_size, digest(target)))


if __name__ == "__main__":
    main()
