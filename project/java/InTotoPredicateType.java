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
  A type of predicate an in-toto statement can carry, named by the URI a statement's predicate_type holds.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoPredicateType  {

  private URI predicateTypeUri;
  private String predicateVersion;
  private URI predicateSpecification;
  private String vettedAs;


}