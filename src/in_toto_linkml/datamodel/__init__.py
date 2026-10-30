"""Data model package for in-toto."""

from pathlib import Path
from .in_toto_linkml import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "in_toto_linkml.yaml"
