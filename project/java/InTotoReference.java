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
  The predicate that points from the subjects, as a whole, to documents about them, such as a bill of materials.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoReference extends InTotoPredicate {

  private InTotoReferenceAttester referenceAttester;
  private List<InTotoReferencedDocument> referencedDocuments;


}