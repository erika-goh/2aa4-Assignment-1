package catanutils;

import catandomainmodel.*;
import java.util.List;

public class VerifyExport {
    public static void main(String[] args) {
        List<Tile> tiles = Demonstrator.createTiles();
        List<Node> nodes = Demonstrator.createNodes();
        Demonstrator.mapNodesToTiles(tiles, nodes);
        List<Edge> edges = Demonstrator.createEdges(nodes);
        Board board = new Board(tiles, nodes, edges);
        Player p4 = new Player(4); // White
        Game game = new Game(board, List.of(new Player(1), new Player(2), new Player(3), p4), List.of());

        // Build at various nodes to see where they land in JSON
        int[] testNodes = { 13, 14, 15, 0, 5 };
        for (int id : testNodes) {
            Node n = board.getNode(id);
            if (n != null) {
                new BuildSettlementCommand(p4, n, game.getResourceBank()).execute();
            }
        }

        // Force road 14-15 if we can find it
        for (Edge e : board.getEdges()) {
            List<Node> eNodes = e.getNodes();
            if (eNodes.size() == 2) {
                int id1 = eNodes.get(0).getId();
                int id2 = eNodes.get(1).getId();
                if ((id1 == 14 && id2 == 15) || (id1 == 15 && id2 == 14)) {
                    new BuildRoadCommand(p4, e, game.getResourceBank()).execute();
                }
            }
        }

        game.getGameStateExporter().writeState(game);
        System.out.println("Done testing IDs.");
    }
}
