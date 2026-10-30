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
  The predicate that records what a monitor traced while a supply chain step, such as a build, ran.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoRuntimeTrace extends InTotoPredicate {

  private InTotoTraceMonitor traceMonitor;
  private InTotoMonitoredProcess monitoredProcess;
  private InTotoMonitorLog monitorLog;
  private InTotoTraceMetadata traceMetadata;


}