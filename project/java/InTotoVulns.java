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
  The predicate that records the result of one vulnerability scan of the subjects: the scanner, its database and the vulnerabilities it found.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoVulns extends InTotoPredicate {

  private InTotoVulnScanner vulnScanner;
  private InTotoScanMetadata scanMetadata;


}