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
  When a vulnerability scan ran.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoScanMetadata  {

  private ZonedDateTime scanStartedOn;
  private ZonedDateTime scanFinishedOn;


}