-- # Class: InTotoDocument Description: A document that holds in-toto statements and the predicate types they name.
--     * Slot: id
-- # Class: InTotoDigestSet Description: A set of one or more digests over one artifact, keyed by algorithm, from which a consumer picks the algorithm it trusts.
--     * Slot: id
--     * Slot: sha256 Description: The SHA-256 digest of the artifact.
--     * Slot: sha224 Description: The SHA-224 digest of the artifact.
--     * Slot: sha384 Description: The SHA-384 digest of the artifact.
--     * Slot: sha512 Description: The SHA-512 digest of the artifact.
--     * Slot: sha512_224 Description: The SHA-512/224 digest of the artifact.
--     * Slot: sha512_256 Description: The SHA-512/256 digest of the artifact.
--     * Slot: sha3_224 Description: The SHA3-224 digest of the artifact.
--     * Slot: sha3_256 Description: The SHA3-256 digest of the artifact.
--     * Slot: sha3_384 Description: The SHA3-384 digest of the artifact.
--     * Slot: sha3_512 Description: The SHA3-512 digest of the artifact.
--     * Slot: shake128 Description: The SHAKE128 digest of the artifact, of at least 32 bytes.
--     * Slot: shake256 Description: The SHAKE256 digest of the artifact, of at least 32 bytes.
--     * Slot: blake2b Description: The BLAKE2b digest of the artifact, of 32 to 64 bytes.
--     * Slot: blake2s Description: The BLAKE2s digest of the artifact, at its full 32 bytes.
--     * Slot: ripemd160 Description: The RIPEMD-160 digest of the artifact.
--     * Slot: sm3 Description: The SM3 digest of the artifact.
--     * Slot: gost Description: The GOST R 34.11 digest of the artifact, of 256 or 512 bits.
--     * Slot: sha1 Description: The SHA-1 digest of the artifact.
--     * Slot: md5 Description: The MD5 digest of the artifact.
--     * Slot: dir_hash Description: A digest over a directory's content by the dirhash Hash1 function, in lowercase hexadecimal rather than base64.
--     * Slot: git_commit Description: The git commit id of a source revision.
--     * Slot: git_tree Description: The git tree id of a source revision's content, or of any file tree.
--     * Slot: git_blob Description: The git blob id of a file's content.
--     * Slot: git_tag Description: The git object id of an annotated tag.
-- # Class: InTotoAdditionalDigest Description: One digest under an algorithm that InTotoDigestSet does not name, such as an SCS's own revision type.
--     * Slot: id
--     * Slot: algorithm Description: The algorithm's name, as the key the attestation's JSON uses, such as svn_revision_id.
--     * Slot: value Description: The digest under that algorithm, in the encoding the algorithm documents.
--     * Slot: InTotoDigestSet_id Description: Autocreated FK slot
-- # Class: InTotoAnnotation Description: One vendor-specific annotation on a resource descriptor: a key and its values.
--     * Slot: id
--     * Slot: annotation_key Description: The annotation's key.
--     * Slot: InTotoResourceDescriptor_id Description: Autocreated FK slot
--     * Slot: InTotoStatementSubject_id Description: Autocreated FK slot
--     * Slot: InTotoLinkMaterial_id Description: Autocreated FK slot
--     * Slot: InTotoReferencedDocument_id Description: Autocreated FK slot
-- # Class: InTotoResourceDescriptor Description: A reference to a software artifact or other resource by URI or digest, or the resource itself as content, with optional metadata.
--     * Slot: id
--     * Slot: resource_uri Description: The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.
--     * Slot: resource_name Description: A name for the resource within the attestation that carries it.
--     * Slot: download_location Description: Where the resource can be fetched, when that differs from its identifying URI.
--     * Slot: media_type Description: The IANA media type of the resource's content.
--     * Slot: content Description: The resource's content itself, base64-encoded, for a resource small enough to carry inline.
--     * Slot: InTotoTestResult_id Description: Autocreated FK slot
--     * Slot: InTotoMonitorLog_id Description: Autocreated FK slot
--     * Slot: digest_id Description: The cryptographic digests of a resource's content, keyed by algorithm.
-- # Class: InTotoStatementSubject Description: One artifact an in-toto statement is about: a resource descriptor that carries a digest.
--     * Slot: id
--     * Slot: resource_uri Description: The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.
--     * Slot: resource_name Description: A name for the resource within the attestation that carries it.
--     * Slot: download_location Description: Where the resource can be fetched, when that differs from its identifying URI.
--     * Slot: media_type Description: The IANA media type of the resource's content.
--     * Slot: content Description: The resource's content itself, base64-encoded, for a resource small enough to carry inline.
--     * Slot: InTotoStatement_id Description: Autocreated FK slot
--     * Slot: digest_id Description: The cryptographic digests of a resource's content, keyed by algorithm.
-- # Class: InTotoStatement Description: The statement layer of an in-toto attestation: the subjects it is about, the type of its predicate and the predicate itself.
--     * Slot: id
--     * Slot: statement_type Description: The in-toto statement type, always https://in-toto.io/Statement/v1.
--     * Slot: predicate_type Description: The URI that names the predicate's type and so its schema, such as https://in-toto.io/attestation/test-result/v0.1.
--     * Slot: InTotoDocument_id Description: Autocreated FK slot
--     * Slot: predicate_id Description: The predicate, one of the kinds this schema or an importing one models; predicate_kind names which. Unset means the same as empty.
-- # Abstract Class: InTotoPredicate Description: The base of every predicate an in-toto statement can carry; predicate_kind names the concrete kind.
--     * Slot: id
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
-- # Class: InTotoPredicateType Description: A type of predicate an in-toto statement can carry, named by the URI a statement's predicate_type holds.
--     * Slot: id
--     * Slot: predicate_type_uri Description: The URI that names the predicate type, such as https://in-toto.io/attestation/test-result/v0.1.
--     * Slot: predicate_version Description: The version of the predicate's specification, as its page states it, such as 0.1.0.
--     * Slot: predicate_specification Description: The page that specifies the predicate.
--     * Slot: vetted_as Description: The vetted predicate this type is, when the in-toto project vetted it.
--     * Slot: InTotoDocument_id Description: Autocreated FK slot
-- # Class: InTotoObjectEntry Description: One key of a JSON object whose keys the framework leaves to the producer, and the key's values.
--     * Slot: id
--     * Slot: entry_key Description: The object's key.
--     * Slot: InTotoScaiAttributeAssertion_id Description: Autocreated FK slot
--     * Slot: InTotoLink_id Description: Autocreated FK slot
--     * Slot: InTotoTraceMonitor_id Description: Autocreated FK slot
--     * Slot: InTotoVulnResult_id Description: Autocreated FK slot
-- # Class: InTotoTestResult Description: The predicate that records the result of one run of a test suite against the subjects, with the names of the tests that passed, warned and failed.
--     * Slot: id
--     * Slot: test_result Description: The result of the test run.
--     * Slot: test_run_url Description: Where the test run can be read, such as a CI run that holds its logs; the verifier works out how to read it.
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
-- # Class: InTotoSimpleVerificationResult Description: The predicate that says a verifier evaluated the subjects against one or more policies, and which properties passed.
--     * Slot: id
--     * Slot: time_created Description: When the verification took place.
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
--     * Slot: svr_verifier_id Description: The entity that performed the verification.
-- # Class: InTotoSvrVerifier Description: The entity that performed a simple verification.
--     * Slot: id
--     * Slot: svr_verifier_id Description: The URI that identifies the verifier, versioned when its verification logic changes materially.
-- # Class: InTotoScaiAttributeReport Description: The Software Supply Chain Attribute Integrity (SCAI) predicate: assertions about functional attributes of the subjects or their producer, each with the evidence for it.
--     * Slot: id
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
--     * Slot: scai_producer_id Description: The producer of the subjects, where that applies.
-- # Class: InTotoScaiAttributeAssertion Description: One SCAI assertion: an attribute of the subject or its producer, what it applies to, under which conditions, and the evidence for it.
--     * Slot: id
--     * Slot: scai_attribute Description: The functional feature asserted, in a form the producer and consumer agree on.
--     * Slot: InTotoScaiAttributeReport_id Description: Autocreated FK slot
--     * Slot: scai_target_id Description: The artifact or metadata object the attribute applies to.
--     * Slot: scai_evidence_id Description: The evidence, authenticated where possible, for the asserted attribute.
-- # Class: InTotoLink Description: The predicate that records one step of an in-toto layout: the command it ran and the materials it read, for a supply chain that migrates from in-toto 0.9 links.
--     * Slot: id
--     * Slot: step_name Description: The name of the step, which a layout uses to find the link metadata it verifies.
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
-- # Class: InTotoLinkMaterial Description: One material of a link, a resource descriptor with a name and a digest.
--     * Slot: id
--     * Slot: resource_uri Description: The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.
--     * Slot: resource_name Description: A name for the resource within the attestation that carries it.
--     * Slot: download_location Description: Where the resource can be fetched, when that differs from its identifying URI.
--     * Slot: media_type Description: The IANA media type of the resource's content.
--     * Slot: content Description: The resource's content itself, base64-encoded, for a resource small enough to carry inline.
--     * Slot: InTotoLink_id Description: Autocreated FK slot
--     * Slot: digest_id Description: The cryptographic digests of a resource's content, keyed by algorithm.
-- # Class: InTotoReference Description: The predicate that points from the subjects, as a whole, to documents about them, such as a bill of materials.
--     * Slot: id
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
--     * Slot: reference_attester_id Description: The system that provides the documents.
-- # Class: InTotoReferenceAttester Description: The system that provides the documents a Reference predicate points to.
--     * Slot: id
--     * Slot: reference_attester_id Description: The URI that identifies the system.
-- # Class: InTotoReferencedDocument Description: One document a Reference predicate points to: a resource descriptor with a download location and a media type.
--     * Slot: id
--     * Slot: resource_uri Description: The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.
--     * Slot: resource_name Description: A name for the resource within the attestation that carries it.
--     * Slot: download_location Description: Where the resource can be fetched, when that differs from its identifying URI.
--     * Slot: media_type Description: The IANA media type of the resource's content.
--     * Slot: content Description: The resource's content itself, base64-encoded, for a resource small enough to carry inline.
--     * Slot: InTotoReference_id Description: Autocreated FK slot
--     * Slot: digest_id Description: The cryptographic digests of a resource's content, keyed by algorithm.
-- # Class: InTotoRelease Description: The predicate that ties the subjects to one release name and version of a package, so that consumers can check what the release should contain.
--     * Slot: id
--     * Slot: release_purl Description: The package URL that names the release, with its version and, unless the package type needs them, no qualifiers or subpath.
--     * Slot: package_id Description: A stable identifier for the package that does not change between releases, so that a consumer can tell a renamed package from a reused name.
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
-- # Class: InTotoRuntimeTrace Description: The predicate that records what a monitor traced while a supply chain step, such as a build, ran.
--     * Slot: id
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
--     * Slot: trace_monitor_id Description: The monitor instance that traced the run.
--     * Slot: monitored_process_id Description: The process the monitor watched.
--     * Slot: monitor_log_id Description: The events the monitor traced.
--     * Slot: trace_metadata_id Description: Other properties of the monitoring event.
-- # Class: InTotoTraceMonitor Description: The monitor instance that produced a runtime trace.
--     * Slot: id
--     * Slot: monitor_type Description: The URI of the monitor's type.
--     * Slot: monitor_config_source_id Description: The monitor's configuration.
-- # Class: InTotoMonitoredProcess Description: The process a runtime trace watched.
--     * Slot: id
--     * Slot: host_id Description: The URI that identifies the host the process ran on.
--     * Slot: process_type Description: The URI of the type of process, such as the build type when the monitor watched a build.
--     * Slot: process_event Description: The job or task the attestation is about.
-- # Class: InTotoMonitorLog Description: The events a runtime trace's monitor recorded: processes, network activity and file accesses, at least one of them.
--     * Slot: id
-- # Class: InTotoTraceMetadata Description: Other properties of a runtime trace's monitoring event.
--     * Slot: id
--     * Slot: build_started_on Description: When the monitored build started.
--     * Slot: build_finished_on Description: When the monitored build finished.
-- # Class: InTotoVulns Description: The predicate that records the result of one vulnerability scan of the subjects: the scanner, its database and the vulnerabilities it found.
--     * Slot: id
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
--     * Slot: vuln_scanner_id Description: The scanner that ran, its version and the database it used.
--     * Slot: scan_metadata_id Description: When the scan ran.
-- # Class: InTotoVulnScanner Description: The scanner a VULNS predicate records, with its results.
--     * Slot: id
--     * Slot: scanner_uri Description: The URI that identifies the scanner's source.
--     * Slot: scanner_version Description: The scanner's version.
--     * Slot: vuln_db_id Description: The vulnerability database the scanner used.
-- # Class: InTotoVulnDatabase Description: The vulnerability database a scanner used.
--     * Slot: id
--     * Slot: db_uri Description: The URI that identifies the database's source.
--     * Slot: db_version Description: The database's version.
--     * Slot: db_last_update Description: When the database was last updated.
-- # Class: InTotoVulnResult Description: One vulnerability a scanner found.
--     * Slot: id
--     * Slot: vuln_id Description: The vulnerability's identifier, such as GHSA-fxph-q3j8-mv87 or CVE-2017-5645.
--     * Slot: InTotoVulnScanner_id Description: Autocreated FK slot
-- # Class: InTotoVulnSeverity Description: One severity score of a vulnerability, by one scoring method.
--     * Slot: id
--     * Slot: severity_method Description: The scoring method, such as nvd or cvss.
--     * Slot: severity_score Description: The score under that method, as a string.
--     * Slot: InTotoVulnResult_id Description: Autocreated FK slot
-- # Class: InTotoScanMetadata Description: When a vulnerability scan ran.
--     * Slot: id
--     * Slot: scan_started_on Description: When the scan started.
--     * Slot: scan_finished_on Description: When the scan finished.
-- # Class: InTotoAnnotation_annotation_values
--     * Slot: InTotoAnnotation_id Description: Autocreated FK slot
--     * Slot: annotation_values Description: The annotation's values.
-- # Class: InTotoObjectEntry_entry_values
--     * Slot: InTotoObjectEntry_id Description: Autocreated FK slot
--     * Slot: entry_values Description: The key's values.
-- # Class: InTotoTestResult_passed_tests
--     * Slot: InTotoTestResult_id Description: Autocreated FK slot
--     * Slot: passed_tests Description: The names of the tests that passed.
-- # Class: InTotoTestResult_warned_tests
--     * Slot: InTotoTestResult_id Description: Autocreated FK slot
--     * Slot: warned_tests Description: The names of the tests that expressed a warning.
-- # Class: InTotoTestResult_failed_tests
--     * Slot: InTotoTestResult_id Description: Autocreated FK slot
--     * Slot: failed_tests Description: The names of the tests that failed.
-- # Class: InTotoSimpleVerificationResult_verified_properties
--     * Slot: InTotoSimpleVerificationResult_id Description: Autocreated FK slot
--     * Slot: verified_properties Description: The properties of the subjects that passed verification, scoped to the framework or policy verified, such as SLSA_BUILD_LEVEL_3.
-- # Class: InTotoLink_step_command
--     * Slot: InTotoLink_id Description: Autocreated FK slot
--     * Slot: step_command Description: The command the step ran, and its arguments; possibly empty.
-- # Class: InTotoMonitorLog_traced_processes
--     * Slot: InTotoMonitorLog_id Description: Autocreated FK slot
--     * Slot: traced_processes Description: The processes the monitor observed, one JSON object each, written as its JSON text, in a format monitor_type determines.
-- # Class: InTotoMonitorLog_traced_network
--     * Slot: InTotoMonitorLog_id Description: Autocreated FK slot
--     * Slot: traced_network Description: The network activity the monitor observed, one JSON object each, written as its JSON text, in a format monitor_type determines.

CREATE TABLE "InTotoDocument" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoDocument_id" ON "InTotoDocument" (id);

CREATE TABLE "InTotoDigestSet" (
	id INTEGER NOT NULL,
	sha256 TEXT,
	sha224 TEXT,
	sha384 TEXT,
	sha512 TEXT,
	sha512_224 TEXT,
	sha512_256 TEXT,
	sha3_224 TEXT,
	sha3_256 TEXT,
	sha3_384 TEXT,
	sha3_512 TEXT,
	shake128 TEXT,
	shake256 TEXT,
	blake2b TEXT,
	blake2s TEXT,
	ripemd160 TEXT,
	sm3 TEXT,
	gost TEXT,
	sha1 TEXT,
	md5 TEXT,
	dir_hash TEXT,
	git_commit TEXT,
	git_tree TEXT,
	git_blob TEXT,
	git_tag TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoDigestSet_id" ON "InTotoDigestSet" (id);

CREATE TABLE "InTotoPredicate" (
	id INTEGER NOT NULL,
	predicate_kind TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoPredicate_id" ON "InTotoPredicate" (id);

CREATE TABLE "InTotoTestResult" (
	id INTEGER NOT NULL,
	test_result VARCHAR(6) NOT NULL,
	test_run_url TEXT,
	predicate_kind TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoTestResult_id" ON "InTotoTestResult" (id);

CREATE TABLE "InTotoSvrVerifier" (
	id INTEGER NOT NULL,
	svr_verifier_id TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoSvrVerifier_id" ON "InTotoSvrVerifier" (id);

CREATE TABLE "InTotoLink" (
	id INTEGER NOT NULL,
	step_name TEXT NOT NULL,
	predicate_kind TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoLink_id" ON "InTotoLink" (id);

CREATE TABLE "InTotoReferenceAttester" (
	id INTEGER NOT NULL,
	reference_attester_id TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoReferenceAttester_id" ON "InTotoReferenceAttester" (id);

CREATE TABLE "InTotoRelease" (
	id INTEGER NOT NULL,
	release_purl TEXT NOT NULL,
	package_id TEXT,
	predicate_kind TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoRelease_id" ON "InTotoRelease" (id);

CREATE TABLE "InTotoMonitoredProcess" (
	id INTEGER NOT NULL,
	host_id TEXT NOT NULL,
	process_type TEXT NOT NULL,
	process_event TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoMonitoredProcess_id" ON "InTotoMonitoredProcess" (id);

CREATE TABLE "InTotoMonitorLog" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoMonitorLog_id" ON "InTotoMonitorLog" (id);

CREATE TABLE "InTotoTraceMetadata" (
	id INTEGER NOT NULL,
	build_started_on TEXT,
	build_finished_on TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoTraceMetadata_id" ON "InTotoTraceMetadata" (id);

CREATE TABLE "InTotoVulnDatabase" (
	id INTEGER NOT NULL,
	db_uri TEXT,
	db_version TEXT,
	db_last_update TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoVulnDatabase_id" ON "InTotoVulnDatabase" (id);

CREATE TABLE "InTotoScanMetadata" (
	id INTEGER NOT NULL,
	scan_started_on TEXT NOT NULL,
	scan_finished_on TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoScanMetadata_id" ON "InTotoScanMetadata" (id);

CREATE TABLE "InTotoAdditionalDigest" (
	id INTEGER NOT NULL,
	algorithm TEXT NOT NULL,
	value TEXT NOT NULL,
	"InTotoDigestSet_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoDigestSet_id") REFERENCES "InTotoDigestSet" (id)
);
CREATE INDEX "ix_InTotoAdditionalDigest_id" ON "InTotoAdditionalDigest" (id);

CREATE TABLE "InTotoResourceDescriptor" (
	id INTEGER NOT NULL,
	resource_uri TEXT,
	resource_name TEXT,
	download_location TEXT,
	media_type TEXT,
	content TEXT,
	"InTotoTestResult_id" INTEGER,
	"InTotoMonitorLog_id" INTEGER,
	digest_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoTestResult_id") REFERENCES "InTotoTestResult" (id),
	FOREIGN KEY("InTotoMonitorLog_id") REFERENCES "InTotoMonitorLog" (id),
	FOREIGN KEY(digest_id) REFERENCES "InTotoDigestSet" (id)
);
CREATE INDEX "ix_InTotoResourceDescriptor_id" ON "InTotoResourceDescriptor" (id);

CREATE TABLE "InTotoStatement" (
	id INTEGER NOT NULL,
	statement_type TEXT NOT NULL,
	predicate_type TEXT NOT NULL,
	"InTotoDocument_id" INTEGER,
	predicate_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoDocument_id") REFERENCES "InTotoDocument" (id),
	FOREIGN KEY(predicate_id) REFERENCES "InTotoPredicate" (id)
);
CREATE INDEX "ix_InTotoStatement_id" ON "InTotoStatement" (id);

CREATE TABLE "InTotoPredicateType" (
	id INTEGER NOT NULL,
	predicate_type_uri TEXT NOT NULL,
	predicate_version TEXT,
	predicate_specification TEXT,
	vetted_as VARCHAR(26),
	"InTotoDocument_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoDocument_id") REFERENCES "InTotoDocument" (id)
);
CREATE INDEX "ix_InTotoPredicateType_id" ON "InTotoPredicateType" (id);

CREATE TABLE "InTotoSimpleVerificationResult" (
	id INTEGER NOT NULL,
	time_created TEXT NOT NULL,
	predicate_kind TEXT,
	svr_verifier_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(svr_verifier_id) REFERENCES "InTotoSvrVerifier" (id)
);
CREATE INDEX "ix_InTotoSimpleVerificationResult_id" ON "InTotoSimpleVerificationResult" (id);

CREATE TABLE "InTotoLinkMaterial" (
	id INTEGER NOT NULL,
	resource_uri TEXT,
	resource_name TEXT,
	download_location TEXT,
	media_type TEXT,
	content TEXT,
	"InTotoLink_id" INTEGER,
	digest_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoLink_id") REFERENCES "InTotoLink" (id),
	FOREIGN KEY(digest_id) REFERENCES "InTotoDigestSet" (id)
);
CREATE INDEX "ix_InTotoLinkMaterial_id" ON "InTotoLinkMaterial" (id);

CREATE TABLE "InTotoReference" (
	id INTEGER NOT NULL,
	predicate_kind TEXT,
	reference_attester_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(reference_attester_id) REFERENCES "InTotoReferenceAttester" (id)
);
CREATE INDEX "ix_InTotoReference_id" ON "InTotoReference" (id);

CREATE TABLE "InTotoVulnScanner" (
	id INTEGER NOT NULL,
	scanner_uri TEXT NOT NULL,
	scanner_version TEXT,
	vuln_db_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(vuln_db_id) REFERENCES "InTotoVulnDatabase" (id)
);
CREATE INDEX "ix_InTotoVulnScanner_id" ON "InTotoVulnScanner" (id);

CREATE TABLE "InTotoTestResult_passed_tests" (
	"InTotoTestResult_id" INTEGER,
	passed_tests TEXT,
	PRIMARY KEY ("InTotoTestResult_id", passed_tests),
	FOREIGN KEY("InTotoTestResult_id") REFERENCES "InTotoTestResult" (id)
);
CREATE INDEX "ix_InTotoTestResult_passed_tests_InTotoTestResult_id" ON "InTotoTestResult_passed_tests" ("InTotoTestResult_id");
CREATE INDEX "ix_InTotoTestResult_passed_tests_passed_tests" ON "InTotoTestResult_passed_tests" (passed_tests);

CREATE TABLE "InTotoTestResult_warned_tests" (
	"InTotoTestResult_id" INTEGER,
	warned_tests TEXT,
	PRIMARY KEY ("InTotoTestResult_id", warned_tests),
	FOREIGN KEY("InTotoTestResult_id") REFERENCES "InTotoTestResult" (id)
);
CREATE INDEX "ix_InTotoTestResult_warned_tests_InTotoTestResult_id" ON "InTotoTestResult_warned_tests" ("InTotoTestResult_id");
CREATE INDEX "ix_InTotoTestResult_warned_tests_warned_tests" ON "InTotoTestResult_warned_tests" (warned_tests);

CREATE TABLE "InTotoTestResult_failed_tests" (
	"InTotoTestResult_id" INTEGER,
	failed_tests TEXT,
	PRIMARY KEY ("InTotoTestResult_id", failed_tests),
	FOREIGN KEY("InTotoTestResult_id") REFERENCES "InTotoTestResult" (id)
);
CREATE INDEX "ix_InTotoTestResult_failed_tests_InTotoTestResult_id" ON "InTotoTestResult_failed_tests" ("InTotoTestResult_id");
CREATE INDEX "ix_InTotoTestResult_failed_tests_failed_tests" ON "InTotoTestResult_failed_tests" (failed_tests);

CREATE TABLE "InTotoLink_step_command" (
	"InTotoLink_id" INTEGER,
	step_command TEXT,
	PRIMARY KEY ("InTotoLink_id", step_command),
	FOREIGN KEY("InTotoLink_id") REFERENCES "InTotoLink" (id)
);
CREATE INDEX "ix_InTotoLink_step_command_step_command" ON "InTotoLink_step_command" (step_command);
CREATE INDEX "ix_InTotoLink_step_command_InTotoLink_id" ON "InTotoLink_step_command" ("InTotoLink_id");

CREATE TABLE "InTotoMonitorLog_traced_processes" (
	"InTotoMonitorLog_id" INTEGER,
	traced_processes TEXT,
	PRIMARY KEY ("InTotoMonitorLog_id", traced_processes),
	FOREIGN KEY("InTotoMonitorLog_id") REFERENCES "InTotoMonitorLog" (id)
);
CREATE INDEX "ix_InTotoMonitorLog_traced_processes_traced_processes" ON "InTotoMonitorLog_traced_processes" (traced_processes);
CREATE INDEX "ix_InTotoMonitorLog_traced_processes_InTotoMonitorLog_id" ON "InTotoMonitorLog_traced_processes" ("InTotoMonitorLog_id");

CREATE TABLE "InTotoMonitorLog_traced_network" (
	"InTotoMonitorLog_id" INTEGER,
	traced_network TEXT,
	PRIMARY KEY ("InTotoMonitorLog_id", traced_network),
	FOREIGN KEY("InTotoMonitorLog_id") REFERENCES "InTotoMonitorLog" (id)
);
CREATE INDEX "ix_InTotoMonitorLog_traced_network_InTotoMonitorLog_id" ON "InTotoMonitorLog_traced_network" ("InTotoMonitorLog_id");
CREATE INDEX "ix_InTotoMonitorLog_traced_network_traced_network" ON "InTotoMonitorLog_traced_network" (traced_network);

CREATE TABLE "InTotoStatementSubject" (
	id INTEGER NOT NULL,
	resource_uri TEXT,
	resource_name TEXT,
	download_location TEXT,
	media_type TEXT,
	content TEXT,
	"InTotoStatement_id" INTEGER,
	digest_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoStatement_id") REFERENCES "InTotoStatement" (id),
	FOREIGN KEY(digest_id) REFERENCES "InTotoDigestSet" (id)
);
CREATE INDEX "ix_InTotoStatementSubject_id" ON "InTotoStatementSubject" (id);

CREATE TABLE "InTotoScaiAttributeReport" (
	id INTEGER NOT NULL,
	predicate_kind TEXT,
	scai_producer_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(scai_producer_id) REFERENCES "InTotoResourceDescriptor" (id)
);
CREATE INDEX "ix_InTotoScaiAttributeReport_id" ON "InTotoScaiAttributeReport" (id);

CREATE TABLE "InTotoReferencedDocument" (
	id INTEGER NOT NULL,
	resource_uri TEXT,
	resource_name TEXT,
	download_location TEXT,
	media_type TEXT,
	content TEXT,
	"InTotoReference_id" INTEGER,
	digest_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoReference_id") REFERENCES "InTotoReference" (id),
	FOREIGN KEY(digest_id) REFERENCES "InTotoDigestSet" (id)
);
CREATE INDEX "ix_InTotoReferencedDocument_id" ON "InTotoReferencedDocument" (id);

CREATE TABLE "InTotoTraceMonitor" (
	id INTEGER NOT NULL,
	monitor_type TEXT NOT NULL,
	monitor_config_source_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(monitor_config_source_id) REFERENCES "InTotoResourceDescriptor" (id)
);
CREATE INDEX "ix_InTotoTraceMonitor_id" ON "InTotoTraceMonitor" (id);

CREATE TABLE "InTotoVulns" (
	id INTEGER NOT NULL,
	predicate_kind TEXT,
	vuln_scanner_id INTEGER NOT NULL,
	scan_metadata_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(vuln_scanner_id) REFERENCES "InTotoVulnScanner" (id),
	FOREIGN KEY(scan_metadata_id) REFERENCES "InTotoScanMetadata" (id)
);
CREATE INDEX "ix_InTotoVulns_id" ON "InTotoVulns" (id);

CREATE TABLE "InTotoVulnResult" (
	id INTEGER NOT NULL,
	vuln_id TEXT NOT NULL,
	"InTotoVulnScanner_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoVulnScanner_id") REFERENCES "InTotoVulnScanner" (id)
);
CREATE INDEX "ix_InTotoVulnResult_id" ON "InTotoVulnResult" (id);

CREATE TABLE "InTotoSimpleVerificationResult_verified_properties" (
	"InTotoSimpleVerificationResult_id" INTEGER,
	verified_properties TEXT NOT NULL,
	PRIMARY KEY ("InTotoSimpleVerificationResult_id", verified_properties),
	FOREIGN KEY("InTotoSimpleVerificationResult_id") REFERENCES "InTotoSimpleVerificationResult" (id)
);
CREATE INDEX "ix_InTotoSimpleVerificationResult_verified_properties_verified_properties" ON "InTotoSimpleVerificationResult_verified_properties" (verified_properties);
CREATE INDEX "ix_InTotoSimpleVerificationResult_verified_properties_InTotoSimpleVerificationResult_id" ON "InTotoSimpleVerificationResult_verified_properties" ("InTotoSimpleVerificationResult_id");

CREATE TABLE "InTotoAnnotation" (
	id INTEGER NOT NULL,
	annotation_key TEXT NOT NULL,
	"InTotoResourceDescriptor_id" INTEGER,
	"InTotoStatementSubject_id" INTEGER,
	"InTotoLinkMaterial_id" INTEGER,
	"InTotoReferencedDocument_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoResourceDescriptor_id") REFERENCES "InTotoResourceDescriptor" (id),
	FOREIGN KEY("InTotoStatementSubject_id") REFERENCES "InTotoStatementSubject" (id),
	FOREIGN KEY("InTotoLinkMaterial_id") REFERENCES "InTotoLinkMaterial" (id),
	FOREIGN KEY("InTotoReferencedDocument_id") REFERENCES "InTotoReferencedDocument" (id)
);
CREATE INDEX "ix_InTotoAnnotation_id" ON "InTotoAnnotation" (id);

CREATE TABLE "InTotoScaiAttributeAssertion" (
	id INTEGER NOT NULL,
	scai_attribute TEXT NOT NULL,
	"InTotoScaiAttributeReport_id" INTEGER,
	scai_target_id INTEGER,
	scai_evidence_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoScaiAttributeReport_id") REFERENCES "InTotoScaiAttributeReport" (id),
	FOREIGN KEY(scai_target_id) REFERENCES "InTotoResourceDescriptor" (id),
	FOREIGN KEY(scai_evidence_id) REFERENCES "InTotoResourceDescriptor" (id)
);
CREATE INDEX "ix_InTotoScaiAttributeAssertion_id" ON "InTotoScaiAttributeAssertion" (id);

CREATE TABLE "InTotoRuntimeTrace" (
	id INTEGER NOT NULL,
	predicate_kind TEXT,
	trace_monitor_id INTEGER NOT NULL,
	monitored_process_id INTEGER NOT NULL,
	monitor_log_id INTEGER NOT NULL,
	trace_metadata_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(trace_monitor_id) REFERENCES "InTotoTraceMonitor" (id),
	FOREIGN KEY(monitored_process_id) REFERENCES "InTotoMonitoredProcess" (id),
	FOREIGN KEY(monitor_log_id) REFERENCES "InTotoMonitorLog" (id),
	FOREIGN KEY(trace_metadata_id) REFERENCES "InTotoTraceMetadata" (id)
);
CREATE INDEX "ix_InTotoRuntimeTrace_id" ON "InTotoRuntimeTrace" (id);

CREATE TABLE "InTotoVulnSeverity" (
	id INTEGER NOT NULL,
	severity_method TEXT NOT NULL,
	severity_score TEXT NOT NULL,
	"InTotoVulnResult_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoVulnResult_id") REFERENCES "InTotoVulnResult" (id)
);
CREATE INDEX "ix_InTotoVulnSeverity_id" ON "InTotoVulnSeverity" (id);

CREATE TABLE "InTotoObjectEntry" (
	id INTEGER NOT NULL,
	entry_key TEXT NOT NULL,
	"InTotoScaiAttributeAssertion_id" INTEGER,
	"InTotoLink_id" INTEGER,
	"InTotoTraceMonitor_id" INTEGER,
	"InTotoVulnResult_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoScaiAttributeAssertion_id") REFERENCES "InTotoScaiAttributeAssertion" (id),
	FOREIGN KEY("InTotoLink_id") REFERENCES "InTotoLink" (id),
	FOREIGN KEY("InTotoTraceMonitor_id") REFERENCES "InTotoTraceMonitor" (id),
	FOREIGN KEY("InTotoVulnResult_id") REFERENCES "InTotoVulnResult" (id)
);
CREATE INDEX "ix_InTotoObjectEntry_id" ON "InTotoObjectEntry" (id);

CREATE TABLE "InTotoAnnotation_annotation_values" (
	"InTotoAnnotation_id" INTEGER,
	annotation_values TEXT,
	PRIMARY KEY ("InTotoAnnotation_id", annotation_values),
	FOREIGN KEY("InTotoAnnotation_id") REFERENCES "InTotoAnnotation" (id)
);
CREATE INDEX "ix_InTotoAnnotation_annotation_values_annotation_values" ON "InTotoAnnotation_annotation_values" (annotation_values);
CREATE INDEX "ix_InTotoAnnotation_annotation_values_InTotoAnnotation_id" ON "InTotoAnnotation_annotation_values" ("InTotoAnnotation_id");

CREATE TABLE "InTotoObjectEntry_entry_values" (
	"InTotoObjectEntry_id" INTEGER,
	entry_values TEXT,
	PRIMARY KEY ("InTotoObjectEntry_id", entry_values),
	FOREIGN KEY("InTotoObjectEntry_id") REFERENCES "InTotoObjectEntry" (id)
);
CREATE INDEX "ix_InTotoObjectEntry_entry_values_entry_values" ON "InTotoObjectEntry_entry_values" (entry_values);
CREATE INDEX "ix_InTotoObjectEntry_entry_values_InTotoObjectEntry_id" ON "InTotoObjectEntry_entry_values" ("InTotoObjectEntry_id");
