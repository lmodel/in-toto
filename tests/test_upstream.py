"""Checks that the schema renders the in-toto release its copy pins.

src/in_toto_linkml/schema/attestation/ holds the specification pages and
protocol buffer definitions that scripts/check_upstream_release.py pins.
These tests read the copy offline and hold it to the pins.
"""

import hashlib
import importlib.util
from pathlib import Path

ROOT = Path(__file__).parent.parent
COPY = ROOT / "src" / "in_toto_linkml" / "schema" / "attestation"
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"


def _watch():
    spec = importlib.util.spec_from_file_location("watch_pins", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


WATCH = _watch()


def _blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def test_the_copy_is_the_pinned_files():
    """Every copied file is the blob the watch pins, and nothing else is there."""
    held = {
        p.relative_to(COPY).as_posix(): _blob_sha(p)
        for p in COPY.rglob("*")
        if p.is_file()
    }
    assert held == WATCH.PINNED_BLOBS


def test_the_watch_hashes_files_as_git_does():
    """The watch's hash is git's object hash, so it matches the trees API."""
    assert WATCH._blob_sha(COPY / "LICENSE") == WATCH.PINNED_BLOBS["LICENSE"]
