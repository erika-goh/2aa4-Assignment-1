package catandomainmodel;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

class AgentTest {

    private Agent agent;
    private Player player;

    @BeforeEach
    void setUp() {
        player = new Player(1);
        agent = new Agent(player);

        List<Tile> tiles = Demonstrator.createTiles();
        List<Node> nodes = Demonstrator.createNodes();
        Demonstrator.mapNodesToTiles(tiles, nodes);
        List<Edge> edges = Demonstrator.createEdges(nodes);
        new Board(tiles, nodes, edges);
    }

    @Test
    void testChooseRandomActionNullOrEmpty() {
        assertNull(agent.chooseRandomAction(null));
        assertNull(agent.chooseRandomAction(List.of()));
    }

    @Test
    void testChooseRandomActionWithItems() {
        Action a1 = new Action(1, 1, "TEST 1", ActionType.PASS);
        Action a2 = new Action(1, 1, "TEST 2", ActionType.PASS);
        Action chosen = agent.chooseRandomAction(List.of(a1, a2));
        assertNotNull(chosen);
        assertTrue(chosen == a1 || chosen == a2);
    }

    @Test
    void testMakeDecision() {
        Action action = agent.makeDecision();
        assertNotNull(action);
        assertEquals(ActionType.PASS, action.getActionType());
    }

    @Test
    void testRollDice() {
        int roll = agent.rollDice();
        assertTrue(roll >= 2 && roll <= 12);
    }

    @Test
    void testSetStrategy() {
        DecisionStrategy newStrategy = new RuleBasedDecisionStrategy();
        agent.setStrategy(newStrategy);
        assertNotNull(agent.getPlayer());
    }
}
