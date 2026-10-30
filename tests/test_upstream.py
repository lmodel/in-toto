"""Checks that the schema renders the in-toto release its copy pins.

src/in_toto_linkml/schema/attestation/ holds the specification pages and
protocol buffer definitions that scripts/check_upstream_release.py pins.
These tests read the copy offline, hold it to the pins, and hold the schema
to the copy: its header, its list of vetted predicates, each predicate's type
URI and each field of the protocol buffer definitions it renders.
"""

import hashlib
import importlib.util
import json
import re
from pathlib import Path

import pytest
import yaml
from linkml_runtime.utils.schemaview import SchemaView

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


# ── The schema against the copy ──────────────────────────────────────────


SCHEMA_DIR = ROOT / "src" / "in_toto_linkml" / "schema"
SCHEMA = SCHEMA_DIR / "in_toto_linkml.yaml"
PROTOS = COPY / "protos" / "in_toto_attestation"
VIEW = SchemaView(str(SCHEMA))

# Each protocol buffer message the schema renders: the class that renders it,
# and the slot that renders each of its fields. A field the in-toto project
# adds fails the test until it is mapped here, or left out below.
MESSAGES = {
    ("v1/statement.proto", "Statement"): (
        "InTotoStatement",
        {
            "type": "statement_type",
            "subject": "subject",
            "predicate_type": "predicate_type",
            "predicate": "predicate",
        },
    ),
    ("v1/resource_descriptor.proto", "ResourceDescriptor"): (
        "InTotoResourceDescriptor",
        {
            "name": "resource_name",
            "uri": "resource_uri",
            "digest": "digest",
            "content": "content",
            "download_location": "download_location",
            "media_type": "media_type",
            "annotations": "annotations",
        },
    ),
    ("predicates/test_result/v0/test_result.proto", "TestResult"): (
        "InTotoTestResult",
        {
            "result": "test_result",
            "configuration": "configuration",
            "url": "test_run_url",
            "passed_tests": "passed_tests",
            "warned_tests": "warned_tests",
            "failed_tests": "failed_tests",
        },
    ),
    ("predicates/svr/v0.1/svr.proto", "SimpleVerificationResult"): (
        "InTotoSimpleVerificationResult",
        {
            "verifier": "svr_verifier",
            "time_created": "time_created",
            "properties": "verified_properties",
        },
    ),
    ("predicates/svr/v0.1/svr.proto", "Verifier"): (
        "InTotoSvrVerifier",
        {"id": "svr_verifier_id", "policy": None},
    ),
    ("predicates/scai/v0/scai.proto", "AttributeReport"): (
        "InTotoScaiAttributeReport",
        {"attributes": "scai_attributes", "producer": "scai_producer"},
    ),
    ("predicates/scai/v0/scai.proto", "AttributeAssertion"): (
        "InTotoScaiAttributeAssertion",
        {
            "attribute": "scai_attribute",
            "target": "scai_target",
            "conditions": "scai_conditions",
            "evidence": "scai_evidence",
        },
    ),
    ("predicates/link/v0/link.proto", "Link"): (
        "InTotoLink",
        {
            "name": "step_name",
            "command": "step_command",
            "materials": "materials",
            "byproducts": "step_byproducts",
            "environment": "step_environment",
        },
    ),
    ("predicates/reference/v0/reference.proto", "Reference"): (
        "InTotoReference",
        {"attester": "reference_attester", "references": "referenced_documents"},
    ),
    ("predicates/reference/v0/reference.proto", "Attester"): (
        "InTotoReferenceAttester",
        {"id": "reference_attester_id"},
    ),
    ("predicates/release/v0.2/release.proto", "Release"): (
        "InTotoRelease",
        {"purl": "release_purl", "package_id": "package_id"},
    ),
    ("predicates/vulns/v0.2/vulns.proto", "Vulns"): (
        "InTotoVulns",
        {"scanner": "vuln_scanner", "metadata": "scan_metadata"},
    ),
    ("predicates/vulns/v0.2/vulns.proto", "Scanner"): (
        "InTotoVulnScanner",
        {
            "uri": "scanner_uri",
            "version": "scanner_version",
            "db": "vuln_db",
            "result": "scan_results",
        },
    ),
    ("predicates/vulns/v0.2/vulns.proto", "VulnDatabase"): (
        "InTotoVulnDatabase",
        {"uri": "db_uri", "version": "db_version", "last_update": "db_last_update"},
    ),
    ("predicates/vulns/v0.2/vulns.proto", "Result"): (
        "InTotoVulnResult",
        {
            "id": "vuln_id",
            "severity": "vuln_severity",
            "annotations": "vuln_annotations",
        },
    ),
    ("predicates/vulns/v0.2/vulns.proto", "Severity"): (
        "InTotoVulnSeverity",
        {"method": "severity_method", "score": "severity_score"},
    ),
    ("predicates/vulns/v0.2/vulns.proto", "ScanMetadata"): (
        "InTotoScanMetadata",
        {"scan_started_on": "scan_started_on", "scan_finished_on": "scan_finished_on"},
    ),
}
# A field mapped to None is left out on purpose: the Simple Verification
# Result page lists no policy field, and says a verifier may add fields of
# its own, which the proto's optional policy is one form of.

FIELD = re.compile(r"^\s*(?:repeated\s+|optional\s+)?[\w.<>, ]+?\s+(\w+)\s*=\s*\d+")
MESSAGE = re.compile(r"^\s*message\s+(\w+)\s*\{")


def _messages(path: Path) -> dict[str, set[str]]:
    """Each message of a .proto file, nested ones by their own name, and the
    names of its fields."""
    found, stack = {}, []
    for line in path.read_text().splitlines():
        line = line.split("//")[0]
        opened = MESSAGE.match(line)
        if opened:
            stack.append(opened.group(1))
            found[stack[-1]] = set()
        elif stack and (field := FIELD.match(line)):
            found[stack[-1]].add(field.group(1))
        stack = stack[: len(stack) - line.count("}")] if "}" in line else stack
    return found


@pytest.mark.parametrize("key", sorted(MESSAGES), ids=lambda k: f"{k[0]}:{k[1]}")
def test_each_proto_field_has_a_slot(key):
    """Every field of a rendered message is mapped, and each mapped slot is
    one the rendering class has."""
    file, message = key
    cls, fields = MESSAGES[key]
    assert _messages(PROTOS / file)[message] == set(fields)
    slots = set(VIEW.class_slots(cls))
    assert {s for s in fields.values() if s} <= slots, cls


def test_every_predicate_class_is_rendered():
    """Each concrete predicate class renders a message mapped above, or the
    Runtime Trace page, which publishes no protocol buffer definition."""
    predicates = {c for c in VIEW.class_descendants("InTotoPredicate", reflexive=False)}
    rendered = {cls for cls, _ in MESSAGES.values()}
    assert predicates - rendered == {"InTotoRuntimeTrace"}


def test_the_header_names_the_pinned_release():
    """The schema header carries the release and commit the watch pins."""
    header = yaml.safe_load(SCHEMA.read_text())
    assert header["version"] == WATCH.PINNED_TAG.removeprefix("v")
    assert header["annotations"]["attestation_tag"] == WATCH.PINNED_TAG
    assert header["annotations"]["attestation_commit"] == WATCH.PINNED_COMMIT
    assert header["source"].endswith(f"/tree/{WATCH.PINNED_TAG}")


def test_the_vetted_predicates_are_the_listed_ones():
    """InTotoVettedPredicate holds one value per predicate the predicates page
    lists as vetted, and nothing else."""
    page = (COPY / "spec" / "predicates" / "README.md").read_text()
    section = page.split("## Vetted Predicates", 1)[1]
    listed = re.findall(r"^-\s+\[([^\]]+)\]", section, re.M)
    # "[SPDX2] and [SPDX3]" share one bullet.
    listed += re.findall(r"^-\s+\[[^\]]+\] and \[([^\]]+)\]", section, re.M)
    values = VIEW.get_enum("InTotoVettedPredicate").permissible_values
    names = {
        "CycloneDX": "CYCLONEDX",
        "Link": "LINK",
        "Reference": "REFERENCE",
        "Release": "RELEASE",
        "Runtime Traces": "RUNTIME_TRACE",
        "SCAI Report": "SCAI",
        "SLSA Provenance": "SLSA_PROVENANCE",
        "SLSA Verification Summary": "SLSA_VERIFICATION_SUMMARY",
        "SPDX2": "SPDX2",
        "SPDX3": "SPDX3",
        "Simple Verification Result": "SIMPLE_VERIFICATION_RESULT",
        "Test Result": "TEST_RESULT",
        "VULNS": "VULNS",
    }
    assert sorted(names[n] for n in listed) == sorted(values)


PAGES = {
    "InTotoTestResult": "test-result.md",
    "InTotoSimpleVerificationResult": "svr.md",
    "InTotoScaiAttributeReport": "scai.md",
    "InTotoLink": "link.md",
    "InTotoReference": "reference.md",
    "InTotoRelease": "release.md",
    "InTotoRuntimeTrace": "runtime-trace.md",
    "InTotoVulns": "vulns_02.md",
}


@pytest.mark.parametrize("cls", sorted(PAGES))
def test_each_predicate_names_the_type_its_page_gives(cls):
    """A predicate class maps to the predicate_type its page's statements
    carry, and the vetted value of the same predicate means that URI too."""
    (mapping,) = VIEW.get_class(cls).exact_mappings
    uri = VIEW.expand_curie(mapping)
    page = (COPY / "spec" / "predicates" / PAGES[cls]).read_text()
    assert f'"predicateType": "{uri}"' in page
    meanings = {
        VIEW.expand_curie(v.meaning)
        for v in VIEW.get_enum("InTotoVettedPredicate").permissible_values.values()
    }
    assert uri in meanings


PAGE_BASE = "https://github.com/in-toto/attestation/blob/v1.2.0/"


def _stated_uris(page: str) -> set[str]:
    """The type URIs a predicate page states: each example's predicateType,
    each Type URI line, and each Type URI line with the major version of the
    page's Version line, as the framework's versioning rule builds it."""
    uris = set(re.findall(r'"predicateType":\s*"([^"]+)"', page))
    typed = re.findall(r"^Type URI: (\S+)$", page, re.M)
    uris.update(typed)
    if version := re.search(r"^Version:? v?(\d+)", page, re.M):
        uris.update(f"{uri}/v{version.group(1)}" for uri in typed)
    return uris


@pytest.mark.parametrize(
    "value", sorted(VIEW.get_enum("InTotoVettedPredicate").permissible_values)
)
def test_each_vetted_value_means_the_uri_its_page_gives(value):
    """A vetted value names, first in see_also, the in-toto page it renders,
    and means a type URI that page states."""
    pv = VIEW.get_enum("InTotoVettedPredicate").permissible_values[value]
    page_url = pv.see_also[0]
    assert page_url.startswith(PAGE_BASE + "spec/predicates/")
    page = (COPY / page_url.removeprefix(PAGE_BASE)).read_text()
    assert VIEW.expand_curie(pv.meaning) in _stated_uris(page)


# ── The pages' own examples ──────────────────────────────────────────────


VALID = ROOT / "tests" / "data" / "valid"

# Each valid example taken from a specification page, and the page. It holds
# the page's values in this schema's keys, so `just test` validates the
# framework's own examples.
PAGE_EXAMPLES = {
    "InTotoDigestSet-page-arn.yaml": "spec/v1/digest_set.md",
    "InTotoRelease-page-oci.yaml": "spec/predicates/release.md",
    "InTotoRelease-page-scoped-npm.yaml": "spec/predicates/release.md",
    "InTotoResourceDescriptor-page-build-service.yaml": "spec/v1/resource_descriptor.md",
    "InTotoResourceDescriptor-page-tekton-taskrun.yaml": "spec/v1/resource_descriptor.md",
    "InTotoSimpleVerificationResult-page-basic.yaml": "spec/predicates/svr.md",
    "InTotoStatement-page-reference.yaml": "spec/predicates/reference.md",
    "InTotoStatement-page-runtime-trace.yaml": "spec/predicates/runtime-trace.md",
    "InTotoStatement-page-test-result.yaml": "spec/predicates/test-result.md",
    "InTotoStatement-page-vulns.yaml": "spec/predicates/vulns_02.md",
}


def _strings(node, key=None):
    """Every string value in a parsed example, reading a JSON text as the
    value it encodes, except predicate_kind, which the schema adds."""
    if isinstance(node, dict):
        for name, value in node.items():
            yield from _strings(value, name)
    elif isinstance(node, list):
        for item in node:
            yield from _strings(item, key)
    elif isinstance(node, str) and key != "predicate_kind":
        try:
            decoded = json.loads(node)
        except ValueError:
            decoded = None
        if isinstance(decoded, (dict, list)):
            yield from _strings(decoded, key)
        else:
            yield node


def test_every_page_example_names_its_page():
    """Each example whose name says it comes from a page is listed above."""
    assert {p.name for p in VALID.glob("*-page-*.yaml")} == set(PAGE_EXAMPLES)


@pytest.mark.parametrize("name", sorted(PAGE_EXAMPLES))
def test_each_page_example_holds_the_pages_values(name):
    """Every string a page example holds appears on its page, so the example
    is the page's and not one written to fit the schema."""
    page = (COPY / PAGE_EXAMPLES[name]).read_text()
    data = yaml.safe_load((VALID / name).read_text())
    strings = list(_strings(data))
    assert strings
    assert [s for s in strings if s not in page] == []
