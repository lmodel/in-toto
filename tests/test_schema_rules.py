"""Checks that rules the schema states in more than one place agree."""

from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "in_toto_linkml" / "schema" / "in_toto_linkml.yaml"

# The digest set's fields whose key in the attestation's JSON is camelCase.
JSON_KEYS = {
    "dir_hash": "dirHash",
    "git_commit": "gitCommit",
    "git_tree": "gitTree",
    "git_blob": "gitBlob",
    "git_tag": "gitTag",
}


def test_digest_set_rules_name_every_algorithm():
    """The at-least-one rule and the reserved names cover every named algorithm."""
    sv = SchemaView(str(SCHEMA))
    digest_set = sv.get_class("InTotoDigestSet")
    algorithms = set(digest_set.attributes) - {"additional_digests"}
    in_any_of = {name for rule in digest_set.any_of for name in rule.slot_conditions}
    assert in_any_of == algorithms | {"additional_digests"}

    algorithm = sv.get_class("InTotoAdditionalDigest").attributes["algorithm"]
    reserved = set(algorithm.none_of[0].equals_string_in)
    assert reserved == {JSON_KEYS.get(name, name) for name in algorithms} | algorithms


def test_every_predicate_is_a_kind_of_statement_predicate():
    """The statement's predicate ranges over the base every predicate extends,
    so predicate_kind can name each of them."""
    sv = SchemaView(str(SCHEMA))
    assert sv.induced_slot("statement_predicate", "InTotoStatement").range == (
        "InTotoPredicate"
    )
    for name in sv.class_descendants("InTotoPredicate", reflexive=False):
        assert "predicate_kind" in sv.class_slots(name), name
