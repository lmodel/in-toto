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
  The Software Supply Chain Attribute Integrity (SCAI) predicate: assertions about functional attributes of the subjects or their producer, each with the evidence for it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoScaiAttributeReport extends InTotoPredicate {

  private List<InTotoScaiAttributeAssertion> scaiAttributes;
  private InTotoResourceDescriptor scaiProducer;


}