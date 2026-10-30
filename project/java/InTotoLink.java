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
  The predicate that records one step of an in-toto layout: the command it ran and the materials it read, for a supply chain that migrates from in-toto 0.9 links.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoLink extends InTotoPredicate {

  private String stepName;
  private List<String> stepCommand;
  private List<InTotoLinkMaterial> materials;
  private List<InTotoObjectEntry> stepByproducts;
  private List<InTotoObjectEntry> stepEnvironment;


}