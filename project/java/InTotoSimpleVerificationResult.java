package example;

/* metamodel_version: 1.12.0 */
/* version: 1.2.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The predicate that says a verifier evaluated the subjects against one or more policies, and which properties passed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoSimpleVerificationResult extends InTotoPredicate {

  private InTotoSvrVerifier svrVerifier;
  private ZonedDateTime timeCreated;
  private List<String> verifiedProperties;


}