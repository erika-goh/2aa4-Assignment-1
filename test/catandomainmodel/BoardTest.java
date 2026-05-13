package catandomainmodel;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

class BoardTest {
    private Board board;
    private Player player;

    @BeforeEach
    void setUp() {
        player = new Player(1);
        Node n0 = new Node(0);
        Node n1 = new Node(1);
        Edge e = new Edge(0);
        e.addNode(n0);
        e.addNode(n1);
        board = new Board(List.of(new Tile(0, catandomainmodel.ResourceType.WOOL, 5)), List.of(n0, n1), List.of(e));
    }

    @Test
    void testBasicLookups() {
        org.junit.jupiter.api.Assertions.assertNotNull(board.getTile(0));
        board.getTile(-1);
        board.getNode(0);
        board.getNode(-1);
        board.getEdge(0);
        board.getEdge(-1);
    }

    @Test
    void testAdjacencyAndPlacement() {
        Node n0 = board.getNode(0);
        org.junit.jupiter.api.Assertions.assertNotNull(n0);
        Node n1 = board.getNode(1);
        Edge e0 = board.getEdge(0);

        board.getAdjacentNodes(n0);
        board.getAdjacentEdges(n0);

        board.isValidSettlementPlacement(n0, player);
        board.isValidSetupSettlementPlacement(n0, player);
        board.isValidCityPlacement(n0, player);
        board.isValidRoadPlacement(e0, player);

        Settlement s = new Settlement(player, n0);
        n0.setStructure(s);
        board.hasAdjacentStructures(n1);

        board.isValidSettlementPlacement(n1, player);
        board.isValidSetupSettlementPlacement(n1, player);
        board.isValidCityPlacement(n0, player);

        board.getLongestRoadLength(player);
        board.getConnectingRoadCandidate(player);
    }
}
