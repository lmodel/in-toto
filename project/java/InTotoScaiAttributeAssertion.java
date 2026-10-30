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
  One SCAI assertion: an attribute of the subject or its producer, what it applies to, under which conditions, and the evidence for it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoScaiAttributeAssertion  {

  private String scaiAttribute;
  private InTotoResourceDescriptor scaiTarget;
  private List<InTotoObjectEntry> scaiConditions;
  private InTotoResourceDescriptor scaiEvidence;


}