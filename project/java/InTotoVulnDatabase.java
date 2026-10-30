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
  The vulnerability database a scanner used.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoVulnDatabase  {

  private URI dbUri;
  private String dbVersion;
  private ZonedDateTime dbLastUpdate;


}