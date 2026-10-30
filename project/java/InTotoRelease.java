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
  The predicate that ties the subjects to one release name and version of a package, so that consumers can check what the release should contain.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoRelease extends InTotoPredicate {

  private URI releasePurl;
  private String packageId;


}