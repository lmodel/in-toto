# Glossary

* [Statement](statement.md) - In the in-toto Attestation Framework, the middle layer of an attestation, which binds it to its subjects and names the type of its predicate. The schema renders it as `InTotoStatement`.
* [Resource descriptor](resource-descriptor.md) - In the in-toto Attestation Framework, a description of an artifact or other resource by URI, digest or content, with optional metadata. The schema renders it as `InTotoResourceDescriptor`.
* [Digest set](digest-set.md) - In the in-toto Attestation Framework, a set of digests over one artifact, keyed by algorithm, from which a consumer picks one it trusts. The schema renders it as `InTotoDigestSet`.
* [Predicate](predicate.md) - In the in-toto Attestation Framework, the innermost layer of an attestation: metadata about the statement's subjects, whose meaning its predicate type names. The schema's predicates extend `InTotoPredicate`.
* [Predicate type](predicate-type.md) - In the in-toto Attestation Framework, a type of predicate, named by a URI that a statement's predicateType holds and that changes with an incompatible change. The schema renders it as `InTotoPredicateType`, the class its adapt copy roots on `Concept`.
