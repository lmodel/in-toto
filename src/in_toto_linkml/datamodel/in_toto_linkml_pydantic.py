from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "1.2.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'attestation_commit': {'tag': 'attestation_commit',
                                            'value': 'df02077bf97218a8860a5c534eff1f1381f56984'},
                     'attestation_tag': {'tag': 'attestation_tag',
                                         'value': 'v1.2.0'}},
     'comments': ['The version is the release of in-toto/attestation the model '
                  'renders, and the specification pages and protocol buffer '
                  'definitions of that release are copied to '
                  'src/in_toto_linkml/schema/attestation/ at the tag and commit in '
                  "the annotations. The release tags are the schema's own "
                  'versions, and scripts/check_upstream_release.py reads the same '
                  'pins and reports when the in-toto project releases again or the '
                  'copy drifts.',
                  'in_toto_core imports only the LinkML types, in_toto_predicates '
                  'imports the core, and this file adds only the document root, so '
                  'an importer can take one module. lmodel/slsa imports the core '
                  "and models SLSA's own predicates."],
     'default_prefix': 'in_toto_linkml',
     'default_range': 'string',
     'description': 'A LinkML model of the in-toto Attestation Framework: the '
                    'statement that binds an attestation to its subjects, the '
                    'resource descriptor and digest set that identify an artifact, '
                    'the predicate types the in-toto project has vetted, and the '
                    'vetted predicates that no other lmodel schema models.',
     'id': 'https://w3id.org/lmodel/in-toto',
     'imports': ['linkml:types', './in_toto_core', './in_toto_predicates'],
     'license': 'Apache-2.0',
     'name': 'in_toto_linkml',
     'prefixes': {'in_toto_linkml': {'prefix_prefix': 'in_toto_linkml',
                                     'prefix_reference': 'https://w3id.org/lmodel/in-toto/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'see_also': ['https://lmodel.github.io/in-toto',
                  'https://github.com/in-toto/attestation/blob/v1.2.0/spec/README.md',
                  'https://in-toto.io/'],
     'source': 'https://github.com/in-toto/attestation/tree/v1.2.0',
     'source_file': 'src/in_toto_linkml/schema/in_toto_linkml.yaml',
     'title': 'in-toto Attestation Framework'} )

class InTotoTestResultValue(str, Enum):
    """
    The result of a test run, as a Test Result predicate records it.
    """
    PASSED = "PASSED"
    """
    The run passed.
    """
    WARNED = "WARNED"
    """
    The run passed with warnings.
    """
    FAILED = "FAILED"
    """
    The run failed.
    """


class InTotoVettedPredicate(str, Enum):
    """
    The thirteen predicate types the in-toto project lists as vetted at release v1.2.0, each with the predicate_type a statement of it carries at the version its page describes.
    """
    CYCLONEDX = "CYCLONEDX"
    """
    A CycloneDX bill of materials for software artifacts.
    """
    LINK = "LINK"
    """
    One step of an in-toto layout, for migration from in-toto 0.9.
    """
    REFERENCE = "REFERENCE"
    """
    References to documents relevant to a resource.
    """
    RELEASE = "RELEASE"
    """
    An artifact that is part of a given release version.
    """
    RUNTIME_TRACE = "RUNTIME_TRACE"
    """
    Runtime traces of software supply chain operations.
    """
    SCAI = "SCAI"
    """
    Evidence-based assertions about software artifact and supply chain attributes or behaviour.
    """
    SLSA_PROVENANCE = "SLSA_PROVENANCE"
    """
    How an artifact or set of artifacts was produced; lmodel/slsa models it.
    """
    SLSA_VERIFICATION_SUMMARY = "SLSA_VERIFICATION_SUMMARY"
    """
    A SLSA verification decision about a software artifact; lmodel/slsa models it.
    """
    SPDX2 = "SPDX2"
    """
    An SPDX 2 bill of materials for software artifacts.
    """
    SPDX3 = "SPDX3"
    """
    An SPDX 3 bill of materials for software artifacts.
    """
    SIMPLE_VERIFICATION_RESULT = "SIMPLE_VERIFICATION_RESULT"
    """
    Evidence that an artifact was evaluated against one or more policies.
    """
    TEST_RESULT = "TEST_RESULT"
    """
    The results of any type of test.
    """
    VULNS = "VULNS"
    """
    The results of a vulnerability scan of software artifacts.
    """



class InTotoDigestSet(ConfiguredBaseModel):
    """
    A set of one or more digests over one artifact, keyed by algorithm, from which a consumer picks the algorithm it trusts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'slot_conditions': {'sha256': {'any_of': [{'range': 'string'}],
                                                    'name': 'sha256',
                                                    'required': True}}},
                    {'slot_conditions': {'sha224': {'any_of': [{'range': 'string'}],
                                                    'name': 'sha224',
                                                    'required': True}}},
                    {'slot_conditions': {'sha384': {'any_of': [{'range': 'string'}],
                                                    'name': 'sha384',
                                                    'required': True}}},
                    {'slot_conditions': {'sha512': {'any_of': [{'range': 'string'}],
                                                    'name': 'sha512',
                                                    'required': True}}},
                    {'slot_conditions': {'sha512_224': {'any_of': [{'range': 'string'}],
                                                        'name': 'sha512_224',
                                                        'required': True}}},
                    {'slot_conditions': {'sha512_256': {'any_of': [{'range': 'string'}],
                                                        'name': 'sha512_256',
                                                        'required': True}}},
                    {'slot_conditions': {'sha3_224': {'any_of': [{'range': 'string'}],
                                                      'name': 'sha3_224',
                                                      'required': True}}},
                    {'slot_conditions': {'sha3_256': {'any_of': [{'range': 'string'}],
                                                      'name': 'sha3_256',
                                                      'required': True}}},
                    {'slot_conditions': {'sha3_384': {'any_of': [{'range': 'string'}],
                                                      'name': 'sha3_384',
                                                      'required': True}}},
                    {'slot_conditions': {'sha3_512': {'any_of': [{'range': 'string'}],
                                                      'name': 'sha3_512',
                                                      'required': True}}},
                    {'slot_conditions': {'shake128': {'any_of': [{'range': 'string'}],
                                                      'name': 'shake128',
                                                      'required': True}}},
                    {'slot_conditions': {'shake256': {'any_of': [{'range': 'string'}],
                                                      'name': 'shake256',
                                                      'required': True}}},
                    {'slot_conditions': {'blake2b': {'any_of': [{'range': 'string'}],
                                                     'name': 'blake2b',
                                                     'required': True}}},
                    {'slot_conditions': {'blake2s': {'any_of': [{'range': 'string'}],
                                                     'name': 'blake2s',
                                                     'required': True}}},
                    {'slot_conditions': {'ripemd160': {'any_of': [{'range': 'string'}],
                                                       'name': 'ripemd160',
                                                       'required': True}}},
                    {'slot_conditions': {'sm3': {'any_of': [{'range': 'string'}],
                                                 'name': 'sm3',
                                                 'required': True}}},
                    {'slot_conditions': {'gost': {'any_of': [{'range': 'string'}],
                                                  'name': 'gost',
                                                  'required': True}}},
                    {'slot_conditions': {'sha1': {'any_of': [{'range': 'string'}],
                                                  'name': 'sha1',
                                                  'required': True}}},
                    {'slot_conditions': {'md5': {'any_of': [{'range': 'string'}],
                                                 'name': 'md5',
                                                 'required': True}}},
                    {'slot_conditions': {'dir_hash': {'any_of': [{'range': 'string'}],
                                                      'name': 'dir_hash',
                                                      'required': True}}},
                    {'slot_conditions': {'git_commit': {'any_of': [{'range': 'string'}],
                                                        'name': 'git_commit',
                                                        'required': True}}},
                    {'slot_conditions': {'git_tree': {'any_of': [{'range': 'string'}],
                                                      'name': 'git_tree',
                                                      'required': True}}},
                    {'slot_conditions': {'git_blob': {'any_of': [{'range': 'string'}],
                                                      'name': 'git_blob',
                                                      'required': True}}},
                    {'slot_conditions': {'git_tag': {'any_of': [{'range': 'string'}],
                                                     'name': 'git_tag',
                                                     'required': True}}},
                    {'slot_conditions': {'additional_digests': {'multivalued': True,
                                                                'name': 'additional_digests',
                                                                'required': True}}}],
         'comments': ['The named algorithms take lowercase hexadecimal, and '
                      "additional_digests holds any other algorithm, such as an SCS's "
                      'own revision type.',
                      'A consumer accepts only the algorithms it considers secure and '
                      'ignores the rest, and two sets match when any accepted '
                      'algorithm matches.',
                      'SHAKE and BLAKE2 digests can be of any length, and this schema '
                      'asks for at least 32 bytes, since a shorter digest resists '
                      'collisions too weakly to identify an artifact.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core',
         'notes': ['Each condition in any_of names its range through a nested any_of, '
                   "because the JSON Schema generator leaves a condition's own range "
                   'out, and a null value would then count as present.'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md']})

    sha256: Optional[str] = Field(default=None, description="""The SHA-256 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    sha224: Optional[str] = Field(default=None, description="""The SHA-224 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    sha384: Optional[str] = Field(default=None, description="""The SHA-384 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    sha512: Optional[str] = Field(default=None, description="""The SHA-512 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    sha512_224: Optional[str] = Field(default=None, description="""The SHA-512/224 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    sha512_256: Optional[str] = Field(default=None, description="""The SHA-512/256 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    sha3_224: Optional[str] = Field(default=None, description="""The SHA3-224 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    sha3_256: Optional[str] = Field(default=None, description="""The SHA3-256 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    sha3_384: Optional[str] = Field(default=None, description="""The SHA3-384 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    sha3_512: Optional[str] = Field(default=None, description="""The SHA3-512 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    shake128: Optional[str] = Field(default=None, description="""The SHAKE128 digest of the artifact, of at least 32 bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    shake256: Optional[str] = Field(default=None, description="""The SHAKE256 digest of the artifact, of at least 32 bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    blake2b: Optional[str] = Field(default=None, description="""The BLAKE2b digest of the artifact, of 32 to 64 bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    blake2s: Optional[str] = Field(default=None, description="""The BLAKE2s digest of the artifact, at its full 32 bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    ripemd160: Optional[str] = Field(default=None, description="""The RIPEMD-160 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    sm3: Optional[str] = Field(default=None, description="""The SM3 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    gost: Optional[str] = Field(default=None, description="""The GOST R 34.11 digest of the artifact, of 256 or 512 bits.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    sha1: Optional[str] = Field(default=None, description="""The SHA-1 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'comments': ['SHA-1 lacks collision resistance, so most consumers should not '
                      'rely on it.'],
         'domain_of': ['InTotoDigestSet']} })
    md5: Optional[str] = Field(default=None, description="""The MD5 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'comments': ['MD5 lacks collision resistance, so most consumers should not '
                      'accept it.'],
         'domain_of': ['InTotoDigestSet']} })
    dir_hash: Optional[str] = Field(default=None, description="""A digest over a directory's content by the dirhash Hash1 function, in lowercase hexadecimal rather than base64.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    git_commit: Optional[str] = Field(default=None, description="""The git commit id of a source revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    git_tree: Optional[str] = Field(default=None, description="""The git tree id of a source revision's content, or of any file tree.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    git_blob: Optional[str] = Field(default=None, description="""The git blob id of a file's content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    git_tag: Optional[str] = Field(default=None, description="""The git object id of an annotated tag.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    additional_digests: Optional[list[InTotoAdditionalDigest]] = Field(default=None, description="""The digests under algorithms this class does not name.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })

    @field_validator('sha256')
    def pattern_sha256(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha256 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha256 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha224')
    def pattern_sha224(cls, v):
        pattern=re.compile(r"^[a-f0-9]{56}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha224 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha224 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha384')
    def pattern_sha384(cls, v):
        pattern=re.compile(r"^[a-f0-9]{96}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha384 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha384 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha512')
    def pattern_sha512(cls, v):
        pattern=re.compile(r"^[a-f0-9]{128}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha512 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha512 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha512_224')
    def pattern_sha512_224(cls, v):
        pattern=re.compile(r"^[a-f0-9]{56}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha512_224 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha512_224 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha512_256')
    def pattern_sha512_256(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha512_256 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha512_256 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha3_224')
    def pattern_sha3_224(cls, v):
        pattern=re.compile(r"^[a-f0-9]{56}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha3_224 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha3_224 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha3_256')
    def pattern_sha3_256(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha3_256 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha3_256 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha3_384')
    def pattern_sha3_384(cls, v):
        pattern=re.compile(r"^[a-f0-9]{96}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha3_384 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha3_384 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha3_512')
    def pattern_sha3_512(cls, v):
        pattern=re.compile(r"^[a-f0-9]{128}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha3_512 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha3_512 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('shake128')
    def pattern_shake128(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}([a-f0-9]{2})*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid shake128 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid shake128 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('shake256')
    def pattern_shake256(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}([a-f0-9]{2})*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid shake256 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid shake256 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('blake2b')
    def pattern_blake2b(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}([a-f0-9]{2}){0,32}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid blake2b format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid blake2b format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('blake2s')
    def pattern_blake2s(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid blake2s format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid blake2s format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('ripemd160')
    def pattern_ripemd160(cls, v):
        pattern=re.compile(r"^[a-f0-9]{40}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid ripemd160 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid ripemd160 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sm3')
    def pattern_sm3(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sm3 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sm3 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('gost')
    def pattern_gost(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}([a-f0-9]{64})?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gost format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gost format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha1')
    def pattern_sha1(cls, v):
        pattern=re.compile(r"^[a-f0-9]{40}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha1 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha1 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('md5')
    def pattern_md5(cls, v):
        pattern=re.compile(r"^[a-f0-9]{32}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid md5 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid md5 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('dir_hash')
    def pattern_dir_hash(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid dir_hash format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid dir_hash format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('git_commit')
    def pattern_git_commit(cls, v):
        pattern=re.compile(r"^[a-f0-9]{40}([a-f0-9]{24})?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid git_commit format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid git_commit format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('git_tree')
    def pattern_git_tree(cls, v):
        pattern=re.compile(r"^[a-f0-9]{40}([a-f0-9]{24})?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid git_tree format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid git_tree format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('git_blob')
    def pattern_git_blob(cls, v):
        pattern=re.compile(r"^[a-f0-9]{40}([a-f0-9]{24})?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid git_blob format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid git_blob format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('git_tag')
    def pattern_git_tag(cls, v):
        pattern=re.compile(r"^[a-f0-9]{40}([a-f0-9]{24})?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid git_tag format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid git_tag format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoAdditionalDigest(ConfiguredBaseModel):
    """
    One digest under an algorithm that InTotoDigestSet does not name, such as an SCS's own revision type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["In the attestation's JSON the algorithm is a key of the digest "
                      'set beside the named ones, and an algorithm the framework does '
                      'not define documents how its value is encoded.',
                      'An SCS that does not use cryptographic digests defines a '
                      'canonical revision type of its own that includes the '
                      'repository, such as svn_revision_id.',
                      "Each algorithm appears once in a list, since the attestation's "
                      'JSON uses it as a key; the validator does not check this.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md']})

    algorithm: str = Field(default=..., description="""The algorithm's name, as the key the attestation's JSON uses, such as svn_revision_id.""", json_schema_extra = { "linkml_meta": {'comments': ['An algorithm that InTotoDigestSet names, by its JSON key or by '
                      'its field name, goes in that field instead.'],
         'domain_of': ['InTotoAdditionalDigest'],
         'none_of': [{'equals_string_in': ['sha256',
                                           'sha224',
                                           'sha384',
                                           'sha512',
                                           'sha512_224',
                                           'sha512_256',
                                           'sha3_224',
                                           'sha3_256',
                                           'sha3_384',
                                           'sha3_512',
                                           'shake128',
                                           'shake256',
                                           'blake2b',
                                           'blake2s',
                                           'ripemd160',
                                           'sm3',
                                           'gost',
                                           'sha1',
                                           'md5',
                                           'dirHash',
                                           'gitCommit',
                                           'gitTree',
                                           'gitBlob',
                                           'gitTag',
                                           'dir_hash',
                                           'git_commit',
                                           'git_tree',
                                           'git_blob',
                                           'git_tag']}],
         'slot_uri': 'spdx:algorithm'} })
    value: str = Field(default=..., description="""The digest under that algorithm, in the encoding the algorithm documents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoAdditionalDigest']} })

    @field_validator('algorithm')
    def pattern_algorithm(cls, v):
        pattern=re.compile(r"^[a-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid algorithm format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid algorithm format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid value format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid value format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoAnnotation(ConfiguredBaseModel):
    """
    One vendor-specific annotation on a resource descriptor: a key and its values.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["The attestation's JSON allows any JSON value. A string becomes "
                      'one value and an array one value per item; any other value or '
                      'item is written as its JSON text, so one value cannot tell a '
                      'string from a one-item array.',
                      "Each key appears once in a list, since the attestation's JSON "
                      'uses it as a key; the validator does not check this.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core'})

    annotation_key: str = Field(default=..., description="""The annotation's key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoAnnotation']} })
    annotation_values: Optional[list[str]] = Field(default=None, description="""The annotation's values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoAnnotation']} })


class InTotoResourceDescriptor(ConfiguredBaseModel):
    """
    A reference to a software artifact or other resource by URI or digest, or the resource itself as content, with optional metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'slot_conditions': {'resource_uri': {'any_of': [{'range': 'uri'}],
                                                          'name': 'resource_uri',
                                                          'required': True}}},
                    {'slot_conditions': {'digest': {'any_of': [{'range': 'InTotoDigestSet'}],
                                                    'name': 'digest',
                                                    'required': True}}},
                    {'slot_conditions': {'content': {'any_of': [{'range': 'string'}],
                                                     'name': 'content',
                                                     'required': True}}}],
         'comments': ['A descriptor carries at least one of a URI, a digest or its '
                      'content; a field that needs a particular one says so.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core',
         'notes': ['Each condition in any_of names its range through a nested any_of, '
                   "because the JSON Schema generator leaves a condition's own range "
                   'out, and a null value would then count as present.'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/resource_descriptor.md']})

    resource_uri: Optional[str] = Field(default=None, description="""The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/field_types.md#resourceuri'],
         'slot_uri': 'in_toto_linkml:resource_uri'} })
    digest: Optional[InTotoDigestSet] = Field(default=None, description="""The cryptographic digests of a resource's content, keyed by algorithm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md'],
         'slot_uri': 'in_toto_linkml:digest'} })
    resource_name: Optional[str] = Field(default=None, description="""A name for the resource within the attestation that carries it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })
    download_location: Optional[str] = Field(default=None, description="""Where the resource can be fetched, when that differs from its identifying URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })
    media_type: Optional[str] = Field(default=None, description="""The IANA media type of the resource's content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'], 'slot_uri': 'dcat:mediaType'} })
    content: Optional[str] = Field(default=None, description="""The resource's content itself, base64-encoded, for a resource small enough to carry inline.""", json_schema_extra = { "linkml_meta": {'comments': ['The in-toto framework asks for content under 1 KB, so that '
                      'attestations stay small.'],
         'domain_of': ['InTotoResourceDescriptor']} })
    annotations: Optional[list[InTotoAnnotation]] = Field(default=None, description="""Vendor-specific annotations on the resource, such as the source references a SLSA Source Verification Summary records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })

    @field_validator('content')
    def pattern_content(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9+/_-]+={0,2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid content format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid content format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoStatementSubject(InTotoResourceDescriptor):
    """
    One artifact an in-toto statement is about: a resource descriptor that carries a digest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/statement.md'],
         'slot_usage': {'digest': {'name': 'digest', 'required': True}}})

    resource_uri: Optional[str] = Field(default=None, description="""The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/field_types.md#resourceuri'],
         'slot_uri': 'in_toto_linkml:resource_uri'} })
    digest: InTotoDigestSet = Field(default=..., description="""The cryptographic digests of a resource's content, keyed by algorithm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md'],
         'slot_uri': 'in_toto_linkml:digest'} })
    resource_name: Optional[str] = Field(default=None, description="""A name for the resource within the attestation that carries it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })
    download_location: Optional[str] = Field(default=None, description="""Where the resource can be fetched, when that differs from its identifying URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })
    media_type: Optional[str] = Field(default=None, description="""The IANA media type of the resource's content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'], 'slot_uri': 'dcat:mediaType'} })
    content: Optional[str] = Field(default=None, description="""The resource's content itself, base64-encoded, for a resource small enough to carry inline.""", json_schema_extra = { "linkml_meta": {'comments': ['The in-toto framework asks for content under 1 KB, so that '
                      'attestations stay small.'],
         'domain_of': ['InTotoResourceDescriptor']} })
    annotations: Optional[list[InTotoAnnotation]] = Field(default=None, description="""Vendor-specific annotations on the resource, such as the source references a SLSA Source Verification Summary records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })

    @field_validator('content')
    def pattern_content(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9+/_-]+={0,2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid content format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid content format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoStatement(ConfiguredBaseModel):
    """
    The statement layer of an in-toto attestation: the subjects it is about, the type of its predicate and the predicate itself.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The signature envelope around a statement, and the bundle that '
                      'collects signed statements, are outside this model.',
                      'A statement is the attestation, and its predicate is one kind '
                      'of claim about the subjects, such as a test result or build '
                      'provenance.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/statement.md']})

    statement_type: str = Field(default=..., description="""The in-toto statement type, always https://in-toto.io/Statement/v1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement']} })
    subject: list[InTotoStatementSubject] = Field(default=..., description="""The artifacts the predicate is about, each with a digest.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement']} })
    predicate_type: str = Field(default=..., description="""The URI that names the predicate's type and so its schema, such as https://in-toto.io/attestation/test-result/v0.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement']} })
    statement_predicate: Optional[Union[InTotoTestResult,InTotoSimpleVerificationResult,InTotoScaiAttributeReport,InTotoLink,InTotoReference,InTotoRelease,InTotoRuntimeTrace,InTotoVulns]] = Field(default=None, description="""The predicate, one of the kinds this schema or an importing one models; predicate_kind names which. Unset means the same as empty.""", json_schema_extra = { "linkml_meta": {'comments': ["The attestation's JSON calls this field predicate. The name "
                      "here keeps it apart from LOKF's predicate, the type of a "
                      'relation, which a composite schema gives one IRI.'],
         'domain_of': ['InTotoStatement']} })

    @field_validator('statement_type')
    def pattern_statement_type(cls, v):
        pattern=re.compile(r"^https://in-toto\.io/Statement/v1$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid statement_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid statement_type format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoPredicate(ConfiguredBaseModel):
    """
    The base of every predicate an in-toto statement can carry; predicate_kind names the concrete kind.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'comments': ["The statement's predicate_type names the predicate's type by "
                      'URI, and each concrete class says which URI it renders. Nothing '
                      'ties the two, since a schema that imports this module may model '
                      'a predicate under its own URI.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/predicate.md']})

    predicate_kind: Literal["InTotoPredicate"] = Field(default="InTotoPredicate", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['InTotoPredicate']} })


class InTotoPredicateType(ConfiguredBaseModel):
    """
    A type of predicate an in-toto statement can carry, named by the URI a statement's predicate_type holds.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["The type URI includes the predicate's major version and changes "
                      'when the predicate changes incompatibly; a minor version keeps '
                      'it.',
                      'Anyone can define a predicate type. The in-toto project vets '
                      'some of them, and vetted_as names which vetted type this one '
                      'is.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/predicate.md',
                      'https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/README.md']})

    predicate_type_uri: str = Field(default=..., description="""The URI that names the predicate type, such as https://in-toto.io/attestation/test-result/v0.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoPredicateType']} })
    predicate_version: Optional[str] = Field(default=None, description="""The version of the predicate's specification, as its page states it, such as 0.1.0.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoPredicateType']} })
    predicate_specification: Optional[str] = Field(default=None, description="""The page that specifies the predicate.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoPredicateType']} })
    vetted_as: Optional[InTotoVettedPredicate] = Field(default=None, description="""The vetted predicate this type is, when the in-toto project vetted it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoPredicateType']} })


class InTotoObjectEntry(ConfiguredBaseModel):
    """
    One key of a JSON object whose keys the framework leaves to the producer, and the key's values.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['A string becomes one value and an array one value per item; any '
                      'other value or item is written as its JSON text, as '
                      'InTotoAnnotation does.',
                      "Each key appears once in a list, since the attestation's JSON "
                      'uses it as a key; the validator does not check this.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates'})

    entry_key: str = Field(default=..., description="""The object's key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoObjectEntry']} })
    entry_values: Optional[list[str]] = Field(default=None, description="""The key's values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoObjectEntry']} })


class InTotoTestResult(InTotoPredicate):
    """
    The predicate that records the result of one run of a test suite against the subjects, with the names of the tests that passed, warned and failed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The statement that carries it has predicate_type '
                      'https://in-toto.io/attestation/test-result/v0.1.',
                      'One attestation records one invocation of a suite.'],
         'exact_mappings': ['in_toto:test-result/v0.1'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/test-result.md']})

    test_result: InTotoTestResultValue = Field(default=..., description="""The result of the test run.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoTestResult']} })
    configuration: list[InTotoResourceDescriptor] = Field(default=..., description="""The configuration the test run used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoTestResult']} })
    test_run_url: Optional[str] = Field(default=None, description="""Where the test run can be read, such as a CI run that holds its logs; the verifier works out how to read it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoTestResult']} })
    passed_tests: Optional[list[str]] = Field(default=None, description="""The names of the tests that passed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoTestResult']} })
    warned_tests: Optional[list[str]] = Field(default=None, description="""The names of the tests that expressed a warning.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoTestResult']} })
    failed_tests: Optional[list[str]] = Field(default=None, description="""The names of the tests that failed.""", json_schema_extra = { "linkml_meta": {'comments': ['Producer and consumer agree on what a test name means; a policy '
                      'can check that test_result and failed_tests meet its '
                      'requirements.'],
         'domain_of': ['InTotoTestResult']} })
    predicate_kind: Literal["InTotoTestResult"] = Field(default="InTotoTestResult", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['InTotoPredicate']} })


class InTotoSimpleVerificationResult(InTotoPredicate):
    """
    The predicate that says a verifier evaluated the subjects against one or more policies, and which properties passed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The statement that carries it has predicate_type '
                      'https://in-toto.io/attestation/svr/v0.1.',
                      'It is a lighter form of the SLSA Verification Summary, which '
                      'lmodel/slsa models.'],
         'exact_mappings': ['in_toto:svr/v0.1'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/svr.md']})

    svr_verifier: InTotoSvrVerifier = Field(default=..., description="""The entity that performed the verification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoSimpleVerificationResult']} })
    time_created: str = Field(default=..., description="""When the verification took place.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoSimpleVerificationResult']} })
    verified_properties: list[str] = Field(default=..., description="""The properties of the subjects that passed verification, scoped to the framework or policy verified, such as SLSA_BUILD_LEVEL_3.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoSimpleVerificationResult']} })
    predicate_kind: Literal["InTotoSimpleVerificationResult"] = Field(default="InTotoSimpleVerificationResult", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['InTotoPredicate']} })


class InTotoSvrVerifier(ConfiguredBaseModel):
    """
    The entity that performed a simple verification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['A verifier with configurable policies may add fields of its own '
                      'that say which policy it applied; this schema does not model '
                      'them.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/svr.md']})

    svr_verifier_id: str = Field(default=..., description="""The URI that identifies the verifier, versioned when its verification logic changes materially.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoSvrVerifier']} })


class InTotoScaiAttributeReport(InTotoPredicate):
    """
    The Software Supply Chain Attribute Integrity (SCAI) predicate: assertions about functional attributes of the subjects or their producer, each with the evidence for it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The statement that carries it has predicate_type '
                      'https://in-toto.io/attestation/scai/v0.3.'],
         'exact_mappings': ['in_toto:scai/v0.3'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/scai.md']})

    scai_attributes: list[InTotoScaiAttributeAssertion] = Field(default=..., description="""One or more attribute assertions about the subjects.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoScaiAttributeReport']} })
    scai_producer: Optional[InTotoResourceDescriptor] = Field(default=None, description="""The producer of the subjects, where that applies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoScaiAttributeReport']} })
    predicate_kind: Literal["InTotoScaiAttributeReport"] = Field(default="InTotoScaiAttributeReport", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['InTotoPredicate']} })


class InTotoScaiAttributeAssertion(ConfiguredBaseModel):
    """
    One SCAI assertion: an attribute of the subject or its producer, what it applies to, under which conditions, and the evidence for it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/scai.md']})

    scai_attribute: str = Field(default=..., description="""The functional feature asserted, in a form the producer and consumer agree on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoScaiAttributeAssertion']} })
    scai_target: Optional[InTotoResourceDescriptor] = Field(default=None, description="""The artifact or metadata object the attribute applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoScaiAttributeAssertion']} })
    scai_conditions: Optional[list[InTotoObjectEntry]] = Field(default=None, description="""The conditions under which the attribute arises.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoScaiAttributeAssertion']} })
    scai_evidence: Optional[InTotoResourceDescriptor] = Field(default=None, description="""The evidence, authenticated where possible, for the asserted attribute.""", json_schema_extra = { "linkml_meta": {'comments': ['Without evidence a consumer may judge the assertion by who '
                      'produced the attestation.'],
         'domain_of': ['InTotoScaiAttributeAssertion']} })


class InTotoLink(InTotoPredicate):
    """
    The predicate that records one step of an in-toto layout: the command it ran and the materials it read, for a supply chain that migrates from in-toto 0.9 links.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The statement that carries it has predicate_type '
                      'https://in-toto.io/attestation/link/v0.3.',
                      "The statement's subjects are the step's products, and each "
                      "subject's resource_name is unique within the attestation; the "
                      'validator does not check this.'],
         'exact_mappings': ['in_toto:link/v0.3'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/link.md']})

    step_name: str = Field(default=..., description="""The name of the step, which a layout uses to find the link metadata it verifies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoLink']} })
    step_command: Optional[list[str]] = Field(default=None, description="""The command the step ran, and its arguments; possibly empty.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoLink']} })
    materials: Optional[list[InTotoLinkMaterial]] = Field(default=None, description="""The artifacts the step read.""", json_schema_extra = { "linkml_meta": {'comments': ["Each material's resource_name is unique among them; the "
                      'validator does not check this.'],
         'domain_of': ['InTotoLink']} })
    step_byproducts: Optional[list[InTotoObjectEntry]] = Field(default=None, description="""What else the step recorded, such as its standard output, in keys the in-toto specification describes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoLink']} })
    step_environment: Optional[list[InTotoObjectEntry]] = Field(default=None, description="""The environment the step ran in, in keys the producer chooses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoLink']} })
    predicate_kind: Literal["InTotoLink"] = Field(default="InTotoLink", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['InTotoPredicate']} })


class InTotoLinkMaterial(InTotoResourceDescriptor):
    """
    One material of a link, a resource descriptor with a name and a digest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'all_of': [{'slot_conditions': {'resource_name': {'any_of': [{'range': 'string'}],
                                                           'name': 'resource_name',
                                                           'required': True}}}],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'notes': ['The name is required through a slot condition rather than '
                   'slot_usage, because resource_name is an attribute of the parent '
                   'class and the LinkML loader refuses slot_usage on an inherited '
                   'attribute.'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/link.md'],
         'slot_usage': {'digest': {'name': 'digest', 'required': True}}})

    resource_uri: Optional[str] = Field(default=None, description="""The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/field_types.md#resourceuri'],
         'slot_uri': 'in_toto_linkml:resource_uri'} })
    digest: InTotoDigestSet = Field(default=..., description="""The cryptographic digests of a resource's content, keyed by algorithm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md'],
         'slot_uri': 'in_toto_linkml:digest'} })
    resource_name: Optional[str] = Field(default=None, description="""A name for the resource within the attestation that carries it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })
    download_location: Optional[str] = Field(default=None, description="""Where the resource can be fetched, when that differs from its identifying URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })
    media_type: Optional[str] = Field(default=None, description="""The IANA media type of the resource's content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'], 'slot_uri': 'dcat:mediaType'} })
    content: Optional[str] = Field(default=None, description="""The resource's content itself, base64-encoded, for a resource small enough to carry inline.""", json_schema_extra = { "linkml_meta": {'comments': ['The in-toto framework asks for content under 1 KB, so that '
                      'attestations stay small.'],
         'domain_of': ['InTotoResourceDescriptor']} })
    annotations: Optional[list[InTotoAnnotation]] = Field(default=None, description="""Vendor-specific annotations on the resource, such as the source references a SLSA Source Verification Summary records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })

    @field_validator('content')
    def pattern_content(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9+/_-]+={0,2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid content format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid content format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoReference(InTotoPredicate):
    """
    The predicate that points from the subjects, as a whole, to documents about them, such as a bill of materials.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The statement that carries it has predicate_type '
                      'https://in-toto.io/attestation/reference/v0.1.',
                      'Several documents in one predicate read as if each had an '
                      'attestation of its own with everything else unchanged.'],
         'exact_mappings': ['in_toto:reference/v0.1'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/reference.md']})

    reference_attester: InTotoReferenceAttester = Field(default=..., description="""The system that provides the documents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoReference']} })
    referenced_documents: list[InTotoReferencedDocument] = Field(default=..., description="""The documents referred to.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoReference']} })
    predicate_kind: Literal["InTotoReference"] = Field(default="InTotoReference", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['InTotoPredicate']} })


class InTotoReferenceAttester(ConfiguredBaseModel):
    """
    The system that provides the documents a Reference predicate points to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/reference.md']})

    reference_attester_id: str = Field(default=..., description="""The URI that identifies the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoReferenceAttester']} })


class InTotoReferencedDocument(InTotoResourceDescriptor):
    """
    One document a Reference predicate points to: a resource descriptor with a download location and a media type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'all_of': [{'slot_conditions': {'download_location': {'any_of': [{'range': 'uri'}],
                                                               'name': 'download_location',
                                                               'required': True}}},
                    {'slot_conditions': {'media_type': {'any_of': [{'range': 'string'}],
                                                        'name': 'media_type',
                                                        'required': True}}}],
         'comments': ['A document of unknown type takes media_type '
                      'application/octet-stream.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'notes': ['Both fields are required through slot conditions rather than '
                   'slot_usage, because they are attributes of the parent class and '
                   'the LinkML loader refuses slot_usage on an inherited attribute.'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/reference.md']})

    resource_uri: Optional[str] = Field(default=None, description="""The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/field_types.md#resourceuri'],
         'slot_uri': 'in_toto_linkml:resource_uri'} })
    digest: Optional[InTotoDigestSet] = Field(default=None, description="""The cryptographic digests of a resource's content, keyed by algorithm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md'],
         'slot_uri': 'in_toto_linkml:digest'} })
    resource_name: Optional[str] = Field(default=None, description="""A name for the resource within the attestation that carries it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })
    download_location: Optional[str] = Field(default=None, description="""Where the resource can be fetched, when that differs from its identifying URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })
    media_type: Optional[str] = Field(default=None, description="""The IANA media type of the resource's content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'], 'slot_uri': 'dcat:mediaType'} })
    content: Optional[str] = Field(default=None, description="""The resource's content itself, base64-encoded, for a resource small enough to carry inline.""", json_schema_extra = { "linkml_meta": {'comments': ['The in-toto framework asks for content under 1 KB, so that '
                      'attestations stay small.'],
         'domain_of': ['InTotoResourceDescriptor']} })
    annotations: Optional[list[InTotoAnnotation]] = Field(default=None, description="""Vendor-specific annotations on the resource, such as the source references a SLSA Source Verification Summary records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })

    @field_validator('content')
    def pattern_content(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9+/_-]+={0,2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid content format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid content format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoRelease(InTotoPredicate):
    """
    The predicate that ties the subjects to one release name and version of a package, so that consumers can check what the release should contain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The statement that carries it has predicate_type '
                      'https://in-toto.io/attestation/release/v0.1. The page is at '
                      'version 0.2, which renamed releaseId to packageId, and its '
                      'examples keep that URI.',
                      "Each subject's resource_name is the artifact's file name as it "
                      'would appear on disk.'],
         'exact_mappings': ['in_toto:release/v0.1'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/release.md']})

    release_purl: str = Field(default=..., description="""The package URL that names the release, with its version and, unless the package type needs them, no qualifiers or subpath.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoRelease']} })
    package_id: Optional[str] = Field(default=None, description="""A stable identifier for the package that does not change between releases, so that a consumer can tell a renamed package from a reused name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoRelease']} })
    predicate_kind: Literal["InTotoRelease"] = Field(default="InTotoRelease", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['InTotoPredicate']} })

    @field_validator('release_purl')
    def pattern_release_purl(cls, v):
        pattern=re.compile(r"^pkg:[A-Za-z.+-]+/[^@?#]+@[^?#]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid release_purl format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid release_purl format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoRuntimeTrace(InTotoPredicate):
    """
    The predicate that records what a monitor traced while a supply chain step, such as a build, ran.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The statement that carries it has predicate_type '
                      'https://in-toto.io/attestation/runtime-trace/v0.1.'],
         'exact_mappings': ['in_toto:runtime-trace/v0.1'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/runtime-trace.md']})

    trace_monitor: InTotoTraceMonitor = Field(default=..., description="""The monitor instance that traced the run.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoRuntimeTrace']} })
    monitored_process: InTotoMonitoredProcess = Field(default=..., description="""The process the monitor watched.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoRuntimeTrace']} })
    monitor_log: InTotoMonitorLog = Field(default=..., description="""The events the monitor traced.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoRuntimeTrace']} })
    trace_metadata: Optional[InTotoTraceMetadata] = Field(default=None, description="""Other properties of the monitoring event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoRuntimeTrace']} })
    predicate_kind: Literal["InTotoRuntimeTrace"] = Field(default="InTotoRuntimeTrace", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['InTotoPredicate']} })


class InTotoTraceMonitor(ConfiguredBaseModel):
    """
    The monitor instance that produced a runtime trace.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/runtime-trace.md']})

    monitor_type: str = Field(default=..., description="""The URI of the monitor's type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoTraceMonitor']} })
    monitor_config_source: Optional[InTotoResourceDescriptor] = Field(default=None, description="""The monitor's configuration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoTraceMonitor']} })
    trace_policy: Optional[list[InTotoObjectEntry]] = Field(default=None, description="""The trace policy the monitor applied, in the monitor's own format, which monitor_type names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoTraceMonitor']} })


class InTotoMonitoredProcess(ConfiguredBaseModel):
    """
    The process a runtime trace watched.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/runtime-trace.md']})

    host_id: str = Field(default=..., description="""The URI that identifies the host the process ran on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoMonitoredProcess']} })
    process_type: str = Field(default=..., description="""The URI of the type of process, such as the build type when the monitor watched a build.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoMonitoredProcess']} })
    process_event: str = Field(default=..., description="""The job or task the attestation is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoMonitoredProcess']} })


class InTotoMonitorLog(ConfiguredBaseModel):
    """
    The events a runtime trace's monitor recorded: processes, network activity and file accesses, at least one of them.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'slot_conditions': {'traced_processes': {'multivalued': True,
                                                              'name': 'traced_processes',
                                                              'required': True}}},
                    {'slot_conditions': {'traced_network': {'multivalued': True,
                                                            'name': 'traced_network',
                                                            'required': True}}},
                    {'slot_conditions': {'file_access': {'multivalued': True,
                                                         'name': 'file_access',
                                                         'required': True}}}],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'notes': ['Each condition in any_of names its range through a nested any_of, '
                   "because the JSON Schema generator leaves a condition's own range "
                   'out, and a null value would then count as present.'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/runtime-trace.md']})

    traced_processes: Optional[list[str]] = Field(default=None, description="""The processes the monitor observed, one JSON object each, written as its JSON text, in a format monitor_type determines.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoMonitorLog']} })
    traced_network: Optional[list[str]] = Field(default=None, description="""The network activity the monitor observed, one JSON object each, written as its JSON text, in a format monitor_type determines.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoMonitorLog']} })
    file_access: Optional[list[InTotoResourceDescriptor]] = Field(default=None, description="""The files the run accessed, each with its path and digests; one file may appear more than once, with different digests if it changed.""", json_schema_extra = { "linkml_meta": {'comments': ['A monitor that cannot pause the build, such as one that uses '
                      'eBPF, guarantees less about these digests than one that can.'],
         'domain_of': ['InTotoMonitorLog']} })


class InTotoTraceMetadata(ConfiguredBaseModel):
    """
    Other properties of a runtime trace's monitoring event.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/runtime-trace.md']})

    build_started_on: Optional[str] = Field(default=None, description="""When the monitored build started.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoTraceMetadata']} })
    build_finished_on: Optional[str] = Field(default=None, description="""When the monitored build finished.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoTraceMetadata']} })


class InTotoVulns(InTotoPredicate):
    """
    The predicate that records the result of one vulnerability scan of the subjects: the scanner, its database and the vulnerabilities it found.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The statement that carries it has predicate_type '
                      'https://in-toto.io/attestation/vulns/v0.2.'],
         'exact_mappings': ['in_toto:vulns/v0.2'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/vulns_02.md']})

    vuln_scanner: InTotoVulnScanner = Field(default=..., description="""The scanner that ran, its version and the database it used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulns']} })
    scan_metadata: InTotoScanMetadata = Field(default=..., description="""When the scan ran.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulns']} })
    predicate_kind: Literal["InTotoVulns"] = Field(default="InTotoVulns", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['InTotoPredicate']} })


class InTotoVulnScanner(ConfiguredBaseModel):
    """
    The scanner a VULNS predicate records, with its results.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/vulns_02.md']})

    scanner_uri: str = Field(default=..., description="""The URI that identifies the scanner's source.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulnScanner']} })
    scanner_version: Optional[str] = Field(default=None, description="""The scanner's version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulnScanner']} })
    vuln_db: Optional[InTotoVulnDatabase] = Field(default=None, description="""The vulnerability database the scanner used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulnScanner']} })
    scan_results: list[InTotoVulnResult] = Field(default=..., description="""The vulnerabilities the scanner found; an empty list means it found none.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulnScanner']} })


class InTotoVulnDatabase(ConfiguredBaseModel):
    """
    The vulnerability database a scanner used.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/vulns_02.md']})

    db_uri: Optional[str] = Field(default=None, description="""The URI that identifies the database's source.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulnDatabase']} })
    db_version: Optional[str] = Field(default=None, description="""The database's version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulnDatabase']} })
    db_last_update: str = Field(default=..., description="""When the database was last updated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulnDatabase']} })


class InTotoVulnResult(ConfiguredBaseModel):
    """
    One vulnerability a scanner found.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/vulns_02.md']})

    vuln_id: str = Field(default=..., description="""The vulnerability's identifier, such as GHSA-fxph-q3j8-mv87 or CVE-2017-5645.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulnResult']} })
    vuln_severity: list[InTotoVulnSeverity] = Field(default=..., description="""The vulnerability's severity, by one or more scoring methods.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulnResult']} })
    vuln_annotations: Optional[list[InTotoObjectEntry]] = Field(default=None, description="""Custom information the scanner adds, as key and value pairs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulnResult']} })


class InTotoVulnSeverity(ConfiguredBaseModel):
    """
    One severity score of a vulnerability, by one scoring method.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/vulns_02.md']})

    severity_method: str = Field(default=..., description="""The scoring method, such as nvd or cvss.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulnSeverity']} })
    severity_score: str = Field(default=..., description="""The score under that method, as a string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoVulnSeverity']} })


class InTotoScanMetadata(ConfiguredBaseModel):
    """
    When a vulnerability scan ran.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_predicates',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/vulns_02.md']})

    scan_started_on: str = Field(default=..., description="""When the scan started.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoScanMetadata']} })
    scan_finished_on: str = Field(default=..., description="""When the scan finished.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoScanMetadata']} })


class InTotoDocument(ConfiguredBaseModel):
    """
    A document that holds in-toto statements and the predicate types they name.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto', 'tree_root': True})

    in_toto_statements: Optional[list[InTotoStatement]] = Field(default=None, description="""The statements, each an in-toto attestation without its envelope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDocument']} })
    in_toto_predicate_types: Optional[list[InTotoPredicateType]] = Field(default=None, description="""The predicate types.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDocument']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
InTotoDigestSet.model_rebuild()
InTotoAdditionalDigest.model_rebuild()
InTotoAnnotation.model_rebuild()
InTotoResourceDescriptor.model_rebuild()
InTotoStatementSubject.model_rebuild()
InTotoStatement.model_rebuild()
InTotoPredicate.model_rebuild()
InTotoPredicateType.model_rebuild()
InTotoObjectEntry.model_rebuild()
InTotoTestResult.model_rebuild()
InTotoSimpleVerificationResult.model_rebuild()
InTotoSvrVerifier.model_rebuild()
InTotoScaiAttributeReport.model_rebuild()
InTotoScaiAttributeAssertion.model_rebuild()
InTotoLink.model_rebuild()
InTotoLinkMaterial.model_rebuild()
InTotoReference.model_rebuild()
InTotoReferenceAttester.model_rebuild()
InTotoReferencedDocument.model_rebuild()
InTotoRelease.model_rebuild()
InTotoRuntimeTrace.model_rebuild()
InTotoTraceMonitor.model_rebuild()
InTotoMonitoredProcess.model_rebuild()
InTotoMonitorLog.model_rebuild()
InTotoTraceMetadata.model_rebuild()
InTotoVulns.model_rebuild()
InTotoVulnScanner.model_rebuild()
InTotoVulnDatabase.model_rebuild()
InTotoVulnResult.model_rebuild()
InTotoVulnSeverity.model_rebuild()
InTotoScanMetadata.model_rebuild()
InTotoDocument.model_rebuild()
