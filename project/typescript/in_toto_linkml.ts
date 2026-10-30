/**
* The result of a test run, as a Test Result predicate records it.
*/
export enum InTotoTestResultValue {
    
    /** The run passed. */
    PASSED = "PASSED",
    /** The run passed with warnings. */
    WARNED = "WARNED",
    /** The run failed. */
    FAILED = "FAILED",
};
/**
* The thirteen predicate types the in-toto project lists as vetted at release v1.2.0, each with the predicate_type a statement of it carries at the version its page describes.
*/
export enum InTotoVettedPredicate {
    
    /** A CycloneDX bill of materials for software artifacts. */
    CYCLONEDX = "CYCLONEDX",
    /** One step of an in-toto layout, for migration from in-toto 0.9. */
    LINK = "LINK",
    /** References to documents relevant to a resource. */
    REFERENCE = "REFERENCE",
    /** An artifact that is part of a given release version. */
    RELEASE = "RELEASE",
    /** Runtime traces of software supply chain operations. */
    RUNTIME_TRACE = "RUNTIME_TRACE",
    /** Evidence-based assertions about software artifact and supply chain attributes or behaviour. */
    SCAI = "SCAI",
    /** How an artifact or set of artifacts was produced; lmodel/slsa models it. */
    SLSA_PROVENANCE = "SLSA_PROVENANCE",
    /** A SLSA verification decision about a software artifact; lmodel/slsa models it. */
    SLSA_VERIFICATION_SUMMARY = "SLSA_VERIFICATION_SUMMARY",
    /** An SPDX 2 bill of materials for software artifacts. */
    SPDX2 = "SPDX2",
    /** An SPDX 3 bill of materials for software artifacts. */
    SPDX3 = "SPDX3",
    /** Evidence that an artifact was evaluated against one or more policies. */
    SIMPLE_VERIFICATION_RESULT = "SIMPLE_VERIFICATION_RESULT",
    /** The results of any type of test. */
    TEST_RESULT = "TEST_RESULT",
    /** The results of a vulnerability scan of software artifacts. */
    VULNS = "VULNS",
};


/**
 * A set of one or more digests over one artifact, keyed by algorithm, from which a consumer picks the algorithm it trusts.
 */
export interface InTotoDigestSet {
    /** The SHA-256 digest of the artifact. */
    sha256?: string,
    /** The SHA-224 digest of the artifact. */
    sha224?: string,
    /** The SHA-384 digest of the artifact. */
    sha384?: string,
    /** The SHA-512 digest of the artifact. */
    sha512?: string,
    /** The SHA-512/224 digest of the artifact. */
    sha512_224?: string,
    /** The SHA-512/256 digest of the artifact. */
    sha512_256?: string,
    /** The SHA3-224 digest of the artifact. */
    sha3_224?: string,
    /** The SHA3-256 digest of the artifact. */
    sha3_256?: string,
    /** The SHA3-384 digest of the artifact. */
    sha3_384?: string,
    /** The SHA3-512 digest of the artifact. */
    sha3_512?: string,
    /** The SHAKE128 digest of the artifact, of at least 32 bytes. */
    shake128?: string,
    /** The SHAKE256 digest of the artifact, of at least 32 bytes. */
    shake256?: string,
    /** The BLAKE2b digest of the artifact, of 32 to 64 bytes. */
    blake2b?: string,
    /** The BLAKE2s digest of the artifact, at its full 32 bytes. */
    blake2s?: string,
    /** The RIPEMD-160 digest of the artifact. */
    ripemd160?: string,
    /** The SM3 digest of the artifact. */
    sm3?: string,
    /** The GOST R 34.11 digest of the artifact, of 256 or 512 bits. */
    gost?: string,
    /** The SHA-1 digest of the artifact. */
    sha1?: string,
    /** The MD5 digest of the artifact. */
    md5?: string,
    /** A digest over a directory's content by the dirhash Hash1 function, in lowercase hexadecimal rather than base64. */
    dir_hash?: string,
    /** The git commit id of a source revision. */
    git_commit?: string,
    /** The git tree id of a source revision's content, or of any file tree. */
    git_tree?: string,
    /** The git blob id of a file's content. */
    git_blob?: string,
    /** The git object id of an annotated tag. */
    git_tag?: string,
    /** The digests under algorithms this class does not name. */
    additional_digests?: InTotoAdditionalDigest[],
}


/**
 * One digest under an algorithm that InTotoDigestSet does not name, such as an SCS's own revision type.
 */
export interface InTotoAdditionalDigest {
    /** The algorithm's name, as the key the attestation's JSON uses, such as svn_revision_id. */
    algorithm: string,
    /** The digest under that algorithm, in the encoding the algorithm documents. */
    value: string,
}


/**
 * One vendor-specific annotation on a resource descriptor: a key and its values.
 */
export interface InTotoAnnotation {
    /** The annotation's key. */
    annotation_key: string,
    /** The annotation's values. */
    annotation_values?: string[],
}


/**
 * A reference to a software artifact or other resource by URI or digest, or the resource itself as content, with optional metadata.
 */
export interface InTotoResourceDescriptor {
    /** The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference. */
    resource_uri?: string,
    /** The cryptographic digests of a resource's content, keyed by algorithm. */
    digest?: InTotoDigestSet,
    /** A name for the resource within the attestation that carries it. */
    resource_name?: string,
    /** Where the resource can be fetched, when that differs from its identifying URI. */
    download_location?: string,
    /** The IANA media type of the resource's content. */
    media_type?: string,
    /** The resource's content itself, base64-encoded, for a resource small enough to carry inline. */
    content?: string,
    /** Vendor-specific annotations on the resource, such as the source references a SLSA Source Verification Summary records. */
    annotations?: InTotoAnnotation[],
}


/**
 * One artifact an in-toto statement is about: a resource descriptor that carries a digest.
 */
export interface InTotoStatementSubject extends InTotoResourceDescriptor {
}


/**
 * The statement layer of an in-toto attestation: the subjects it is about, the type of its predicate and the predicate itself.
 */
export interface InTotoStatement {
    /** The predicate, one of the kinds this schema or an importing one models; predicate_kind names which. Unset means the same as empty. */
    predicate?: InTotoPredicate,
    /** The in-toto statement type, always https://in-toto.io/Statement/v1. */
    statement_type: string,
    /** The artifacts the predicate is about, each with a digest. */
    subject: InTotoStatementSubject[],
    /** The URI that names the predicate's type and so its schema, such as https://in-toto.io/attestation/test-result/v0.1. */
    predicate_type: string,
}


/**
 * The base of every predicate an in-toto statement can carry; predicate_kind names the concrete kind.
 */
export interface InTotoPredicate {
    /** The kind of predicate, one of this class's descendants. */
    predicate_kind?: string,
}


/**
 * A type of predicate an in-toto statement can carry, named by the URI a statement's predicate_type holds.
 */
export interface InTotoPredicateType {
    /** The URI that names the predicate type, such as https://in-toto.io/attestation/test-result/v0.1. */
    predicate_type_uri: string,
    /** The version of the predicate's specification, as its page states it, such as 0.1.0. */
    predicate_version?: string,
    /** The page that specifies the predicate. */
    predicate_specification?: string,
    /** The vetted predicate this type is, when the in-toto project vetted it. */
    vetted_as?: string,
}


/**
 * One key of a JSON object whose keys the framework leaves to the producer, and the key's values.
 */
export interface InTotoObjectEntry {
    /** The object's key. */
    entry_key: string,
    /** The key's values. */
    entry_values?: string[],
}


/**
 * The predicate that records the result of one run of a test suite against the subjects, with the names of the tests that passed, warned and failed.
 */
export interface InTotoTestResult extends InTotoPredicate {
    /** The result of the test run. */
    test_result: string,
    /** The configuration the test run used. */
    configuration: InTotoResourceDescriptor[],
    /** Where the test run can be read, such as a CI run that holds its logs; the verifier works out how to read it. */
    test_run_url?: string,
    /** The names of the tests that passed. */
    passed_tests?: string[],
    /** The names of the tests that expressed a warning. */
    warned_tests?: string[],
    /** The names of the tests that failed. */
    failed_tests?: string[],
}


/**
 * The predicate that says a verifier evaluated the subjects against one or more policies, and which properties passed.
 */
export interface InTotoSimpleVerificationResult extends InTotoPredicate {
    /** The entity that performed the verification. */
    svr_verifier: InTotoSvrVerifier,
    /** When the verification took place. */
    time_created: string,
    /** The properties of the subjects that passed verification, scoped to the framework or policy verified, such as SLSA_BUILD_LEVEL_3. */
    verified_properties: string[],
}


/**
 * The entity that performed a simple verification.
 */
export interface InTotoSvrVerifier {
    /** The URI that identifies the verifier, versioned when its verification logic changes materially. */
    svr_verifier_id: string,
}


/**
 * The Software Supply Chain Attribute Integrity (SCAI) predicate: assertions about functional attributes of the subjects or their producer, each with the evidence for it.
 */
export interface InTotoScaiAttributeReport extends InTotoPredicate {
    /** One or more attribute assertions about the subjects. */
    scai_attributes: InTotoScaiAttributeAssertion[],
    /** The producer of the subjects, where that applies. */
    scai_producer?: InTotoResourceDescriptor,
}


/**
 * One SCAI assertion: an attribute of the subject or its producer, what it applies to, under which conditions, and the evidence for it.
 */
export interface InTotoScaiAttributeAssertion {
    /** The functional feature asserted, in a form the producer and consumer agree on. */
    scai_attribute: string,
    /** The artifact or metadata object the attribute applies to. */
    scai_target?: InTotoResourceDescriptor,
    /** The conditions under which the attribute arises. */
    scai_conditions?: InTotoObjectEntry[],
    /** The evidence, authenticated where possible, for the asserted attribute. */
    scai_evidence?: InTotoResourceDescriptor,
}


/**
 * The predicate that records one step of an in-toto layout: the command it ran and the materials it read, for a supply chain that migrates from in-toto 0.9 links.
 */
export interface InTotoLink extends InTotoPredicate {
    /** The name of the step, which a layout uses to find the link metadata it verifies. */
    step_name: string,
    /** The command the step ran, and its arguments; possibly empty. */
    step_command?: string[],
    /** The artifacts the step read. */
    materials?: InTotoLinkMaterial[],
    /** What else the step recorded, such as its standard output, in keys the in-toto specification describes. */
    step_byproducts?: InTotoObjectEntry[],
    /** The environment the step ran in, in keys the producer chooses. */
    step_environment?: InTotoObjectEntry[],
}


/**
 * One material of a link, a resource descriptor with a name and a digest.
 */
export interface InTotoLinkMaterial extends InTotoResourceDescriptor {
}


/**
 * The predicate that points from the subjects, as a whole, to documents about them, such as a bill of materials.
 */
export interface InTotoReference extends InTotoPredicate {
    /** The system that provides the documents. */
    reference_attester: InTotoReferenceAttester,
    /** The documents referred to. */
    referenced_documents: InTotoReferencedDocument[],
}


/**
 * The system that provides the documents a Reference predicate points to.
 */
export interface InTotoReferenceAttester {
    /** The URI that identifies the system. */
    reference_attester_id: string,
}


/**
 * One document a Reference predicate points to: a resource descriptor with a download location and a media type.
 */
export interface InTotoReferencedDocument extends InTotoResourceDescriptor {
}


/**
 * The predicate that ties the subjects to one release name and version of a package, so that consumers can check what the release should contain.
 */
export interface InTotoRelease extends InTotoPredicate {
    /** The package URL that names the release, with its version and, unless the package type needs them, no qualifiers or subpath. */
    release_purl: string,
    /** A stable identifier for the package that does not change between releases, so that a consumer can tell a renamed package from a reused name. */
    package_id?: string,
}


/**
 * The predicate that records what a monitor traced while a supply chain step, such as a build, ran.
 */
export interface InTotoRuntimeTrace extends InTotoPredicate {
    /** The monitor instance that traced the run. */
    trace_monitor: InTotoTraceMonitor,
    /** The process the monitor watched. */
    monitored_process: InTotoMonitoredProcess,
    /** The events the monitor traced. */
    monitor_log: InTotoMonitorLog,
    /** Other properties of the monitoring event. */
    trace_metadata?: InTotoTraceMetadata,
}


/**
 * The monitor instance that produced a runtime trace.
 */
export interface InTotoTraceMonitor {
    /** The URI of the monitor's type. */
    monitor_type: string,
    /** The monitor's configuration. */
    monitor_config_source?: InTotoResourceDescriptor,
    /** The trace policy the monitor applied, in the monitor's own format, which monitor_type names. */
    trace_policy?: InTotoObjectEntry[],
}


/**
 * The process a runtime trace watched.
 */
export interface InTotoMonitoredProcess {
    /** The URI that identifies the host the process ran on. */
    host_id: string,
    /** The URI of the type of process, such as the build type when the monitor watched a build. */
    process_type: string,
    /** The job or task the attestation is about. */
    process_event: string,
}


/**
 * The events a runtime trace's monitor recorded: processes, network activity and file accesses, at least one of them.
 */
export interface InTotoMonitorLog {
    /** The processes the monitor observed, one JSON object each, written as its JSON text, in a format monitor_type determines. */
    traced_processes?: string[],
    /** The network activity the monitor observed, one JSON object each, written as its JSON text, in a format monitor_type determines. */
    traced_network?: string[],
    /** The files the run accessed, each with its path and digests; one file may appear more than once, with different digests if it changed. */
    file_access?: InTotoResourceDescriptor[],
}


/**
 * Other properties of a runtime trace's monitoring event.
 */
export interface InTotoTraceMetadata {
    /** When the monitored build started. */
    build_started_on?: string,
    /** When the monitored build finished. */
    build_finished_on?: string,
}


/**
 * The predicate that records the result of one vulnerability scan of the subjects: the scanner, its database and the vulnerabilities it found.
 */
export interface InTotoVulns extends InTotoPredicate {
    /** The scanner that ran, its version and the database it used. */
    vuln_scanner: InTotoVulnScanner,
    /** When the scan ran. */
    scan_metadata: InTotoScanMetadata,
}


/**
 * The scanner a VULNS predicate records, with its results.
 */
export interface InTotoVulnScanner {
    /** The URI that identifies the scanner's source. */
    scanner_uri: string,
    /** The scanner's version. */
    scanner_version?: string,
    /** The vulnerability database the scanner used. */
    vuln_db?: InTotoVulnDatabase,
    /** The vulnerabilities the scanner found; an empty list means it found none. */
    scan_results: InTotoVulnResult[],
}


/**
 * The vulnerability database a scanner used.
 */
export interface InTotoVulnDatabase {
    /** The URI that identifies the database's source. */
    db_uri?: string,
    /** The database's version. */
    db_version?: string,
    /** When the database was last updated. */
    db_last_update: string,
}


/**
 * One vulnerability a scanner found.
 */
export interface InTotoVulnResult {
    /** The vulnerability's identifier, such as GHSA-fxph-q3j8-mv87 or CVE-2017-5645. */
    vuln_id: string,
    /** The vulnerability's severity, by one or more scoring methods. */
    vuln_severity: InTotoVulnSeverity[],
    /** Custom information the scanner adds, as key and value pairs. */
    vuln_annotations?: InTotoObjectEntry[],
}


/**
 * One severity score of a vulnerability, by one scoring method.
 */
export interface InTotoVulnSeverity {
    /** The scoring method, such as nvd or cvss. */
    severity_method: string,
    /** The score under that method, as a string. */
    severity_score: string,
}


/**
 * When a vulnerability scan ran.
 */
export interface InTotoScanMetadata {
    /** When the scan started. */
    scan_started_on: string,
    /** When the scan finished. */
    scan_finished_on: string,
}


/**
 * A document that holds in-toto statements and the predicate types they name.
 */
export interface InTotoDocument {
    /** The statements, each an in-toto attestation without its envelope. */
    in_toto_statements?: InTotoStatement[],
    /** The predicate types. */
    in_toto_predicate_types?: InTotoPredicateType[],
}



