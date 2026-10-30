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
  One vulnerability a scanner found.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoVulnResult  {

  private String vulnId;
  private List<InTotoVulnSeverity> vulnSeverity;
  private List<InTotoObjectEntry> vulnAnnotations;


}