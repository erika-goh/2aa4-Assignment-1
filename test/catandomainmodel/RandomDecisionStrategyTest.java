package catandomainmodel;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.List;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

class RandomDecisionStrategyTest {

    private Game game;
    private Player player;
    private RandomDecisionStrategy strategy;

    @BeforeEach
    void setUp() {
        player = new Player(1);

        List<Tile> tiles = Demonstrator.createTiles();
        List<Node> nodes = Demonstrator.createNodes();
        Demonstrator.mapNodesToTiles(tiles, nodes);
        List<Edge> edges = Demonstrator.createEdges(nodes);
        Board board = new Board(tiles, nodes, edges);

        game = new Game(board, List.of(player), List.of(new Agent(player)));
        strategy = new RandomDecisionStrategy();
    }

    @Test
    void testChooseActionWithNoResources() {
        GameState state = new GameState(game, player);
        Action action = strategy.chooseAction(state);
        assertNotNull(action);
    }

    @Test
    void testChooseActionWithResources() {
        // Give player resources to unlock more random options
        player.getResourceHand().add(ResourceType.WOOL, 5);
        player.getResourceHand().add(ResourceType.BRICK, 5);
        player.getResourceHand().add(ResourceType.LUMBER, 5);
        player.getResourceHand().add(ResourceType.GRAIN, 5);
        player.getResourceHand().add(ResourceType.ORE, 5);

        // Seed board with initial placements so actions are actually valid
        Board board = game.getBoard();
        Node n0 = board.getNode(0);
        Node n1 = board.getAdjacentNodes(n0).get(0);

        // Settlement at n0 to allow city upgrades
        n0.setStructure(new Settlement(player, n0));

        // Connect road n0-n1 to allow settlement at n1 and road extensions
        Edge e01 = board.getEdges().stream().filter(e -> e.getNodes().contains(n0) && e.getNodes().contains(n1))
                .findFirst().orElse(null);
        if (e01 != null)
            e01.setRoad(new Road(player, e01));

        GameState state = new GameState(game, player);

        for (int i = 0; i < 10; i++) {
            Action action = strategy.chooseAction(state);
            assertNotNull(action);
            assertTrue(
                    action.getActionType() == ActionType.PASS ||
                            action.getActionType() == ActionType.BUILD_SETTLEMENT ||
                            action.getActionType() == ActionType.BUILD_CITY ||
                            action.getActionType() == ActionType.BUILD_ROAD);
        }
    }
}
