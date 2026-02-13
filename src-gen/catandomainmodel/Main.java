package catandomainmodel;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        System.out.println("=== Catan Simulator Started ===");

        // Minimal board for scaffold (will be populated later)
        List<Tile> tiles = new ArrayList<>();
        List<Node> nodes = new ArrayList<>();
        List<Edge> edges = new ArrayList<>();
        Board board = new Board(tiles, nodes, edges);

        // Create 4 players (may need adjusting depending on Player constructor)
        List<Player> players = new ArrayList<>();
        for (int i = 1; i <= 4; i++) {
            players.add(new Player(i));
        }

        Game game = new Game(board, players);
        game.startGame();

        System.out.println("=== Simulation Finished ===");
    }
}
