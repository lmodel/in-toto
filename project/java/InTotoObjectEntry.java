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
  One key of a JSON object whose keys the framework leaves to the producer, and the key's values.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoObjectEntry  {

  private String entryKey;
  private List<String> entryValues;


}