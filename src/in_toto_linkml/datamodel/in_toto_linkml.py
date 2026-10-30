# Auto generated from in_toto_linkml.yaml by pythongen.py version: 0.0.1
# Schema: in_toto_linkml
#
# id: https://w3id.org/lmodel/in-toto
# description: A LinkML model of the in-toto Attestation Framework: the statement that binds an attestation to its subjects, the resource descriptor and digest set that identify an artifact, the predicate types the in-toto project has vetted, and the vetted predicates that no other lmodel schema models.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String, Uri
from linkml_runtime.utils.metamodelcore import URI

metamodel_version = "1.12.0"
version = "1.2.0"

# Namespaces
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
IN_TOTO = CurieNamespace('in_toto', 'https://in-toto.io/attestation/')
IN_TOTO_LINKML = CurieNamespace('in_toto_linkml', 'https://w3id.org/lmodel/in-toto/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SPDX = CurieNamespace('spdx', 'http://spdx.org/rdf/terms#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = IN_TOTO_LINKML


# Types
class InTotoTimestamp(String):
    """ A point in time in RFC 3339 format in the UTC time zone, written with a trailing Z, such as 1985-04-12T23:20:50.52Z. """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "InTotoTimestamp"
    type_model_uri = IN_TOTO_LINKML.InTotoTimestamp


# Class references



@dataclass(repr=False)
class InTotoDocument(YAMLRoot):
    """
    A document that holds in-toto statements and the predicate types they name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoDocument"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoDocument"
    class_name: ClassVar[str] = "InTotoDocument"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoDocument

    in_toto_statements: Optional[Union[Union[dict, "InTotoStatement"], list[Union[dict, "InTotoStatement"]]]] = empty_list()
    in_toto_predicate_types: Optional[Union[Union[dict, "InTotoPredicateType"], list[Union[dict, "InTotoPredicateType"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="in_toto_statements", slot_type=InTotoStatement, key_name="statement_type", keyed=False)

        self._normalize_inlined_as_list(slot_name="in_toto_predicate_types", slot_type=InTotoPredicateType, key_name="predicate_type_uri", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoDigestSet(YAMLRoot):
    """
    A set of one or more digests over one artifact, keyed by algorithm, from which a consumer picks the algorithm it
    trusts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoDigestSet"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoDigestSet"
    class_name: ClassVar[str] = "InTotoDigestSet"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoDigestSet

    sha256: Optional[str] = None
    sha224: Optional[str] = None
    sha384: Optional[str] = None
    sha512: Optional[str] = None
    sha512_224: Optional[str] = None
    sha512_256: Optional[str] = None
    sha3_224: Optional[str] = None
    sha3_256: Optional[str] = None
    sha3_384: Optional[str] = None
    sha3_512: Optional[str] = None
    shake128: Optional[str] = None
    shake256: Optional[str] = None
    blake2b: Optional[str] = None
    blake2s: Optional[str] = None
    ripemd160: Optional[str] = None
    sm3: Optional[str] = None
    gost: Optional[str] = None
    sha1: Optional[str] = None
    md5: Optional[str] = None
    dir_hash: Optional[str] = None
    git_commit: Optional[str] = None
    git_tree: Optional[str] = None
    git_blob: Optional[str] = None
    git_tag: Optional[str] = None
    additional_digests: Optional[Union[Union[dict, "InTotoAdditionalDigest"], list[Union[dict, "InTotoAdditionalDigest"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.sha256 is not None and not isinstance(self.sha256, str):
            self.sha256 = str(self.sha256)

        if self.sha224 is not None and not isinstance(self.sha224, str):
            self.sha224 = str(self.sha224)

        if self.sha384 is not None and not isinstance(self.sha384, str):
            self.sha384 = str(self.sha384)

        if self.sha512 is not None and not isinstance(self.sha512, str):
            self.sha512 = str(self.sha512)

        if self.sha512_224 is not None and not isinstance(self.sha512_224, str):
            self.sha512_224 = str(self.sha512_224)

        if self.sha512_256 is not None and not isinstance(self.sha512_256, str):
            self.sha512_256 = str(self.sha512_256)

        if self.sha3_224 is not None and not isinstance(self.sha3_224, str):
            self.sha3_224 = str(self.sha3_224)

        if self.sha3_256 is not None and not isinstance(self.sha3_256, str):
            self.sha3_256 = str(self.sha3_256)

        if self.sha3_384 is not None and not isinstance(self.sha3_384, str):
            self.sha3_384 = str(self.sha3_384)

        if self.sha3_512 is not None and not isinstance(self.sha3_512, str):
            self.sha3_512 = str(self.sha3_512)

        if self.shake128 is not None and not isinstance(self.shake128, str):
            self.shake128 = str(self.shake128)

        if self.shake256 is not None and not isinstance(self.shake256, str):
            self.shake256 = str(self.shake256)

        if self.blake2b is not None and not isinstance(self.blake2b, str):
            self.blake2b = str(self.blake2b)

        if self.blake2s is not None and not isinstance(self.blake2s, str):
            self.blake2s = str(self.blake2s)

        if self.ripemd160 is not None and not isinstance(self.ripemd160, str):
            self.ripemd160 = str(self.ripemd160)

        if self.sm3 is not None and not isinstance(self.sm3, str):
            self.sm3 = str(self.sm3)

        if self.gost is not None and not isinstance(self.gost, str):
            self.gost = str(self.gost)

        if self.sha1 is not None and not isinstance(self.sha1, str):
            self.sha1 = str(self.sha1)

        if self.md5 is not None and not isinstance(self.md5, str):
            self.md5 = str(self.md5)

        if self.dir_hash is not None and not isinstance(self.dir_hash, str):
            self.dir_hash = str(self.dir_hash)

        if self.git_commit is not None and not isinstance(self.git_commit, str):
            self.git_commit = str(self.git_commit)

        if self.git_tree is not None and not isinstance(self.git_tree, str):
            self.git_tree = str(self.git_tree)

        if self.git_blob is not None and not isinstance(self.git_blob, str):
            self.git_blob = str(self.git_blob)

        if self.git_tag is not None and not isinstance(self.git_tag, str):
            self.git_tag = str(self.git_tag)

        self._normalize_inlined_as_list(slot_name="additional_digests", slot_type=InTotoAdditionalDigest, key_name="algorithm", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoAdditionalDigest(YAMLRoot):
    """
    One digest under an algorithm that InTotoDigestSet does not name, such as an SCS's own revision type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoAdditionalDigest"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoAdditionalDigest"
    class_name: ClassVar[str] = "InTotoAdditionalDigest"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoAdditionalDigest

    algorithm: str = None
    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.algorithm):
            self.MissingRequiredField("algorithm")
        if not isinstance(self.algorithm, str):
            self.algorithm = str(self.algorithm)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoAnnotation(YAMLRoot):
    """
    One vendor-specific annotation on a resource descriptor: a key and its values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoAnnotation"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoAnnotation"
    class_name: ClassVar[str] = "InTotoAnnotation"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoAnnotation

    annotation_key: str = None
    annotation_values: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.annotation_key):
            self.MissingRequiredField("annotation_key")
        if not isinstance(self.annotation_key, str):
            self.annotation_key = str(self.annotation_key)

        if not isinstance(self.annotation_values, list):
            self.annotation_values = [self.annotation_values] if self.annotation_values is not None else []
        self.annotation_values = [v if isinstance(v, str) else str(v) for v in self.annotation_values]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoResourceDescriptor(YAMLRoot):
    """
    A reference to a software artifact or other resource by URI or digest, or the resource itself as content, with
    optional metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoResourceDescriptor"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoResourceDescriptor"
    class_name: ClassVar[str] = "InTotoResourceDescriptor"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoResourceDescriptor

    resource_uri: Optional[Union[str, URI]] = None
    digest: Optional[Union[dict, InTotoDigestSet]] = None
    resource_name: Optional[str] = None
    download_location: Optional[Union[str, URI]] = None
    media_type: Optional[str] = None
    content: Optional[str] = None
    annotations: Optional[Union[Union[dict, InTotoAnnotation], list[Union[dict, InTotoAnnotation]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.resource_uri is not None and not isinstance(self.resource_uri, URI):
            self.resource_uri = URI(self.resource_uri)

        if self.digest is not None and not isinstance(self.digest, InTotoDigestSet):
            self.digest = InTotoDigestSet(**as_dict(self.digest))

        if self.resource_name is not None and not isinstance(self.resource_name, str):
            self.resource_name = str(self.resource_name)

        if self.download_location is not None and not isinstance(self.download_location, URI):
            self.download_location = URI(self.download_location)

        if self.media_type is not None and not isinstance(self.media_type, str):
            self.media_type = str(self.media_type)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        self._normalize_inlined_as_list(slot_name="annotations", slot_type=InTotoAnnotation, key_name="annotation_key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoStatementSubject(InTotoResourceDescriptor):
    """
    One artifact an in-toto statement is about: a resource descriptor that carries a digest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoStatementSubject"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoStatementSubject"
    class_name: ClassVar[str] = "InTotoStatementSubject"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoStatementSubject

    digest: Union[dict, InTotoDigestSet] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.digest):
            self.MissingRequiredField("digest")
        if not isinstance(self.digest, InTotoDigestSet):
            self.digest = InTotoDigestSet(**as_dict(self.digest))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoStatement(YAMLRoot):
    """
    The statement layer of an in-toto attestation: the subjects it is about, the type of its predicate and the
    predicate itself.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoStatement"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoStatement"
    class_name: ClassVar[str] = "InTotoStatement"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoStatement

    statement_type: Union[str, URI] = None
    subject: Union[Union[dict, InTotoStatementSubject], list[Union[dict, InTotoStatementSubject]]] = None
    predicate_type: Union[str, URI] = None
    statement_predicate: Optional[Union[dict, "InTotoPredicate"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.statement_type):
            self.MissingRequiredField("statement_type")
        if not isinstance(self.statement_type, URI):
            self.statement_type = URI(self.statement_type)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, list):
            self.subject = [self.subject] if self.subject is not None else []
        self.subject = [v if isinstance(v, InTotoStatementSubject) else InTotoStatementSubject(**as_dict(v)) for v in self.subject]

        if self._is_empty(self.predicate_type):
            self.MissingRequiredField("predicate_type")
        if not isinstance(self.predicate_type, URI):
            self.predicate_type = URI(self.predicate_type)

        if self.statement_predicate is not None and not isinstance(self.statement_predicate, InTotoPredicate):
            self.statement_predicate = InTotoPredicate(**as_dict(self.statement_predicate))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoPredicate(YAMLRoot):
    """
    The base of every predicate an in-toto statement can carry; predicate_kind names the concrete kind.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoPredicate"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoPredicate"
    class_name: ClassVar[str] = "InTotoPredicate"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoPredicate

    predicate_kind: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self.predicate_kind = str(self.class_name)

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "predicate_kind"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class InTotoPredicateType(YAMLRoot):
    """
    A type of predicate an in-toto statement can carry, named by the URI a statement's predicate_type holds.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoPredicateType"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoPredicateType"
    class_name: ClassVar[str] = "InTotoPredicateType"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoPredicateType

    predicate_type_uri: Union[str, URI] = None
    predicate_version: Optional[str] = None
    predicate_specification: Optional[Union[str, URI]] = None
    vetted_as: Optional[Union[str, "InTotoVettedPredicate"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.predicate_type_uri):
            self.MissingRequiredField("predicate_type_uri")
        if not isinstance(self.predicate_type_uri, URI):
            self.predicate_type_uri = URI(self.predicate_type_uri)

        if self.predicate_version is not None and not isinstance(self.predicate_version, str):
            self.predicate_version = str(self.predicate_version)

        if self.predicate_specification is not None and not isinstance(self.predicate_specification, URI):
            self.predicate_specification = URI(self.predicate_specification)

        if self.vetted_as is not None and not isinstance(self.vetted_as, InTotoVettedPredicate):
            self.vetted_as = InTotoVettedPredicate(self.vetted_as)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoObjectEntry(YAMLRoot):
    """
    One key of a JSON object whose keys the framework leaves to the producer, and the key's values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoObjectEntry"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoObjectEntry"
    class_name: ClassVar[str] = "InTotoObjectEntry"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoObjectEntry

    entry_key: str = None
    entry_values: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.entry_key):
            self.MissingRequiredField("entry_key")
        if not isinstance(self.entry_key, str):
            self.entry_key = str(self.entry_key)

        if not isinstance(self.entry_values, list):
            self.entry_values = [self.entry_values] if self.entry_values is not None else []
        self.entry_values = [v if isinstance(v, str) else str(v) for v in self.entry_values]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoTestResult(InTotoPredicate):
    """
    The predicate that records the result of one run of a test suite against the subjects, with the names of the tests
    that passed, warned and failed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoTestResult"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoTestResult"
    class_name: ClassVar[str] = "InTotoTestResult"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoTestResult

    test_result: Union[str, "InTotoTestResultValue"] = None
    configuration: Union[Union[dict, InTotoResourceDescriptor], list[Union[dict, InTotoResourceDescriptor]]] = None
    test_run_url: Optional[Union[str, URI]] = None
    passed_tests: Optional[Union[str, list[str]]] = empty_list()
    warned_tests: Optional[Union[str, list[str]]] = empty_list()
    failed_tests: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.test_result):
            self.MissingRequiredField("test_result")
        if not isinstance(self.test_result, InTotoTestResultValue):
            self.test_result = InTotoTestResultValue(self.test_result)

        if self._is_empty(self.configuration):
            self.MissingRequiredField("configuration")
        if not isinstance(self.configuration, list):
            self.configuration = [self.configuration] if self.configuration is not None else []
        self.configuration = [v if isinstance(v, InTotoResourceDescriptor) else InTotoResourceDescriptor(**as_dict(v)) for v in self.configuration]

        if self.test_run_url is not None and not isinstance(self.test_run_url, URI):
            self.test_run_url = URI(self.test_run_url)

        if not isinstance(self.passed_tests, list):
            self.passed_tests = [self.passed_tests] if self.passed_tests is not None else []
        self.passed_tests = [v if isinstance(v, str) else str(v) for v in self.passed_tests]

        if not isinstance(self.warned_tests, list):
            self.warned_tests = [self.warned_tests] if self.warned_tests is not None else []
        self.warned_tests = [v if isinstance(v, str) else str(v) for v in self.warned_tests]

        if not isinstance(self.failed_tests, list):
            self.failed_tests = [self.failed_tests] if self.failed_tests is not None else []
        self.failed_tests = [v if isinstance(v, str) else str(v) for v in self.failed_tests]

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


@dataclass(repr=False)
class InTotoSimpleVerificationResult(InTotoPredicate):
    """
    The predicate that says a verifier evaluated the subjects against one or more policies, and which properties
    passed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoSimpleVerificationResult"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoSimpleVerificationResult"
    class_name: ClassVar[str] = "InTotoSimpleVerificationResult"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoSimpleVerificationResult

    svr_verifier: Union[dict, "InTotoSvrVerifier"] = None
    time_created: Union[str, InTotoTimestamp] = None
    verified_properties: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.svr_verifier):
            self.MissingRequiredField("svr_verifier")
        if not isinstance(self.svr_verifier, InTotoSvrVerifier):
            self.svr_verifier = InTotoSvrVerifier(**as_dict(self.svr_verifier))

        if self._is_empty(self.time_created):
            self.MissingRequiredField("time_created")
        if not isinstance(self.time_created, InTotoTimestamp):
            self.time_created = InTotoTimestamp(self.time_created)

        if self._is_empty(self.verified_properties):
            self.MissingRequiredField("verified_properties")
        if not isinstance(self.verified_properties, list):
            self.verified_properties = [self.verified_properties] if self.verified_properties is not None else []
        self.verified_properties = [v if isinstance(v, str) else str(v) for v in self.verified_properties]

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


@dataclass(repr=False)
class InTotoSvrVerifier(YAMLRoot):
    """
    The entity that performed a simple verification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoSvrVerifier"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoSvrVerifier"
    class_name: ClassVar[str] = "InTotoSvrVerifier"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoSvrVerifier

    svr_verifier_id: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.svr_verifier_id):
            self.MissingRequiredField("svr_verifier_id")
        if not isinstance(self.svr_verifier_id, URI):
            self.svr_verifier_id = URI(self.svr_verifier_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoScaiAttributeReport(InTotoPredicate):
    """
    The Software Supply Chain Attribute Integrity (SCAI) predicate: assertions about functional attributes of the
    subjects or their producer, each with the evidence for it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoScaiAttributeReport"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoScaiAttributeReport"
    class_name: ClassVar[str] = "InTotoScaiAttributeReport"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoScaiAttributeReport

    scai_attributes: Union[Union[dict, "InTotoScaiAttributeAssertion"], list[Union[dict, "InTotoScaiAttributeAssertion"]]] = None
    scai_producer: Optional[Union[dict, InTotoResourceDescriptor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scai_attributes):
            self.MissingRequiredField("scai_attributes")
        self._normalize_inlined_as_list(slot_name="scai_attributes", slot_type=InTotoScaiAttributeAssertion, key_name="scai_attribute", keyed=False)

        if self.scai_producer is not None and not isinstance(self.scai_producer, InTotoResourceDescriptor):
            self.scai_producer = InTotoResourceDescriptor(**as_dict(self.scai_producer))

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


@dataclass(repr=False)
class InTotoScaiAttributeAssertion(YAMLRoot):
    """
    One SCAI assertion: an attribute of the subject or its producer, what it applies to, under which conditions, and
    the evidence for it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoScaiAttributeAssertion"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoScaiAttributeAssertion"
    class_name: ClassVar[str] = "InTotoScaiAttributeAssertion"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoScaiAttributeAssertion

    scai_attribute: str = None
    scai_target: Optional[Union[dict, InTotoResourceDescriptor]] = None
    scai_conditions: Optional[Union[Union[dict, InTotoObjectEntry], list[Union[dict, InTotoObjectEntry]]]] = empty_list()
    scai_evidence: Optional[Union[dict, InTotoResourceDescriptor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scai_attribute):
            self.MissingRequiredField("scai_attribute")
        if not isinstance(self.scai_attribute, str):
            self.scai_attribute = str(self.scai_attribute)

        if self.scai_target is not None and not isinstance(self.scai_target, InTotoResourceDescriptor):
            self.scai_target = InTotoResourceDescriptor(**as_dict(self.scai_target))

        self._normalize_inlined_as_list(slot_name="scai_conditions", slot_type=InTotoObjectEntry, key_name="entry_key", keyed=False)

        if self.scai_evidence is not None and not isinstance(self.scai_evidence, InTotoResourceDescriptor):
            self.scai_evidence = InTotoResourceDescriptor(**as_dict(self.scai_evidence))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoLink(InTotoPredicate):
    """
    The predicate that records one step of an in-toto layout: the command it ran and the materials it read, for a
    supply chain that migrates from in-toto 0.9 links.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoLink"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoLink"
    class_name: ClassVar[str] = "InTotoLink"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoLink

    step_name: str = None
    step_command: Optional[Union[str, list[str]]] = empty_list()
    materials: Optional[Union[Union[dict, "InTotoLinkMaterial"], list[Union[dict, "InTotoLinkMaterial"]]]] = empty_list()
    step_byproducts: Optional[Union[Union[dict, InTotoObjectEntry], list[Union[dict, InTotoObjectEntry]]]] = empty_list()
    step_environment: Optional[Union[Union[dict, InTotoObjectEntry], list[Union[dict, InTotoObjectEntry]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.step_name):
            self.MissingRequiredField("step_name")
        if not isinstance(self.step_name, str):
            self.step_name = str(self.step_name)

        if not isinstance(self.step_command, list):
            self.step_command = [self.step_command] if self.step_command is not None else []
        self.step_command = [v if isinstance(v, str) else str(v) for v in self.step_command]

        if not isinstance(self.materials, list):
            self.materials = [self.materials] if self.materials is not None else []
        self.materials = [v if isinstance(v, InTotoLinkMaterial) else InTotoLinkMaterial(**as_dict(v)) for v in self.materials]

        self._normalize_inlined_as_list(slot_name="step_byproducts", slot_type=InTotoObjectEntry, key_name="entry_key", keyed=False)

        self._normalize_inlined_as_list(slot_name="step_environment", slot_type=InTotoObjectEntry, key_name="entry_key", keyed=False)

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


@dataclass(repr=False)
class InTotoLinkMaterial(InTotoResourceDescriptor):
    """
    One material of a link, a resource descriptor with a name and a digest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoLinkMaterial"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoLinkMaterial"
    class_name: ClassVar[str] = "InTotoLinkMaterial"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoLinkMaterial

    digest: Union[dict, InTotoDigestSet] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.digest):
            self.MissingRequiredField("digest")
        if not isinstance(self.digest, InTotoDigestSet):
            self.digest = InTotoDigestSet(**as_dict(self.digest))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoReference(InTotoPredicate):
    """
    The predicate that points from the subjects, as a whole, to documents about them, such as a bill of materials.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoReference"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoReference"
    class_name: ClassVar[str] = "InTotoReference"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoReference

    reference_attester: Union[dict, "InTotoReferenceAttester"] = None
    referenced_documents: Union[Union[dict, "InTotoReferencedDocument"], list[Union[dict, "InTotoReferencedDocument"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference_attester):
            self.MissingRequiredField("reference_attester")
        if not isinstance(self.reference_attester, InTotoReferenceAttester):
            self.reference_attester = InTotoReferenceAttester(**as_dict(self.reference_attester))

        if self._is_empty(self.referenced_documents):
            self.MissingRequiredField("referenced_documents")
        if not isinstance(self.referenced_documents, list):
            self.referenced_documents = [self.referenced_documents] if self.referenced_documents is not None else []
        self.referenced_documents = [v if isinstance(v, InTotoReferencedDocument) else InTotoReferencedDocument(**as_dict(v)) for v in self.referenced_documents]

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


@dataclass(repr=False)
class InTotoReferenceAttester(YAMLRoot):
    """
    The system that provides the documents a Reference predicate points to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoReferenceAttester"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoReferenceAttester"
    class_name: ClassVar[str] = "InTotoReferenceAttester"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoReferenceAttester

    reference_attester_id: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference_attester_id):
            self.MissingRequiredField("reference_attester_id")
        if not isinstance(self.reference_attester_id, URI):
            self.reference_attester_id = URI(self.reference_attester_id)

        super().__post_init__(**kwargs)


class InTotoReferencedDocument(InTotoResourceDescriptor):
    """
    One document a Reference predicate points to: a resource descriptor with a download location and a media type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoReferencedDocument"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoReferencedDocument"
    class_name: ClassVar[str] = "InTotoReferencedDocument"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoReferencedDocument


@dataclass(repr=False)
class InTotoRelease(InTotoPredicate):
    """
    The predicate that ties the subjects to one release name and version of a package, so that consumers can check
    what the release should contain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoRelease"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoRelease"
    class_name: ClassVar[str] = "InTotoRelease"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoRelease

    release_purl: Union[str, URI] = None
    package_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.release_purl):
            self.MissingRequiredField("release_purl")
        if not isinstance(self.release_purl, URI):
            self.release_purl = URI(self.release_purl)

        if self.package_id is not None and not isinstance(self.package_id, str):
            self.package_id = str(self.package_id)

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


@dataclass(repr=False)
class InTotoRuntimeTrace(InTotoPredicate):
    """
    The predicate that records what a monitor traced while a supply chain step, such as a build, ran.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoRuntimeTrace"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoRuntimeTrace"
    class_name: ClassVar[str] = "InTotoRuntimeTrace"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoRuntimeTrace

    trace_monitor: Union[dict, "InTotoTraceMonitor"] = None
    monitored_process: Union[dict, "InTotoMonitoredProcess"] = None
    monitor_log: Union[dict, "InTotoMonitorLog"] = None
    trace_metadata: Optional[Union[dict, "InTotoTraceMetadata"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.trace_monitor):
            self.MissingRequiredField("trace_monitor")
        if not isinstance(self.trace_monitor, InTotoTraceMonitor):
            self.trace_monitor = InTotoTraceMonitor(**as_dict(self.trace_monitor))

        if self._is_empty(self.monitored_process):
            self.MissingRequiredField("monitored_process")
        if not isinstance(self.monitored_process, InTotoMonitoredProcess):
            self.monitored_process = InTotoMonitoredProcess(**as_dict(self.monitored_process))

        if self._is_empty(self.monitor_log):
            self.MissingRequiredField("monitor_log")
        if not isinstance(self.monitor_log, InTotoMonitorLog):
            self.monitor_log = InTotoMonitorLog(**as_dict(self.monitor_log))

        if self.trace_metadata is not None and not isinstance(self.trace_metadata, InTotoTraceMetadata):
            self.trace_metadata = InTotoTraceMetadata(**as_dict(self.trace_metadata))

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


@dataclass(repr=False)
class InTotoTraceMonitor(YAMLRoot):
    """
    The monitor instance that produced a runtime trace.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoTraceMonitor"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoTraceMonitor"
    class_name: ClassVar[str] = "InTotoTraceMonitor"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoTraceMonitor

    monitor_type: Union[str, URI] = None
    monitor_config_source: Optional[Union[dict, InTotoResourceDescriptor]] = None
    trace_policy: Optional[Union[Union[dict, InTotoObjectEntry], list[Union[dict, InTotoObjectEntry]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.monitor_type):
            self.MissingRequiredField("monitor_type")
        if not isinstance(self.monitor_type, URI):
            self.monitor_type = URI(self.monitor_type)

        if self.monitor_config_source is not None and not isinstance(self.monitor_config_source, InTotoResourceDescriptor):
            self.monitor_config_source = InTotoResourceDescriptor(**as_dict(self.monitor_config_source))

        self._normalize_inlined_as_list(slot_name="trace_policy", slot_type=InTotoObjectEntry, key_name="entry_key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoMonitoredProcess(YAMLRoot):
    """
    The process a runtime trace watched.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoMonitoredProcess"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoMonitoredProcess"
    class_name: ClassVar[str] = "InTotoMonitoredProcess"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoMonitoredProcess

    host_id: Union[str, URI] = None
    process_type: Union[str, URI] = None
    process_event: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.host_id):
            self.MissingRequiredField("host_id")
        if not isinstance(self.host_id, URI):
            self.host_id = URI(self.host_id)

        if self._is_empty(self.process_type):
            self.MissingRequiredField("process_type")
        if not isinstance(self.process_type, URI):
            self.process_type = URI(self.process_type)

        if self._is_empty(self.process_event):
            self.MissingRequiredField("process_event")
        if not isinstance(self.process_event, str):
            self.process_event = str(self.process_event)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoMonitorLog(YAMLRoot):
    """
    The events a runtime trace's monitor recorded: processes, network activity and file accesses, at least one of them.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoMonitorLog"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoMonitorLog"
    class_name: ClassVar[str] = "InTotoMonitorLog"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoMonitorLog

    traced_processes: Optional[Union[str, list[str]]] = empty_list()
    traced_network: Optional[Union[str, list[str]]] = empty_list()
    file_access: Optional[Union[Union[dict, InTotoResourceDescriptor], list[Union[dict, InTotoResourceDescriptor]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.traced_processes, list):
            self.traced_processes = [self.traced_processes] if self.traced_processes is not None else []
        self.traced_processes = [v if isinstance(v, str) else str(v) for v in self.traced_processes]

        if not isinstance(self.traced_network, list):
            self.traced_network = [self.traced_network] if self.traced_network is not None else []
        self.traced_network = [v if isinstance(v, str) else str(v) for v in self.traced_network]

        if not isinstance(self.file_access, list):
            self.file_access = [self.file_access] if self.file_access is not None else []
        self.file_access = [v if isinstance(v, InTotoResourceDescriptor) else InTotoResourceDescriptor(**as_dict(v)) for v in self.file_access]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoTraceMetadata(YAMLRoot):
    """
    Other properties of a runtime trace's monitoring event.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoTraceMetadata"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoTraceMetadata"
    class_name: ClassVar[str] = "InTotoTraceMetadata"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoTraceMetadata

    build_started_on: Optional[Union[str, InTotoTimestamp]] = None
    build_finished_on: Optional[Union[str, InTotoTimestamp]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.build_started_on is not None and not isinstance(self.build_started_on, InTotoTimestamp):
            self.build_started_on = InTotoTimestamp(self.build_started_on)

        if self.build_finished_on is not None and not isinstance(self.build_finished_on, InTotoTimestamp):
            self.build_finished_on = InTotoTimestamp(self.build_finished_on)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoVulns(InTotoPredicate):
    """
    The predicate that records the result of one vulnerability scan of the subjects: the scanner, its database and the
    vulnerabilities it found.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoVulns"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoVulns"
    class_name: ClassVar[str] = "InTotoVulns"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoVulns

    vuln_scanner: Union[dict, "InTotoVulnScanner"] = None
    scan_metadata: Union[dict, "InTotoScanMetadata"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.vuln_scanner):
            self.MissingRequiredField("vuln_scanner")
        if not isinstance(self.vuln_scanner, InTotoVulnScanner):
            self.vuln_scanner = InTotoVulnScanner(**as_dict(self.vuln_scanner))

        if self._is_empty(self.scan_metadata):
            self.MissingRequiredField("scan_metadata")
        if not isinstance(self.scan_metadata, InTotoScanMetadata):
            self.scan_metadata = InTotoScanMetadata(**as_dict(self.scan_metadata))

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


@dataclass(repr=False)
class InTotoVulnScanner(YAMLRoot):
    """
    The scanner a VULNS predicate records, with its results.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoVulnScanner"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoVulnScanner"
    class_name: ClassVar[str] = "InTotoVulnScanner"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoVulnScanner

    scanner_uri: Union[str, URI] = None
    scan_results: Union[Union[dict, "InTotoVulnResult"], list[Union[dict, "InTotoVulnResult"]]] = None
    scanner_version: Optional[str] = None
    vuln_db: Optional[Union[dict, "InTotoVulnDatabase"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scanner_uri):
            self.MissingRequiredField("scanner_uri")
        if not isinstance(self.scanner_uri, URI):
            self.scanner_uri = URI(self.scanner_uri)

        if self._is_empty(self.scan_results):
            self.MissingRequiredField("scan_results")
        self._normalize_inlined_as_list(slot_name="scan_results", slot_type=InTotoVulnResult, key_name="vuln_id", keyed=False)

        if self.scanner_version is not None and not isinstance(self.scanner_version, str):
            self.scanner_version = str(self.scanner_version)

        if self.vuln_db is not None and not isinstance(self.vuln_db, InTotoVulnDatabase):
            self.vuln_db = InTotoVulnDatabase(**as_dict(self.vuln_db))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoVulnDatabase(YAMLRoot):
    """
    The vulnerability database a scanner used.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoVulnDatabase"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoVulnDatabase"
    class_name: ClassVar[str] = "InTotoVulnDatabase"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoVulnDatabase

    db_last_update: Union[str, InTotoTimestamp] = None
    db_uri: Optional[Union[str, URI]] = None
    db_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.db_last_update):
            self.MissingRequiredField("db_last_update")
        if not isinstance(self.db_last_update, InTotoTimestamp):
            self.db_last_update = InTotoTimestamp(self.db_last_update)

        if self.db_uri is not None and not isinstance(self.db_uri, URI):
            self.db_uri = URI(self.db_uri)

        if self.db_version is not None and not isinstance(self.db_version, str):
            self.db_version = str(self.db_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoVulnResult(YAMLRoot):
    """
    One vulnerability a scanner found.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoVulnResult"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoVulnResult"
    class_name: ClassVar[str] = "InTotoVulnResult"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoVulnResult

    vuln_id: str = None
    vuln_severity: Union[Union[dict, "InTotoVulnSeverity"], list[Union[dict, "InTotoVulnSeverity"]]] = None
    vuln_annotations: Optional[Union[Union[dict, InTotoObjectEntry], list[Union[dict, InTotoObjectEntry]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.vuln_id):
            self.MissingRequiredField("vuln_id")
        if not isinstance(self.vuln_id, str):
            self.vuln_id = str(self.vuln_id)

        if self._is_empty(self.vuln_severity):
            self.MissingRequiredField("vuln_severity")
        self._normalize_inlined_as_list(slot_name="vuln_severity", slot_type=InTotoVulnSeverity, key_name="severity_method", keyed=False)

        self._normalize_inlined_as_list(slot_name="vuln_annotations", slot_type=InTotoObjectEntry, key_name="entry_key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoVulnSeverity(YAMLRoot):
    """
    One severity score of a vulnerability, by one scoring method.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoVulnSeverity"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoVulnSeverity"
    class_name: ClassVar[str] = "InTotoVulnSeverity"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoVulnSeverity

    severity_method: str = None
    severity_score: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.severity_method):
            self.MissingRequiredField("severity_method")
        if not isinstance(self.severity_method, str):
            self.severity_method = str(self.severity_method)

        if self._is_empty(self.severity_score):
            self.MissingRequiredField("severity_score")
        if not isinstance(self.severity_score, str):
            self.severity_score = str(self.severity_score)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoScanMetadata(YAMLRoot):
    """
    When a vulnerability scan ran.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoScanMetadata"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoScanMetadata"
    class_name: ClassVar[str] = "InTotoScanMetadata"
    class_model_uri: ClassVar[URIRef] = IN_TOTO_LINKML.InTotoScanMetadata

    scan_started_on: Union[str, InTotoTimestamp] = None
    scan_finished_on: Union[str, InTotoTimestamp] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scan_started_on):
            self.MissingRequiredField("scan_started_on")
        if not isinstance(self.scan_started_on, InTotoTimestamp):
            self.scan_started_on = InTotoTimestamp(self.scan_started_on)

        if self._is_empty(self.scan_finished_on):
            self.MissingRequiredField("scan_finished_on")
        if not isinstance(self.scan_finished_on, InTotoTimestamp):
            self.scan_finished_on = InTotoTimestamp(self.scan_finished_on)

        super().__post_init__(**kwargs)


# Enumerations
class InTotoTestResultValue(EnumDefinitionImpl):
    """
    The result of a test run, as a Test Result predicate records it.
    """
    PASSED = PermissibleValue(
        text="PASSED",
        description="The run passed.")
    WARNED = PermissibleValue(
        text="WARNED",
        description="The run passed with warnings.")
    FAILED = PermissibleValue(
        text="FAILED",
        description="The run failed.")

    _defn = EnumDefinition(
        name="InTotoTestResultValue",
        description="The result of a test run, as a Test Result predicate records it.",
    )

class InTotoVettedPredicate(EnumDefinitionImpl):
    """
    The thirteen predicate types the in-toto project lists as vetted at release v1.2.0, each with the predicate_type a
    statement of it carries at the version its page describes.
    """
    CYCLONEDX = PermissibleValue(
        text="CYCLONEDX",
        description="A CycloneDX bill of materials for software artifacts.",
        meaning=None)
    LINK = PermissibleValue(
        text="LINK",
        description="One step of an in-toto layout, for migration from in-toto 0.9.",
        meaning=IN_TOTO["link/v0.3"])
    REFERENCE = PermissibleValue(
        text="REFERENCE",
        description="References to documents relevant to a resource.",
        meaning=IN_TOTO["reference/v0.1"])
    RELEASE = PermissibleValue(
        text="RELEASE",
        description="An artifact that is part of a given release version.",
        meaning=IN_TOTO["release/v0.1"])
    RUNTIME_TRACE = PermissibleValue(
        text="RUNTIME_TRACE",
        description="Runtime traces of software supply chain operations.",
        meaning=IN_TOTO["runtime-trace/v0.1"])
    SCAI = PermissibleValue(
        text="SCAI",
        description="Evidence-based assertions about software artifact and supply chain attributes or behaviour.",
        meaning=IN_TOTO["scai/v0.3"])
    SLSA_PROVENANCE = PermissibleValue(
        text="SLSA_PROVENANCE",
        description="How an artifact or set of artifacts was produced; lmodel/slsa models it.",
        meaning=None)
    SLSA_VERIFICATION_SUMMARY = PermissibleValue(
        text="SLSA_VERIFICATION_SUMMARY",
        description="A SLSA verification decision about a software artifact; lmodel/slsa models it.",
        meaning=None)
    SPDX2 = PermissibleValue(
        text="SPDX2",
        description="An SPDX 2 bill of materials for software artifacts.",
        meaning=None)
    SPDX3 = PermissibleValue(
        text="SPDX3",
        description="An SPDX 3 bill of materials for software artifacts.",
        meaning=None)
    SIMPLE_VERIFICATION_RESULT = PermissibleValue(
        text="SIMPLE_VERIFICATION_RESULT",
        description="Evidence that an artifact was evaluated against one or more policies.",
        meaning=IN_TOTO["svr/v0.1"])
    TEST_RESULT = PermissibleValue(
        text="TEST_RESULT",
        description="The results of any type of test.",
        meaning=IN_TOTO["test-result/v0.1"])
    VULNS = PermissibleValue(
        text="VULNS",
        description="The results of a vulnerability scan of software artifacts.",
        meaning=IN_TOTO["vulns/v0.2"])

    _defn = EnumDefinition(
        name="InTotoVettedPredicate",
        description="""The thirteen predicate types the in-toto project lists as vetted at release v1.2.0, each with the predicate_type a statement of it carries at the version its page describes.""",
    )

# Slots
class slots:
    pass

slots.resource_uri = Slot(uri=IN_TOTO_LINKML.resource_uri, name="resource_uri", curie=IN_TOTO_LINKML.curie('resource_uri'),
                   model_uri=IN_TOTO_LINKML.resource_uri, domain=None, range=Optional[Union[str, URI]])

slots.digest = Slot(uri=IN_TOTO_LINKML.digest, name="digest", curie=IN_TOTO_LINKML.curie('digest'),
                   model_uri=IN_TOTO_LINKML.digest, domain=None, range=Optional[Union[dict, InTotoDigestSet]])

slots.inTotoDocument__in_toto_statements = Slot(uri=IN_TOTO_LINKML.in_toto_statements, name="inTotoDocument__in_toto_statements", curie=IN_TOTO_LINKML.curie('in_toto_statements'),
                   model_uri=IN_TOTO_LINKML.inTotoDocument__in_toto_statements, domain=None, range=Optional[Union[Union[dict, InTotoStatement], list[Union[dict, InTotoStatement]]]])

slots.inTotoDocument__in_toto_predicate_types = Slot(uri=IN_TOTO_LINKML.in_toto_predicate_types, name="inTotoDocument__in_toto_predicate_types", curie=IN_TOTO_LINKML.curie('in_toto_predicate_types'),
                   model_uri=IN_TOTO_LINKML.inTotoDocument__in_toto_predicate_types, domain=None, range=Optional[Union[Union[dict, InTotoPredicateType], list[Union[dict, InTotoPredicateType]]]])

slots.inTotoDigestSet__sha256 = Slot(uri=IN_TOTO_LINKML.sha256, name="inTotoDigestSet__sha256", curie=IN_TOTO_LINKML.curie('sha256'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__sha256, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.inTotoDigestSet__sha224 = Slot(uri=IN_TOTO_LINKML.sha224, name="inTotoDigestSet__sha224", curie=IN_TOTO_LINKML.curie('sha224'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__sha224, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{56}$'))

slots.inTotoDigestSet__sha384 = Slot(uri=IN_TOTO_LINKML.sha384, name="inTotoDigestSet__sha384", curie=IN_TOTO_LINKML.curie('sha384'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__sha384, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{96}$'))

slots.inTotoDigestSet__sha512 = Slot(uri=IN_TOTO_LINKML.sha512, name="inTotoDigestSet__sha512", curie=IN_TOTO_LINKML.curie('sha512'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__sha512, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{128}$'))

slots.inTotoDigestSet__sha512_224 = Slot(uri=IN_TOTO_LINKML.sha512_224, name="inTotoDigestSet__sha512_224", curie=IN_TOTO_LINKML.curie('sha512_224'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__sha512_224, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{56}$'))

slots.inTotoDigestSet__sha512_256 = Slot(uri=IN_TOTO_LINKML.sha512_256, name="inTotoDigestSet__sha512_256", curie=IN_TOTO_LINKML.curie('sha512_256'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__sha512_256, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.inTotoDigestSet__sha3_224 = Slot(uri=IN_TOTO_LINKML.sha3_224, name="inTotoDigestSet__sha3_224", curie=IN_TOTO_LINKML.curie('sha3_224'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__sha3_224, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{56}$'))

slots.inTotoDigestSet__sha3_256 = Slot(uri=IN_TOTO_LINKML.sha3_256, name="inTotoDigestSet__sha3_256", curie=IN_TOTO_LINKML.curie('sha3_256'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__sha3_256, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.inTotoDigestSet__sha3_384 = Slot(uri=IN_TOTO_LINKML.sha3_384, name="inTotoDigestSet__sha3_384", curie=IN_TOTO_LINKML.curie('sha3_384'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__sha3_384, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{96}$'))

slots.inTotoDigestSet__sha3_512 = Slot(uri=IN_TOTO_LINKML.sha3_512, name="inTotoDigestSet__sha3_512", curie=IN_TOTO_LINKML.curie('sha3_512'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__sha3_512, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{128}$'))

slots.inTotoDigestSet__shake128 = Slot(uri=IN_TOTO_LINKML.shake128, name="inTotoDigestSet__shake128", curie=IN_TOTO_LINKML.curie('shake128'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__shake128, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}([a-f0-9]{2})*$'))

slots.inTotoDigestSet__shake256 = Slot(uri=IN_TOTO_LINKML.shake256, name="inTotoDigestSet__shake256", curie=IN_TOTO_LINKML.curie('shake256'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__shake256, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}([a-f0-9]{2})*$'))

slots.inTotoDigestSet__blake2b = Slot(uri=IN_TOTO_LINKML.blake2b, name="inTotoDigestSet__blake2b", curie=IN_TOTO_LINKML.curie('blake2b'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__blake2b, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}([a-f0-9]{2}){0,32}$'))

slots.inTotoDigestSet__blake2s = Slot(uri=IN_TOTO_LINKML.blake2s, name="inTotoDigestSet__blake2s", curie=IN_TOTO_LINKML.curie('blake2s'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__blake2s, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.inTotoDigestSet__ripemd160 = Slot(uri=IN_TOTO_LINKML.ripemd160, name="inTotoDigestSet__ripemd160", curie=IN_TOTO_LINKML.curie('ripemd160'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__ripemd160, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{40}$'))

slots.inTotoDigestSet__sm3 = Slot(uri=IN_TOTO_LINKML.sm3, name="inTotoDigestSet__sm3", curie=IN_TOTO_LINKML.curie('sm3'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__sm3, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.inTotoDigestSet__gost = Slot(uri=IN_TOTO_LINKML.gost, name="inTotoDigestSet__gost", curie=IN_TOTO_LINKML.curie('gost'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__gost, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}([a-f0-9]{64})?$'))

slots.inTotoDigestSet__sha1 = Slot(uri=IN_TOTO_LINKML.sha1, name="inTotoDigestSet__sha1", curie=IN_TOTO_LINKML.curie('sha1'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__sha1, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{40}$'))

slots.inTotoDigestSet__md5 = Slot(uri=IN_TOTO_LINKML.md5, name="inTotoDigestSet__md5", curie=IN_TOTO_LINKML.curie('md5'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__md5, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{32}$'))

slots.inTotoDigestSet__dir_hash = Slot(uri=IN_TOTO_LINKML.dir_hash, name="inTotoDigestSet__dir_hash", curie=IN_TOTO_LINKML.curie('dir_hash'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__dir_hash, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.inTotoDigestSet__git_commit = Slot(uri=IN_TOTO_LINKML.git_commit, name="inTotoDigestSet__git_commit", curie=IN_TOTO_LINKML.curie('git_commit'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__git_commit, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{40}([a-f0-9]{24})?$'))

slots.inTotoDigestSet__git_tree = Slot(uri=IN_TOTO_LINKML.git_tree, name="inTotoDigestSet__git_tree", curie=IN_TOTO_LINKML.curie('git_tree'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__git_tree, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{40}([a-f0-9]{24})?$'))

slots.inTotoDigestSet__git_blob = Slot(uri=IN_TOTO_LINKML.git_blob, name="inTotoDigestSet__git_blob", curie=IN_TOTO_LINKML.curie('git_blob'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__git_blob, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{40}([a-f0-9]{24})?$'))

slots.inTotoDigestSet__git_tag = Slot(uri=IN_TOTO_LINKML.git_tag, name="inTotoDigestSet__git_tag", curie=IN_TOTO_LINKML.curie('git_tag'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__git_tag, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{40}([a-f0-9]{24})?$'))

slots.inTotoDigestSet__additional_digests = Slot(uri=IN_TOTO_LINKML.additional_digests, name="inTotoDigestSet__additional_digests", curie=IN_TOTO_LINKML.curie('additional_digests'),
                   model_uri=IN_TOTO_LINKML.inTotoDigestSet__additional_digests, domain=None, range=Optional[Union[Union[dict, InTotoAdditionalDigest], list[Union[dict, InTotoAdditionalDigest]]]])

slots.inTotoAdditionalDigest__algorithm = Slot(uri=SPDX.algorithm, name="inTotoAdditionalDigest__algorithm", curie=SPDX.curie('algorithm'),
                   model_uri=IN_TOTO_LINKML.inTotoAdditionalDigest__algorithm, domain=None, range=str,
                   pattern=re.compile(r'^[a-z][A-Za-z0-9_]*$'))

slots.inTotoAdditionalDigest__value = Slot(uri=IN_TOTO_LINKML.value, name="inTotoAdditionalDigest__value", curie=IN_TOTO_LINKML.curie('value'),
                   model_uri=IN_TOTO_LINKML.inTotoAdditionalDigest__value, domain=None, range=str,
                   pattern=re.compile(r'^\S+$'))

slots.inTotoAnnotation__annotation_key = Slot(uri=IN_TOTO_LINKML.annotation_key, name="inTotoAnnotation__annotation_key", curie=IN_TOTO_LINKML.curie('annotation_key'),
                   model_uri=IN_TOTO_LINKML.inTotoAnnotation__annotation_key, domain=None, range=str)

slots.inTotoAnnotation__annotation_values = Slot(uri=IN_TOTO_LINKML.annotation_values, name="inTotoAnnotation__annotation_values", curie=IN_TOTO_LINKML.curie('annotation_values'),
                   model_uri=IN_TOTO_LINKML.inTotoAnnotation__annotation_values, domain=None, range=Optional[Union[str, list[str]]])

slots.inTotoResourceDescriptor__resource_name = Slot(uri=IN_TOTO_LINKML.resource_name, name="inTotoResourceDescriptor__resource_name", curie=IN_TOTO_LINKML.curie('resource_name'),
                   model_uri=IN_TOTO_LINKML.inTotoResourceDescriptor__resource_name, domain=None, range=Optional[str])

slots.inTotoResourceDescriptor__download_location = Slot(uri=IN_TOTO_LINKML.download_location, name="inTotoResourceDescriptor__download_location", curie=IN_TOTO_LINKML.curie('download_location'),
                   model_uri=IN_TOTO_LINKML.inTotoResourceDescriptor__download_location, domain=None, range=Optional[Union[str, URI]])

slots.inTotoResourceDescriptor__media_type = Slot(uri=DCAT.mediaType, name="inTotoResourceDescriptor__media_type", curie=DCAT.curie('mediaType'),
                   model_uri=IN_TOTO_LINKML.inTotoResourceDescriptor__media_type, domain=None, range=Optional[str])

slots.inTotoResourceDescriptor__content = Slot(uri=IN_TOTO_LINKML.content, name="inTotoResourceDescriptor__content", curie=IN_TOTO_LINKML.curie('content'),
                   model_uri=IN_TOTO_LINKML.inTotoResourceDescriptor__content, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9+/_-]+={0,2}$'))

slots.inTotoResourceDescriptor__annotations = Slot(uri=IN_TOTO_LINKML.annotations, name="inTotoResourceDescriptor__annotations", curie=IN_TOTO_LINKML.curie('annotations'),
                   model_uri=IN_TOTO_LINKML.inTotoResourceDescriptor__annotations, domain=None, range=Optional[Union[Union[dict, InTotoAnnotation], list[Union[dict, InTotoAnnotation]]]])

slots.inTotoStatement__statement_type = Slot(uri=IN_TOTO_LINKML.statement_type, name="inTotoStatement__statement_type", curie=IN_TOTO_LINKML.curie('statement_type'),
                   model_uri=IN_TOTO_LINKML.inTotoStatement__statement_type, domain=None, range=Union[str, URI],
                   pattern=re.compile(r'^https://in-toto\.io/Statement/v1$'))

slots.inTotoStatement__subject = Slot(uri=IN_TOTO_LINKML.subject, name="inTotoStatement__subject", curie=IN_TOTO_LINKML.curie('subject'),
                   model_uri=IN_TOTO_LINKML.inTotoStatement__subject, domain=None, range=Union[Union[dict, InTotoStatementSubject], list[Union[dict, InTotoStatementSubject]]])

slots.inTotoStatement__predicate_type = Slot(uri=IN_TOTO_LINKML.predicate_type, name="inTotoStatement__predicate_type", curie=IN_TOTO_LINKML.curie('predicate_type'),
                   model_uri=IN_TOTO_LINKML.inTotoStatement__predicate_type, domain=None, range=Union[str, URI])

slots.inTotoStatement__statement_predicate = Slot(uri=IN_TOTO_LINKML.statement_predicate, name="inTotoStatement__statement_predicate", curie=IN_TOTO_LINKML.curie('statement_predicate'),
                   model_uri=IN_TOTO_LINKML.inTotoStatement__statement_predicate, domain=None, range=Optional[Union[dict, InTotoPredicate]])

slots.inTotoPredicate__predicate_kind = Slot(uri=IN_TOTO_LINKML.predicate_kind, name="inTotoPredicate__predicate_kind", curie=IN_TOTO_LINKML.curie('predicate_kind'),
                   model_uri=IN_TOTO_LINKML.inTotoPredicate__predicate_kind, domain=None, range=Optional[str])

slots.inTotoPredicateType__predicate_type_uri = Slot(uri=IN_TOTO_LINKML.predicate_type_uri, name="inTotoPredicateType__predicate_type_uri", curie=IN_TOTO_LINKML.curie('predicate_type_uri'),
                   model_uri=IN_TOTO_LINKML.inTotoPredicateType__predicate_type_uri, domain=None, range=Union[str, URI])

slots.inTotoPredicateType__predicate_version = Slot(uri=IN_TOTO_LINKML.predicate_version, name="inTotoPredicateType__predicate_version", curie=IN_TOTO_LINKML.curie('predicate_version'),
                   model_uri=IN_TOTO_LINKML.inTotoPredicateType__predicate_version, domain=None, range=Optional[str])

slots.inTotoPredicateType__predicate_specification = Slot(uri=IN_TOTO_LINKML.predicate_specification, name="inTotoPredicateType__predicate_specification", curie=IN_TOTO_LINKML.curie('predicate_specification'),
                   model_uri=IN_TOTO_LINKML.inTotoPredicateType__predicate_specification, domain=None, range=Optional[Union[str, URI]])

slots.inTotoPredicateType__vetted_as = Slot(uri=IN_TOTO_LINKML.vetted_as, name="inTotoPredicateType__vetted_as", curie=IN_TOTO_LINKML.curie('vetted_as'),
                   model_uri=IN_TOTO_LINKML.inTotoPredicateType__vetted_as, domain=None, range=Optional[Union[str, "InTotoVettedPredicate"]])

slots.inTotoObjectEntry__entry_key = Slot(uri=IN_TOTO_LINKML.entry_key, name="inTotoObjectEntry__entry_key", curie=IN_TOTO_LINKML.curie('entry_key'),
                   model_uri=IN_TOTO_LINKML.inTotoObjectEntry__entry_key, domain=None, range=str)

slots.inTotoObjectEntry__entry_values = Slot(uri=IN_TOTO_LINKML.entry_values, name="inTotoObjectEntry__entry_values", curie=IN_TOTO_LINKML.curie('entry_values'),
                   model_uri=IN_TOTO_LINKML.inTotoObjectEntry__entry_values, domain=None, range=Optional[Union[str, list[str]]])

slots.inTotoTestResult__test_result = Slot(uri=IN_TOTO_LINKML.test_result, name="inTotoTestResult__test_result", curie=IN_TOTO_LINKML.curie('test_result'),
                   model_uri=IN_TOTO_LINKML.inTotoTestResult__test_result, domain=None, range=Union[str, "InTotoTestResultValue"])

slots.inTotoTestResult__configuration = Slot(uri=IN_TOTO_LINKML.configuration, name="inTotoTestResult__configuration", curie=IN_TOTO_LINKML.curie('configuration'),
                   model_uri=IN_TOTO_LINKML.inTotoTestResult__configuration, domain=None, range=Union[Union[dict, InTotoResourceDescriptor], list[Union[dict, InTotoResourceDescriptor]]])

slots.inTotoTestResult__test_run_url = Slot(uri=IN_TOTO_LINKML.test_run_url, name="inTotoTestResult__test_run_url", curie=IN_TOTO_LINKML.curie('test_run_url'),
                   model_uri=IN_TOTO_LINKML.inTotoTestResult__test_run_url, domain=None, range=Optional[Union[str, URI]])

slots.inTotoTestResult__passed_tests = Slot(uri=IN_TOTO_LINKML.passed_tests, name="inTotoTestResult__passed_tests", curie=IN_TOTO_LINKML.curie('passed_tests'),
                   model_uri=IN_TOTO_LINKML.inTotoTestResult__passed_tests, domain=None, range=Optional[Union[str, list[str]]])

slots.inTotoTestResult__warned_tests = Slot(uri=IN_TOTO_LINKML.warned_tests, name="inTotoTestResult__warned_tests", curie=IN_TOTO_LINKML.curie('warned_tests'),
                   model_uri=IN_TOTO_LINKML.inTotoTestResult__warned_tests, domain=None, range=Optional[Union[str, list[str]]])

slots.inTotoTestResult__failed_tests = Slot(uri=IN_TOTO_LINKML.failed_tests, name="inTotoTestResult__failed_tests", curie=IN_TOTO_LINKML.curie('failed_tests'),
                   model_uri=IN_TOTO_LINKML.inTotoTestResult__failed_tests, domain=None, range=Optional[Union[str, list[str]]])

slots.inTotoSimpleVerificationResult__svr_verifier = Slot(uri=IN_TOTO_LINKML.svr_verifier, name="inTotoSimpleVerificationResult__svr_verifier", curie=IN_TOTO_LINKML.curie('svr_verifier'),
                   model_uri=IN_TOTO_LINKML.inTotoSimpleVerificationResult__svr_verifier, domain=None, range=Union[dict, InTotoSvrVerifier])

slots.inTotoSimpleVerificationResult__time_created = Slot(uri=IN_TOTO_LINKML.time_created, name="inTotoSimpleVerificationResult__time_created", curie=IN_TOTO_LINKML.curie('time_created'),
                   model_uri=IN_TOTO_LINKML.inTotoSimpleVerificationResult__time_created, domain=None, range=Union[str, InTotoTimestamp])

slots.inTotoSimpleVerificationResult__verified_properties = Slot(uri=IN_TOTO_LINKML.verified_properties, name="inTotoSimpleVerificationResult__verified_properties", curie=IN_TOTO_LINKML.curie('verified_properties'),
                   model_uri=IN_TOTO_LINKML.inTotoSimpleVerificationResult__verified_properties, domain=None, range=Union[str, list[str]])

slots.inTotoSvrVerifier__svr_verifier_id = Slot(uri=IN_TOTO_LINKML.svr_verifier_id, name="inTotoSvrVerifier__svr_verifier_id", curie=IN_TOTO_LINKML.curie('svr_verifier_id'),
                   model_uri=IN_TOTO_LINKML.inTotoSvrVerifier__svr_verifier_id, domain=None, range=Union[str, URI])

slots.inTotoScaiAttributeReport__scai_attributes = Slot(uri=IN_TOTO_LINKML.scai_attributes, name="inTotoScaiAttributeReport__scai_attributes", curie=IN_TOTO_LINKML.curie('scai_attributes'),
                   model_uri=IN_TOTO_LINKML.inTotoScaiAttributeReport__scai_attributes, domain=None, range=Union[Union[dict, InTotoScaiAttributeAssertion], list[Union[dict, InTotoScaiAttributeAssertion]]])

slots.inTotoScaiAttributeReport__scai_producer = Slot(uri=IN_TOTO_LINKML.scai_producer, name="inTotoScaiAttributeReport__scai_producer", curie=IN_TOTO_LINKML.curie('scai_producer'),
                   model_uri=IN_TOTO_LINKML.inTotoScaiAttributeReport__scai_producer, domain=None, range=Optional[Union[dict, InTotoResourceDescriptor]])

slots.inTotoScaiAttributeAssertion__scai_attribute = Slot(uri=IN_TOTO_LINKML.scai_attribute, name="inTotoScaiAttributeAssertion__scai_attribute", curie=IN_TOTO_LINKML.curie('scai_attribute'),
                   model_uri=IN_TOTO_LINKML.inTotoScaiAttributeAssertion__scai_attribute, domain=None, range=str)

slots.inTotoScaiAttributeAssertion__scai_target = Slot(uri=IN_TOTO_LINKML.scai_target, name="inTotoScaiAttributeAssertion__scai_target", curie=IN_TOTO_LINKML.curie('scai_target'),
                   model_uri=IN_TOTO_LINKML.inTotoScaiAttributeAssertion__scai_target, domain=None, range=Optional[Union[dict, InTotoResourceDescriptor]])

slots.inTotoScaiAttributeAssertion__scai_conditions = Slot(uri=IN_TOTO_LINKML.scai_conditions, name="inTotoScaiAttributeAssertion__scai_conditions", curie=IN_TOTO_LINKML.curie('scai_conditions'),
                   model_uri=IN_TOTO_LINKML.inTotoScaiAttributeAssertion__scai_conditions, domain=None, range=Optional[Union[Union[dict, InTotoObjectEntry], list[Union[dict, InTotoObjectEntry]]]])

slots.inTotoScaiAttributeAssertion__scai_evidence = Slot(uri=IN_TOTO_LINKML.scai_evidence, name="inTotoScaiAttributeAssertion__scai_evidence", curie=IN_TOTO_LINKML.curie('scai_evidence'),
                   model_uri=IN_TOTO_LINKML.inTotoScaiAttributeAssertion__scai_evidence, domain=None, range=Optional[Union[dict, InTotoResourceDescriptor]])

slots.inTotoLink__step_name = Slot(uri=IN_TOTO_LINKML.step_name, name="inTotoLink__step_name", curie=IN_TOTO_LINKML.curie('step_name'),
                   model_uri=IN_TOTO_LINKML.inTotoLink__step_name, domain=None, range=str)

slots.inTotoLink__step_command = Slot(uri=IN_TOTO_LINKML.step_command, name="inTotoLink__step_command", curie=IN_TOTO_LINKML.curie('step_command'),
                   model_uri=IN_TOTO_LINKML.inTotoLink__step_command, domain=None, range=Optional[Union[str, list[str]]])

slots.inTotoLink__materials = Slot(uri=IN_TOTO_LINKML.materials, name="inTotoLink__materials", curie=IN_TOTO_LINKML.curie('materials'),
                   model_uri=IN_TOTO_LINKML.inTotoLink__materials, domain=None, range=Optional[Union[Union[dict, InTotoLinkMaterial], list[Union[dict, InTotoLinkMaterial]]]])

slots.inTotoLink__step_byproducts = Slot(uri=IN_TOTO_LINKML.step_byproducts, name="inTotoLink__step_byproducts", curie=IN_TOTO_LINKML.curie('step_byproducts'),
                   model_uri=IN_TOTO_LINKML.inTotoLink__step_byproducts, domain=None, range=Optional[Union[Union[dict, InTotoObjectEntry], list[Union[dict, InTotoObjectEntry]]]])

slots.inTotoLink__step_environment = Slot(uri=IN_TOTO_LINKML.step_environment, name="inTotoLink__step_environment", curie=IN_TOTO_LINKML.curie('step_environment'),
                   model_uri=IN_TOTO_LINKML.inTotoLink__step_environment, domain=None, range=Optional[Union[Union[dict, InTotoObjectEntry], list[Union[dict, InTotoObjectEntry]]]])

slots.inTotoReference__reference_attester = Slot(uri=IN_TOTO_LINKML.reference_attester, name="inTotoReference__reference_attester", curie=IN_TOTO_LINKML.curie('reference_attester'),
                   model_uri=IN_TOTO_LINKML.inTotoReference__reference_attester, domain=None, range=Union[dict, InTotoReferenceAttester])

slots.inTotoReference__referenced_documents = Slot(uri=IN_TOTO_LINKML.referenced_documents, name="inTotoReference__referenced_documents", curie=IN_TOTO_LINKML.curie('referenced_documents'),
                   model_uri=IN_TOTO_LINKML.inTotoReference__referenced_documents, domain=None, range=Union[Union[dict, InTotoReferencedDocument], list[Union[dict, InTotoReferencedDocument]]])

slots.inTotoReferenceAttester__reference_attester_id = Slot(uri=IN_TOTO_LINKML.reference_attester_id, name="inTotoReferenceAttester__reference_attester_id", curie=IN_TOTO_LINKML.curie('reference_attester_id'),
                   model_uri=IN_TOTO_LINKML.inTotoReferenceAttester__reference_attester_id, domain=None, range=Union[str, URI])

slots.inTotoRelease__release_purl = Slot(uri=IN_TOTO_LINKML.release_purl, name="inTotoRelease__release_purl", curie=IN_TOTO_LINKML.curie('release_purl'),
                   model_uri=IN_TOTO_LINKML.inTotoRelease__release_purl, domain=None, range=Union[str, URI],
                   pattern=re.compile(r'^pkg:[A-Za-z.+-]+/[^@?#]+@[^?#]+'))

slots.inTotoRelease__package_id = Slot(uri=IN_TOTO_LINKML.package_id, name="inTotoRelease__package_id", curie=IN_TOTO_LINKML.curie('package_id'),
                   model_uri=IN_TOTO_LINKML.inTotoRelease__package_id, domain=None, range=Optional[str])

slots.inTotoRuntimeTrace__trace_monitor = Slot(uri=IN_TOTO_LINKML.trace_monitor, name="inTotoRuntimeTrace__trace_monitor", curie=IN_TOTO_LINKML.curie('trace_monitor'),
                   model_uri=IN_TOTO_LINKML.inTotoRuntimeTrace__trace_monitor, domain=None, range=Union[dict, InTotoTraceMonitor])

slots.inTotoRuntimeTrace__monitored_process = Slot(uri=IN_TOTO_LINKML.monitored_process, name="inTotoRuntimeTrace__monitored_process", curie=IN_TOTO_LINKML.curie('monitored_process'),
                   model_uri=IN_TOTO_LINKML.inTotoRuntimeTrace__monitored_process, domain=None, range=Union[dict, InTotoMonitoredProcess])

slots.inTotoRuntimeTrace__monitor_log = Slot(uri=IN_TOTO_LINKML.monitor_log, name="inTotoRuntimeTrace__monitor_log", curie=IN_TOTO_LINKML.curie('monitor_log'),
                   model_uri=IN_TOTO_LINKML.inTotoRuntimeTrace__monitor_log, domain=None, range=Union[dict, InTotoMonitorLog])

slots.inTotoRuntimeTrace__trace_metadata = Slot(uri=IN_TOTO_LINKML.trace_metadata, name="inTotoRuntimeTrace__trace_metadata", curie=IN_TOTO_LINKML.curie('trace_metadata'),
                   model_uri=IN_TOTO_LINKML.inTotoRuntimeTrace__trace_metadata, domain=None, range=Optional[Union[dict, InTotoTraceMetadata]])

slots.inTotoTraceMonitor__monitor_type = Slot(uri=IN_TOTO_LINKML.monitor_type, name="inTotoTraceMonitor__monitor_type", curie=IN_TOTO_LINKML.curie('monitor_type'),
                   model_uri=IN_TOTO_LINKML.inTotoTraceMonitor__monitor_type, domain=None, range=Union[str, URI])

slots.inTotoTraceMonitor__monitor_config_source = Slot(uri=IN_TOTO_LINKML.monitor_config_source, name="inTotoTraceMonitor__monitor_config_source", curie=IN_TOTO_LINKML.curie('monitor_config_source'),
                   model_uri=IN_TOTO_LINKML.inTotoTraceMonitor__monitor_config_source, domain=None, range=Optional[Union[dict, InTotoResourceDescriptor]])

slots.inTotoTraceMonitor__trace_policy = Slot(uri=IN_TOTO_LINKML.trace_policy, name="inTotoTraceMonitor__trace_policy", curie=IN_TOTO_LINKML.curie('trace_policy'),
                   model_uri=IN_TOTO_LINKML.inTotoTraceMonitor__trace_policy, domain=None, range=Optional[Union[Union[dict, InTotoObjectEntry], list[Union[dict, InTotoObjectEntry]]]])

slots.inTotoMonitoredProcess__host_id = Slot(uri=IN_TOTO_LINKML.host_id, name="inTotoMonitoredProcess__host_id", curie=IN_TOTO_LINKML.curie('host_id'),
                   model_uri=IN_TOTO_LINKML.inTotoMonitoredProcess__host_id, domain=None, range=Union[str, URI])

slots.inTotoMonitoredProcess__process_type = Slot(uri=IN_TOTO_LINKML.process_type, name="inTotoMonitoredProcess__process_type", curie=IN_TOTO_LINKML.curie('process_type'),
                   model_uri=IN_TOTO_LINKML.inTotoMonitoredProcess__process_type, domain=None, range=Union[str, URI])

slots.inTotoMonitoredProcess__process_event = Slot(uri=IN_TOTO_LINKML.process_event, name="inTotoMonitoredProcess__process_event", curie=IN_TOTO_LINKML.curie('process_event'),
                   model_uri=IN_TOTO_LINKML.inTotoMonitoredProcess__process_event, domain=None, range=str)

slots.inTotoMonitorLog__traced_processes = Slot(uri=IN_TOTO_LINKML.traced_processes, name="inTotoMonitorLog__traced_processes", curie=IN_TOTO_LINKML.curie('traced_processes'),
                   model_uri=IN_TOTO_LINKML.inTotoMonitorLog__traced_processes, domain=None, range=Optional[Union[str, list[str]]])

slots.inTotoMonitorLog__traced_network = Slot(uri=IN_TOTO_LINKML.traced_network, name="inTotoMonitorLog__traced_network", curie=IN_TOTO_LINKML.curie('traced_network'),
                   model_uri=IN_TOTO_LINKML.inTotoMonitorLog__traced_network, domain=None, range=Optional[Union[str, list[str]]])

slots.inTotoMonitorLog__file_access = Slot(uri=IN_TOTO_LINKML.file_access, name="inTotoMonitorLog__file_access", curie=IN_TOTO_LINKML.curie('file_access'),
                   model_uri=IN_TOTO_LINKML.inTotoMonitorLog__file_access, domain=None, range=Optional[Union[Union[dict, InTotoResourceDescriptor], list[Union[dict, InTotoResourceDescriptor]]]])

slots.inTotoTraceMetadata__build_started_on = Slot(uri=IN_TOTO_LINKML.build_started_on, name="inTotoTraceMetadata__build_started_on", curie=IN_TOTO_LINKML.curie('build_started_on'),
                   model_uri=IN_TOTO_LINKML.inTotoTraceMetadata__build_started_on, domain=None, range=Optional[Union[str, InTotoTimestamp]])

slots.inTotoTraceMetadata__build_finished_on = Slot(uri=IN_TOTO_LINKML.build_finished_on, name="inTotoTraceMetadata__build_finished_on", curie=IN_TOTO_LINKML.curie('build_finished_on'),
                   model_uri=IN_TOTO_LINKML.inTotoTraceMetadata__build_finished_on, domain=None, range=Optional[Union[str, InTotoTimestamp]])

slots.inTotoVulns__vuln_scanner = Slot(uri=IN_TOTO_LINKML.vuln_scanner, name="inTotoVulns__vuln_scanner", curie=IN_TOTO_LINKML.curie('vuln_scanner'),
                   model_uri=IN_TOTO_LINKML.inTotoVulns__vuln_scanner, domain=None, range=Union[dict, InTotoVulnScanner])

slots.inTotoVulns__scan_metadata = Slot(uri=IN_TOTO_LINKML.scan_metadata, name="inTotoVulns__scan_metadata", curie=IN_TOTO_LINKML.curie('scan_metadata'),
                   model_uri=IN_TOTO_LINKML.inTotoVulns__scan_metadata, domain=None, range=Union[dict, InTotoScanMetadata])

slots.inTotoVulnScanner__scanner_uri = Slot(uri=IN_TOTO_LINKML.scanner_uri, name="inTotoVulnScanner__scanner_uri", curie=IN_TOTO_LINKML.curie('scanner_uri'),
                   model_uri=IN_TOTO_LINKML.inTotoVulnScanner__scanner_uri, domain=None, range=Union[str, URI])

slots.inTotoVulnScanner__scanner_version = Slot(uri=IN_TOTO_LINKML.scanner_version, name="inTotoVulnScanner__scanner_version", curie=IN_TOTO_LINKML.curie('scanner_version'),
                   model_uri=IN_TOTO_LINKML.inTotoVulnScanner__scanner_version, domain=None, range=Optional[str])

slots.inTotoVulnScanner__vuln_db = Slot(uri=IN_TOTO_LINKML.vuln_db, name="inTotoVulnScanner__vuln_db", curie=IN_TOTO_LINKML.curie('vuln_db'),
                   model_uri=IN_TOTO_LINKML.inTotoVulnScanner__vuln_db, domain=None, range=Optional[Union[dict, InTotoVulnDatabase]])

slots.inTotoVulnScanner__scan_results = Slot(uri=IN_TOTO_LINKML.scan_results, name="inTotoVulnScanner__scan_results", curie=IN_TOTO_LINKML.curie('scan_results'),
                   model_uri=IN_TOTO_LINKML.inTotoVulnScanner__scan_results, domain=None, range=Union[Union[dict, InTotoVulnResult], list[Union[dict, InTotoVulnResult]]])

slots.inTotoVulnDatabase__db_uri = Slot(uri=IN_TOTO_LINKML.db_uri, name="inTotoVulnDatabase__db_uri", curie=IN_TOTO_LINKML.curie('db_uri'),
                   model_uri=IN_TOTO_LINKML.inTotoVulnDatabase__db_uri, domain=None, range=Optional[Union[str, URI]])

slots.inTotoVulnDatabase__db_version = Slot(uri=IN_TOTO_LINKML.db_version, name="inTotoVulnDatabase__db_version", curie=IN_TOTO_LINKML.curie('db_version'),
                   model_uri=IN_TOTO_LINKML.inTotoVulnDatabase__db_version, domain=None, range=Optional[str])

slots.inTotoVulnDatabase__db_last_update = Slot(uri=IN_TOTO_LINKML.db_last_update, name="inTotoVulnDatabase__db_last_update", curie=IN_TOTO_LINKML.curie('db_last_update'),
                   model_uri=IN_TOTO_LINKML.inTotoVulnDatabase__db_last_update, domain=None, range=Union[str, InTotoTimestamp])

slots.inTotoVulnResult__vuln_id = Slot(uri=IN_TOTO_LINKML.vuln_id, name="inTotoVulnResult__vuln_id", curie=IN_TOTO_LINKML.curie('vuln_id'),
                   model_uri=IN_TOTO_LINKML.inTotoVulnResult__vuln_id, domain=None, range=str)

slots.inTotoVulnResult__vuln_severity = Slot(uri=IN_TOTO_LINKML.vuln_severity, name="inTotoVulnResult__vuln_severity", curie=IN_TOTO_LINKML.curie('vuln_severity'),
                   model_uri=IN_TOTO_LINKML.inTotoVulnResult__vuln_severity, domain=None, range=Union[Union[dict, InTotoVulnSeverity], list[Union[dict, InTotoVulnSeverity]]])

slots.inTotoVulnResult__vuln_annotations = Slot(uri=IN_TOTO_LINKML.vuln_annotations, name="inTotoVulnResult__vuln_annotations", curie=IN_TOTO_LINKML.curie('vuln_annotations'),
                   model_uri=IN_TOTO_LINKML.inTotoVulnResult__vuln_annotations, domain=None, range=Optional[Union[Union[dict, InTotoObjectEntry], list[Union[dict, InTotoObjectEntry]]]])

slots.inTotoVulnSeverity__severity_method = Slot(uri=IN_TOTO_LINKML.severity_method, name="inTotoVulnSeverity__severity_method", curie=IN_TOTO_LINKML.curie('severity_method'),
                   model_uri=IN_TOTO_LINKML.inTotoVulnSeverity__severity_method, domain=None, range=str)

slots.inTotoVulnSeverity__severity_score = Slot(uri=IN_TOTO_LINKML.severity_score, name="inTotoVulnSeverity__severity_score", curie=IN_TOTO_LINKML.curie('severity_score'),
                   model_uri=IN_TOTO_LINKML.inTotoVulnSeverity__severity_score, domain=None, range=str)

slots.inTotoScanMetadata__scan_started_on = Slot(uri=IN_TOTO_LINKML.scan_started_on, name="inTotoScanMetadata__scan_started_on", curie=IN_TOTO_LINKML.curie('scan_started_on'),
                   model_uri=IN_TOTO_LINKML.inTotoScanMetadata__scan_started_on, domain=None, range=Union[str, InTotoTimestamp])

slots.inTotoScanMetadata__scan_finished_on = Slot(uri=IN_TOTO_LINKML.scan_finished_on, name="inTotoScanMetadata__scan_finished_on", curie=IN_TOTO_LINKML.curie('scan_finished_on'),
                   model_uri=IN_TOTO_LINKML.inTotoScanMetadata__scan_finished_on, domain=None, range=Union[str, InTotoTimestamp])

slots.InTotoStatementSubject_digest = Slot(uri=IN_TOTO_LINKML.digest, name="InTotoStatementSubject_digest", curie=IN_TOTO_LINKML.curie('digest'),
                   model_uri=IN_TOTO_LINKML.InTotoStatementSubject_digest, domain=InTotoStatementSubject, range=Union[dict, InTotoDigestSet])

slots.InTotoLinkMaterial_digest = Slot(uri=IN_TOTO_LINKML.digest, name="InTotoLinkMaterial_digest", curie=IN_TOTO_LINKML.curie('digest'),
                   model_uri=IN_TOTO_LINKML.InTotoLinkMaterial_digest, domain=InTotoLinkMaterial, range=Union[dict, InTotoDigestSet])
