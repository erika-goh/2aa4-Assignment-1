package catandomainmodel;

import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.Collections;
import java.util.EnumMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * R3.2 Rule-based machine intelligence.
 * Evaluates legal actions based on immediate value and chooses the best.
 */
public class RuleBasedDecisionStrategy implements DecisionStrategy {
    private static final Logger LOGGER = Logger.getLogger(RuleBasedDecisionStrategy.class.getName());
    private Random random = new SecureRandom();

    private static final Map<ResourceType, Integer> SETTLEMENT_COST = new EnumMap<>(ResourceType.class);
    private static final Map<ResourceType, Integer> CITY_COST = new EnumMap<>(ResourceType.class);
    private static final Map<ResourceType, Integer> ROAD_COST = new EnumMap<>(ResourceType.class);

    static {
        SETTLEMENT_COST.put(ResourceType.BRICK, 1);
        SETTLEMENT_COST.put(ResourceType.LUMBER, 1);
        SETTLEMENT_COST.put(ResourceType.WOOL, 1);
        SETTLEMENT_COST.put(ResourceType.GRAIN, 1);

        CITY_COST.put(ResourceType.ORE, 3);
        CITY_COST.put(ResourceType.GRAIN, 2);

        ROAD_COST.put(ResourceType.BRICK, 1);
        ROAD_COST.put(ResourceType.LUMBER, 1);
    }

    @Override
    public Action chooseAction(GameState state) {
        Board board = state.getBoard();
        Player player = state.getCurrentAgentPlayer();
        int round = state.getRound();

        LOGGER.log(Level.INFO, "--- Player {0} Decision (Round {1}) ---", new Object[] { player.getId(), round });
        LOGGER.log(Level.INFO, "    Resources: {0}", player.getResourceHand().toString());

        // R3.3 Priorities (Priority Checks before scoring)
        Action priorityAction = checkPriorityConstraints(state);
        if (priorityAction != null) {
            LOGGER.log(Level.INFO, "    R3.3 Priority Constraint Triggered: {0}", priorityAction.getActionType());
            LOGGER.log(Level.INFO, "    Chosen Action: {0}", priorityAction);
            return priorityAction;
        }

        List<ScoredAction> candidates = new ArrayList<>();
        ResourceHand hand = player.getResourceHand();

        // Gather all legal actions and score them per R3.2:
        // VP gain (settlement/city) = 1.0 -- always, never downgraded
        // Non-VP build (road) = 0.8 -- or 0.5 if hand drops below 5
        // Economy spend = 0.5 -- road that leaves < 5 cards in hand

        // 1. Settlements (VP Gain = 1.0, never downgraded)
        if (hand.canAfford(SETTLEMENT_COST)) {
            for (Node n : board.getNodes()) {
                if (board.isValidSettlementPlacement(n, player)) {
                    candidates.add(new ScoredAction(
                            new Action(round, player.getId(), "BUILD_SETTLEMENT " + n.getId(),
                                    ActionType.BUILD_SETTLEMENT),
                            1.0));
                }
            }
        }

        // 2. Cities (VP Gain = 1.0, never downgraded)
        if (hand.canAfford(CITY_COST)) {
            for (Node n : board.getNodes()) {
                if (board.isValidCityPlacement(n, player)) {
                    candidates.add(new ScoredAction(
                            new Action(round, player.getId(), "BUILD_CITY " + n.getId(), ActionType.BUILD_CITY),
                            1.0));
                }
            }
        }

        // 3. Roads: start at 0.8; downgrade to 0.5 if building it leaves fewer than 5
        // cards.
        // Economy rule (R3.2) only applies here — roads do not earn VP.
        if (hand.canAfford(ROAD_COST)) {
            for (Edge e : board.getEdges()) {
                if (board.isValidRoadPlacement(e, player)) {
                    if (e.getNodes().size() == 2) {
                        int n1 = e.getNodes().get(0).getId();
                        int n2 = e.getNodes().get(1).getId();
                        Action roadAction = new Action(round, player.getId(), "BUILD_ROAD " + n1 + " " + n2,
                                ActionType.BUILD_ROAD);
                        double roadScore = leavesFewerThanFiveCards(player, roadAction) ? 0.5 : 0.8;
                        candidates.add(new ScoredAction(roadAction, roadScore));
                    }
                }
            }
        }

        if (candidates.isEmpty()) {
            LOGGER.info("    No legal build actions found.");
            Action pass = new Action(round, player.getId(), "PASS", ActionType.PASS);
            LOGGER.log(Level.INFO, "    Chosen Action: {0}", pass);
            return pass;
        }

        LOGGER.info("    Candidate Actions:");
        for (ScoredAction sa : candidates) {
            LOGGER.log(Level.INFO, "      - {0} | Score: {1}", new Object[] { sa.action, sa.score });
        }

        // Choose best
        double maxScore = -1.0;
        for (ScoredAction sa : candidates) {
            if (sa.score > maxScore) {
                maxScore = sa.score;
            }
        }

        List<Action> bestActions = new ArrayList<>();
        for (ScoredAction sa : candidates) {
            if (Math.abs(sa.score - maxScore) < 0.0001) {
                bestActions.add(sa.action);
            }
        }

        Collections.shuffle(bestActions, random);
        Action finalAction = bestActions.get(0);
        LOGGER.log(Level.INFO, "    Chosen Action: {0}", finalAction);
        return finalAction;
    }

    private Action checkPriorityConstraints(GameState state) {
        // R3.3 Priorities

        Player player = state.getCurrentAgentPlayer();

        // 1. More than 7 cards -> must spend
        if (player.getResourceHand().getTotalCards() > 7) {
            // Find any build action to lower card count
            Action a = findAnyBuildAction(state);
            if (a != null)
                return a;
        }

        // 2. Road segments within two units -> try to connect
        Action roadConn = findConnectingRoadAction(state);
        if (roadConn != null)
            return roadConn;

        // 3. Longest road threatened -> buy connected road
        Action defensiveRoad = findDefensiveRoadAction(state);
        if (defensiveRoad != null)
            return defensiveRoad;

        return null; // No priority constraint triggered
    }

    private Action findAnyBuildAction(GameState state) {
        // Simplified: just return the first legal build action found
        // This is triggered if player has > 7 cards.
        Board board = state.getBoard();
        Player player = state.getCurrentAgentPlayer();
        ResourceHand hand = player.getResourceHand();
        int round = state.getRound();

        if (hand.canAfford(SETTLEMENT_COST)) {
            for (Node n : board.getNodes()) {
                if (board.isValidSettlementPlacement(n, player)) {
                    return new Action(round, player.getId(), "BUILD_SETTLEMENT " + n.getId(),
                            ActionType.BUILD_SETTLEMENT);
                }
            }
        }
        if (hand.canAfford(CITY_COST)) {
            for (Node n : board.getNodes()) {
                if (board.isValidCityPlacement(n, player)) {
                    return new Action(round, player.getId(), "BUILD_CITY " + n.getId(), ActionType.BUILD_CITY);
                }
            }
        }
        if (hand.canAfford(ROAD_COST)) {
            for (Edge e : board.getEdges()) {
                if (board.isValidRoadPlacement(e, player)) {
                    int n1 = e.getNodes().get(0).getId();
                    int n2 = e.getNodes().get(1).getId();
                    return new Action(round, player.getId(), "BUILD_ROAD " + n1 + " " + n2, ActionType.BUILD_ROAD);
                }
            }
        }
        return null;
    }

    private Action findConnectingRoadAction(GameState state) {
        // R3.3.2: Connect segments within two units
        Board board = state.getBoard();
        Player player = state.getCurrentAgentPlayer();
        Edge candidate = board.getConnectingRoadCandidate(player);
        if (candidate != null && player.getResourceHand().canAfford(ROAD_COST)) {
            int n1 = candidate.getNodes().get(0).getId();
            int n2 = candidate.getNodes().get(1).getId();
            return new Action(state.getRound(), player.getId(), "BUILD_ROAD " + n1 + " " + n2, ActionType.BUILD_ROAD);
        }
        return null;
    }

    private Action findDefensiveRoadAction(GameState state) {
        // R3.3.3: Defence of Longest Road
        Player player = state.getCurrentAgentPlayer();
        Player holder = state.getLongestRoadHolder();
        // If we do not currently hold the Longest Road, we cannot defend it here
        if (holder == null || holder.getId() != player.getId())
            return null;

        Board board = state.getBoard();
        int myLength = board.getLongestRoadLength(player);

        boolean isThreatened = false;
        for (Player other : state.getPlayers()) {
            if (other.getId() == player.getId())
                continue;
            int otherLength = board.getLongestRoadLength(other);

            // If another player is within 1 road of exceeding our length
            if (otherLength >= myLength - 1) {
                isThreatened = true;
                break;
            }
        }

        if (isThreatened) {
            // Try to build any road to extend lead
            for (Edge e : board.getEdges()) {
                if (board.isValidRoadPlacement(e, player) && player.getResourceHand().canAfford(ROAD_COST)) {
                    int n1 = e.getNodes().get(0).getId();
                    int n2 = e.getNodes().get(1).getId();
                    return new Action(state.getRound(), player.getId(), "BUILD_ROAD " + n1 + " " + n2,
                            ActionType.BUILD_ROAD);
                }
            }
        }
        return null;
    }

    private boolean leavesFewerThanFiveCards(Player player, Action action) {
        int cost = 0;
        switch (action.getActionType()) {
            case BUILD_SETTLEMENT:
                cost = 4;
                break;
            case BUILD_CITY:
                cost = 5;
                break;
            case BUILD_ROAD:
                cost = 2;
                break;
            default:
                break;
        }
        int remaining = player.getResourceHand().getTotalCards() - cost;
        return remaining < 5;
    }

    private static class ScoredAction {
        Action action;
        double score;

        ScoredAction(Action action, double score) {
            this.action = action;
            this.score = score;
        }
    }
}
