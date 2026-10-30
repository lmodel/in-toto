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
  The process a runtime trace watched.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoMonitoredProcess  {

  private URI hostId;
  private URI processType;
  private String processEvent;


}