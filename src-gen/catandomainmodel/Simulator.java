// --------------------------------------------------------
// Simulator: encapsulates setup and execution of a Catan game.
//
// SOLID Justification:
// - SRP: Simulator handles ONLY game setup and delegation.
//        It does not contain simulation logic (that lives in Game/Agent).
// - OCP: Simulator delegates to Game.startGame() without modifying
//        or overriding core behaviour. New features (e.g. different
//        board layouts) can be added via new factory methods or
//        subclasses without changing existing code.
// - Encapsulation: Simulator never manipulates internal game state
//        directly; it uses only public constructors and methods.
// --------------------------------------------------------

package catandomainmodel;

import java.util.ArrayList;
import java.util.List;

/**
 * Encapsulates the creation and execution of a Catan simulation.
 * Main delegates to this class so the entry point stays minimal.
 */
public class Simulator {

    private static final int NUM_PLAYERS = 4;

    private Game game;

    /**
     * Creates a Simulator with a default board configuration
     * and the standard number of players (4).
     */
    public Simulator() {
        Board board = createBoard();
        List<Player> players = createPlayers();
        this.game = new Game(board, players);
    }

    /**
     * Runs the simulation from start to termination.
     * Delegates entirely to Game.startGame(), which handles
     * round progression, agent turns, and winner announcement.
     */
    public void run() {
        game.startGame();
    }

    // ---- Private factory helpers (setup only) ----

    /**
     * Creates a minimal board with empty tile/node/edge lists.
     * A real implementation would populate these from a config file.
     */
    private Board createBoard() {
        List<Tile> tiles = new ArrayList<>();
        List<Node> nodes = new ArrayList<>();
        List<Edge> edges = new ArrayList<>();
        return new Board(tiles, nodes, edges);
    }

    /**
     * Creates NUM_PLAYERS players with sequential IDs starting at 1.
     */
    private List<Player> createPlayers() {
        List<Player> players = new ArrayList<>();
        for (int i = 1; i <= NUM_PLAYERS; i++) {
            players.add(new Player(i));
        }
        return players;
    }
}
