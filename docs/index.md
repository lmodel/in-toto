# in-toto

This project is a LinkML model of the in-toto Attestation Framework at
release v1.2.0. It covers the statement that binds an attestation to its
subjects, the resource descriptor and digest set that identify an artifact,
the predicate types the in-toto project has vetted, and the eight vetted
predicates that lmodel/slsa does not model.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the elements are named and what the model leaves out
- [`in_toto_linkml.yaml`](schema/in_toto_linkml.yaml): the schema

## Validating data

`linkml-validate -s src/in_toto_linkml/schema/in_toto_linkml.yaml -C InTotoStatement attestation.yaml`
checks a file against the JSON Schema generated from the schema, and
`tests/test_data.py` holds every example to it.

Validate a file before loading it into either model in
`src/in_toto_linkml/datamodel/`. LinkML 1.12.1 generates models that check
less:

- The dataclasses check required fields and enum values, but no pattern, and
  they read an empty required list, such as a scan's empty `scan_results`, as
  a missing one.
- The Pydantic models also check the patterns a field carries itself, such as
  the digest lengths and `release_purl`. They do not check a type's pattern:
  that a timestamp is in UTC, or that a URI's scheme and authority are
  lowercase.
- Neither checks a class's `any_of` or `all_of` conditions: that a digest set
  holds one digest at least, that a resource descriptor has a URI, a digest or
  content, that a monitor log records something, and that a link's material
  has a name and a referenced document a location and a media type.

No check covers these rules:

- that a key appears once in a list of annotations, additional digests or
  object entries, since the attestation's JSON uses it as a key;
- that the subjects' names and URIs, and a link's materials' names, are
  unique;
- that a statement's `predicate_type` is the type URI of the predicate its
  `predicate_kind` names;
- that a timestamp is a real date and time;
- that a release's package URL carries no qualifiers or subpath unless its
  type needs them, and that inline content stays under 1 KB.
