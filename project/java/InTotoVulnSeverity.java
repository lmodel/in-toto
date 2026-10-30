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
  One severity score of a vulnerability, by one scoring method.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoVulnSeverity  {

  private String severityMethod;
  private String severityScore;


}