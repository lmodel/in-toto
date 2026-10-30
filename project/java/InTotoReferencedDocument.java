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
  One document a Reference predicate points to: a resource descriptor with a download location and a media type.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoReferencedDocument extends InTotoResourceDescriptor {



}