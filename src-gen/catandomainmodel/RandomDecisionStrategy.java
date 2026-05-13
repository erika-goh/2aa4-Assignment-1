package catandomainmodel;

import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * A machine decision strategy that picks a random legal action.
 */
public class RandomDecisionStrategy implements DecisionStrategy {
    private Random random = new SecureRandom();

    @Override
    public Action chooseAction(GameState state) {
        Board board = state.getBoard();
        Player player = state.getCurrentAgentPlayer();
        int round = state.getRound();
        List<Action> availableActions = new ArrayList<>();

        // Check for legal settlements
        for (Node n : board.getNodes()) {
            if (board.isValidSettlementPlacement(n, player)) {
                availableActions.add(new Action(round, player.getId(), "BUILD_SETTLEMENT " + n.getId(),
                        ActionType.BUILD_SETTLEMENT));
            }
        }

        // Check for legal cities
        for (Node n : board.getNodes()) {
            if (board.isValidCityPlacement(n, player)) {
                availableActions
                        .add(new Action(round, player.getId(), "BUILD_CITY " + n.getId(), ActionType.BUILD_CITY));
            }
        }

        // Check for legal roads
        for (Edge e : board.getEdges()) {
            if (board.isValidRoadPlacement(e, player) && e.getNodes().size() == 2) {
                int n1 = e.getNodes().get(0).getId();
                int n2 = e.getNodes().get(1).getId();
                availableActions.add(
                        new Action(round, player.getId(), "BUILD_ROAD " + n1 + " " + n2, ActionType.BUILD_ROAD));
            }
        }

        // Pass is always an option
        availableActions.add(new Action(round, player.getId(), "PASS", ActionType.PASS));

        if (availableActions.isEmpty()) {
            return null;
        }

        return availableActions.get(random.nextInt(availableActions.size()));
    }
}
