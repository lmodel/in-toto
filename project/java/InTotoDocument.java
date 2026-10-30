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
  A document that holds in-toto statements and the predicate types they name.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoDocument  {

  private List<InTotoStatement> inTotoStatements;
  private List<InTotoPredicateType> inTotoPredicateTypes;


}