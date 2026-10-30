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
  The events a runtime trace's monitor recorded: processes, network activity and file accesses, at least one of them.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoMonitorLog  {

  private List<String> tracedProcesses;
  private List<String> tracedNetwork;
  private List<InTotoResourceDescriptor> fileAccess;


}