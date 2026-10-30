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
  The scanner a VULNS predicate records, with its results.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoVulnScanner  {

  private URI scannerUri;
  private String scannerVersion;
  private InTotoVulnDatabase vulnDb;
  private List<InTotoVulnResult> scanResults;


}