package catandomainmodel;

/**
 * A read-only view of the game state for AI agents to use.
 * Exposes only the necessary information for decision making
 * to preserve encapsulation.
 */
public class GameState {
    private final Game game;
    private final Player currentAgentPlayer;

    public GameState(Game game, Player currentAgentPlayer) {
        this.game = game;
        this.currentAgentPlayer = currentAgentPlayer;
    }

    public Board getBoard() {
        return game.getBoard();
    }

    public int getRound() {
        return game.getRound();
    }

    public Player getLongestRoadHolder() {
        return game.getLongestRoadHolder();
    }

    public java.util.List<Player> getPlayers() {
        return java.util.Collections.unmodifiableList(game.getPlayers());
    }

    public Player getCurrentAgentPlayer() {
        return currentAgentPlayer;
    }
}
