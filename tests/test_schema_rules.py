"""Checks that rules the schema states in more than one place agree, and
that the adapt copy can sit beside LOKF and the neighbours' copies."""

import hashlib
from pathlib import Path

import yaml
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


# What a host may import beside this schema's adapt copy: LOKF's schema, pinned
# by the sidecar, and the adapt copies other lmodel repositories release. Each
# neighbour is the schema asset of a release, downloaded and checked against
# the release's .sha256 and its build-provenance attestation, and pinned here
# by that checksum.
COPY = ROOT / ".lokf" / "in-toto.yaml"
LOKF = ROOT / ".lokf" / "lokf.yaml"
NEIGHBOURS = {
    # lmodel/slsa v0.7.0, schema-v0.7.0-slsa.yaml
    "slsa.yaml": "b25407db9480751e521edf36a1ef75ab0ef2d6652d7e153e66afdbfc37aa19ce",
    # lmodel/github-actions v0.2.1, schema-v0.2.1-github-actions.yaml
    "github-actions.yaml": "52224e53939325f56d3470ed6ddd2041cdd53ae7cdb0ac72773829100798452e",
    # lmodel/oscal v0.1.2, schema-v0.1.2-oscal.yaml
    "oscal.yaml": "4eb56d7d1106463ed0a2255a29af14b8d619741acc29863d1e86eb3f8923c710",
    # lmodel/spdx v0.1.0, schema-v0.1.0-spdx.yaml
    "spdx.yaml": "3411cf5d19b1955f0362988c542984e4c817417c7b7b7892647aba1adf1ddd4a",
    # lmodel/nist-sp-800-218 v0.1.1, schema-v0.1.1-nist-sp-800-218.yaml
    "nist-sp-800-218.yaml": "479824cdd95e52226a35ff3a471b7ce93239635ccd5db7ac72a8143cdd1d8495",
    # lmodel/nist-sp-800-53 v0.1.0, schema-v0.1.0-nist-sp-800-53.yaml
    "nist-sp-800-53.yaml": "d32a989b5b855281cb45d707bf59cf52b125f05a09c54930e2b4d45c174c0d99",
    # lmodel/nist-sp-800-171 v0.1.0, schema-v0.1.0-nist-sp-800-171.yaml
    "nist-sp-800-171.yaml": "d204efa6653692da665f8604a8fb8bf445f04b37f41460a5ce2853a014b2982f",
    # lmodel/nist-csf-v2 v0.1.0, schema-v0.1.0-nist-csf-v2.yaml
    "nist-csf-v2.yaml": "5f6bba4c4721f65665c3a0a702ca6b15df5b488048fed454acfe4cc69f7ca9c7",
}
NEIGHBOUR_DIR = ROOT / "tests" / "neighbours"
ELEMENT_KINDS = ("classes", "enums", "types", "subsets")

# The in-toto layer that lmodel/slsa v0.7.0 still defines itself. Its next
# release imports the layer from this schema and drops its own copy, so the
# two copies share these names until a host pins that release; neither copy
# is meant to sit beside the other.
SLSA_LAYER_CLASSES = {
    "InTotoAdditionalDigest",
    "InTotoAnnotation",
    "InTotoDigestSet",
    "InTotoResourceDescriptor",
    "InTotoStatement",
    "InTotoStatementSubject",
}
SLSA_LAYER_KEYS = {
    "additional_digests", "algorithm", "annotation_key", "annotation_values",
    "annotations", "blake2b", "blake2s", "content", "digest", "dir_hash",
    "download_location", "git_blob", "git_commit", "git_tag", "git_tree",
    "gost", "md5", "media_type", "predicate_kind", "predicate_type",
    "resource_name", "resource_uri", "ripemd160", "sha1", "sha224", "sha256",
    "sha384", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "sha512",
    "sha512_224", "sha512_256", "shake128", "shake256", "sm3",
    "statement_type", "subject", "value",
}  # fmt: skip

# Keys the copy shares with a neighbour. LinkML keeps one namespace, and the
# JSON-LD context gives each key one IRI across a composite, whether it is a
# slot or an attribute on either side, so a shared key projects under one
# vocabulary's IRI. The statement's subject and the additional digest's value
# keep the names lmodel/slsa gave them, which the oscal and spdx copies use
# too; any other overlap fails the test.
SHARED_WITH_NEIGHBOURS = {name: set() for name in NEIGHBOURS}
SHARED_WITH_NEIGHBOURS["slsa.yaml"] = SLSA_LAYER_KEYS
SHARED_WITH_NEIGHBOURS["oscal.yaml"] = {"subject", "value"}
SHARED_WITH_NEIGHBOURS["spdx.yaml"] = {"subject", "value"}
SHARED_ELEMENTS = {name: set() for name in NEIGHBOURS}
SHARED_ELEMENTS["slsa.yaml"] = SLSA_LAYER_CLASSES

# The classes `just lokf-adapt` re-roots on Concept, which the README lists
# for the plugins' Known LOKF types setting.
ROOTS = {"InTotoPredicateType"}

MAPPING_KEYS = (
    "mappings",
    "exact_mappings",
    "close_mappings",
    "related_mappings",
    "narrow_mappings",
    "broad_mappings",
)


def _names(path):
    """Each kind of element a schema file declares, and every slot and
    attribute name with the IRI it expands to."""
    doc = yaml.safe_load(path.read_text())
    prefixes = doc.get("prefixes") or {}

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return prefixes[prefix] + local if prefix in prefixes else curie

    default = doc.get("default_prefix")
    elements = {kind: set(doc.get(kind) or {}) for kind in ELEMENT_KINDS}
    slots = {}
    owners = [doc.get("slots") or {}]
    owners += [
        (cls or {}).get("attributes") or {}
        for cls in (doc.get("classes") or {}).values()
    ]
    for owner in owners:
        for name, slot in owner.items():
            uri = (slot or {}).get("slot_uri") or f"{default}:{name}"
            slots.setdefault(name, set()).add(expand(uri))
    return elements, slots


def _mappings(node):
    """Every mapping value anywhere in a parsed schema file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in MAPPING_KEYS:
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _mappings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _mappings(item)


def test_neighbours_are_the_released_assets():
    """Each neighbour copy is byte for byte the asset its release published."""
    assert {p.name for p in NEIGHBOUR_DIR.iterdir()} == set(NEIGHBOURS)
    for name, sha256 in NEIGHBOURS.items():
        digest = hashlib.sha256((NEIGHBOUR_DIR / name).read_bytes()).hexdigest()
        assert digest == sha256, name


def test_names_apart_from_lokf():
    """No class, enum, type or subset name of the copy is LOKF's, and a slot
    name the two share carries LOKF's IRI."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(LOKF)
    for kind in ELEMENT_KINDS:
        assert not elements[kind] & their_elements[kind], kind
    for name in slots.keys() & their_slots.keys():
        assert slots[name] == their_slots[name], name


def test_names_apart_from_neighbours():
    """The only element names and keys the copy shares with a neighbour are
    the listed ones."""
    elements, slots = _names(COPY)
    for name in NEIGHBOURS:
        their_elements, their_slots = _names(NEIGHBOUR_DIR / name)
        shared = set().union(
            *(elements[kind] & their_elements[kind] for kind in ELEMENT_KINDS)
        )
        assert shared == SHARED_ELEMENTS[name], name
        assert slots.keys() & their_slots.keys() == SHARED_WITH_NEIGHBOURS[name], name


def test_copy_roots_the_concept_classes():
    """The copy re-roots exactly the concept classes on Concept and imports
    nothing but the LinkML types and LOKF."""
    doc = yaml.safe_load(COPY.read_text())
    rooted = {
        name for name, cls in doc["classes"].items() if cls.get("is_a") == "Concept"
    }
    assert rooted == ROOTS
    assert doc["imports"] == ["linkml:types", "lokf"]


def test_mappings_use_a_bound_prefix():
    """Every mapping in the copy is a CURIE whose prefix the copy binds. A full
    address that no prefix covers makes every `lokf convert --schema` over the
    copy warn that it has no namespace."""
    doc = yaml.safe_load(COPY.read_text())
    prefixes = doc.get("prefixes") or {}
    mappings = list(_mappings(doc))
    assert mappings
    for mapping in mappings:
        prefix, sep, _ = mapping.partition(":")
        assert sep and prefix in prefixes, mapping
