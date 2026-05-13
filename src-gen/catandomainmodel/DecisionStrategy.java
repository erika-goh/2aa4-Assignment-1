package catandomainmodel;

/**
 * Strategy interface for machine decision-making.
 * Defines how an agent chooses an action based on the game state.
 */
public interface DecisionStrategy {
    /**
     * Chooses the best action for the given player.
     * 
     * @param state the read-only game state view
     * @return the chosen Action, or null if no action is possible/chosen
     */
    Action chooseAction(GameState state);
}
