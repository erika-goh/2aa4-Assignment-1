// --------------------------------------------------------
// Main: minimal entry point for the Catan simulator demonstrator.
//
// Design rationale:
// - Main contains NO simulation or setup logic (SRP).
// - It delegates to Simulator, which owns object creation.
// - Simulator delegates to Game, which owns round execution.
// - This two-level delegation keeps Main trivially simple and
//   means new features never require changes to this file (OCP).
// --------------------------------------------------------

package catandomainmodel;

/**
 * Demonstrator entry point for the Catan simulator.
 */
public class Demonstrator {

    public static void main(String[] args) {
        System.out.println("========================================");
        System.out.println("   Settlers of Catan – Simulator Demo   ");
        System.out.println("========================================");
        System.out.println();

        // Setup + execution fully encapsulated in Simulator
        Simulator simulator = new Simulator();
        simulator.run();

        System.out.println();
        System.out.println("========================================");
        System.out.println("          Simulation Complete            ");
        System.out.println("========================================");
    }
}
