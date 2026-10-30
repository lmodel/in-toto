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
  The predicate that records the result of one run of a test suite against the subjects, with the names of the tests that passed, warned and failed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoTestResult extends InTotoPredicate {

  private String testResult;
  private List<InTotoResourceDescriptor> configuration;
  private URI testRunUrl;
  private List<String> passedTests;
  private List<String> warnedTests;
  private List<String> failedTests;


}