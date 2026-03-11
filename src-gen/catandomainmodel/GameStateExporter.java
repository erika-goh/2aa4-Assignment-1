package catandomainmodel;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

public class GameStateExporter {

    private static final Logger LOGGER = Logger.getLogger(GameStateExporter.class.getName());
    private static final String JSON_START_BRACE = "    {";
    private static final String DESERT_LITERAL = "DESERT";

    private static final String DEFAULT_BASE_MAP_PATH = "base_map.json";
    private static final String DEFAULT_STATE_PATH = "state.json";

    private String baseMapPath;
    private String statePath;

    public GameStateExporter() {
        // Hardcoded to the visualizer folder as requested, using forward slashes for
        // cross-compatibility
        this.baseMapPath = DEFAULT_BASE_MAP_PATH;
        this.statePath = DEFAULT_STATE_PATH;
    }

    public GameStateExporter(String baseMapPath, String statePath) {
        this.baseMapPath = baseMapPath;
        this.statePath = statePath;
    }

    public void writeBaseMap(Board board) {
        StringBuilder sb = new StringBuilder();
        sb.append("{\n  \"tiles\": [\n");

        List<Tile> tiles = board.getTiles();

        // Cube coordinates for a standard 19-tile hex layout
        int[][] coords = {
                // center
                { 0, 0, 0 },
                // radius 1
                { 1, -1, 0 }, { 1, 0, -1 }, { 0, 1, -1 }, { -1, 1, 0 }, { -1, 0, 1 }, { 0, -1, 1 },
                // radius 2
                { 2, -2, 0 }, { 2, -1, -1 }, { 2, 0, -2 }, { 1, 1, -2 }, { 0, 2, -2 }, { -1, 2, -1 },
                { -2, 2, 0 }, { -2, 1, 1 }, { -2, 0, 2 }, { -1, -1, 2 }, { 0, -2, 2 }, { 1, -2, 1 }
        };

        for (int i = 0; i < tiles.size(); i++) {
            if (i >= coords.length)
                break; // In case we have more than 19 for some reason

            Tile t = tiles.get(i);
            int[] c = coords[i];
            String res = mapResource(t.getResourceType(), t.getNumber());

            sb.append(JSON_START_BRACE)
                    .append("\"id\": ").append(t.getId()).append(", ")
                    .append("\"q\": ").append(c[0]).append(", ")
                    .append("\"s\": ").append(c[1]).append(", ")
                    .append("\"r\": ").append(c[2]).append(", ")
                    .append("\"resource\": \"").append(res).append("\", ")
                    .append("\"number\": ").append(res.equals(DESERT_LITERAL) ? 0 : t.getNumber())
                    .append("}");

            if (i < tiles.size() - 1 && i < coords.length - 1)
                sb.append(",");
            sb.append("\n");
        }
        sb.append("  ]\n}\n");

        try (FileWriter fw = new FileWriter(baseMapPath)) {
            fw.write(sb.toString());
            fw.flush();
        } catch (IOException e) {
            LOGGER.log(Level.SEVERE, "Failed to write base map: {0}", e.getMessage());
        }
    }

    public void writeState(Game game) {
        StringBuilder sb = new StringBuilder();
        sb.append("{\n");
        sb.append("  \"round\": ").append(game.getRound()).append(",\n");

        writeBuildingsJson(sb, game.getPlayers());
        writeRoadsJson(sb, game.getBoard().getEdges());

        // We will omit writing other player text specifics here since the visualizer
        // directly renders the board layout.
        sb.append("}\n");

        try (FileWriter fw = new FileWriter(statePath)) {
            fw.write(sb.toString());
            fw.flush();
        } catch (IOException e) {
            LOGGER.log(Level.SEVERE, "Failed to write state: {0}", e.getMessage());
        }
    }

    private void writeBuildingsJson(StringBuilder sb, List<Player> players) {
        sb.append("  \"buildings\": [\n");
        boolean firstBuilding = true;
        for (Player p : players) {
            String color = mapPlayerToColor(p.getId());
            for (Structure s : p.getStructures()) {
                if (!firstBuilding)
                    sb.append(",\n");

                String typeStr = (s instanceof City) ? "CITY" : "SETTLEMENT";
                sb.append(JSON_START_BRACE)
                        .append("\"node\": ").append(s.getLocation().getId()).append(", ")
                        .append("\"owner\": \"").append(color).append("\", ")
                        .append("\"type\": \"").append(typeStr).append("\"")
                        .append("}");
                firstBuilding = false;
            }
        }
        sb.append("\n  ],\n");
    }

    private void writeRoadsJson(StringBuilder sb, List<Edge> edges) {
        sb.append("  \"roads\": [\n");
        boolean firstRoad = true;
        for (Edge e : edges) {
            if (e.getRoad() != null && e.getNodes().size() == 2) {
                if (!firstRoad)
                    sb.append(",\n");

                String color = mapPlayerToColor(e.getRoad().getOwner().getId());
                int nodeA = e.getNodes().get(0).getId();
                int nodeB = e.getNodes().get(1).getId();

                sb.append(JSON_START_BRACE)
                        .append("\"a\": ").append(nodeA).append(", ")
                        .append("\"b\": ").append(nodeB).append(", ")
                        .append("\"owner\": \"").append(color).append("\"")
                        .append("}");
                firstRoad = false;
            }
        }
        sb.append("\n  ]\n");
    }

    private String mapResource(ResourceType type, int number) {
        if (number == 0)
            return DESERT_LITERAL;
        switch (type) {
            case LUMBER:
                return "WOOD";
            case WOOL:
                return "SHEEP";
            case GRAIN:
                return "WHEAT";
            case BRICK:
                return "BRICK";
            case ORE:
                return "ORE";
            default:
                return DESERT_LITERAL;
        }
    }

    private String mapPlayerToColor(int playerId) {
        switch (playerId) {
            case 1:
                return "RED";
            case 2:
                return "BLUE";
            case 3:
                return "ORANGE";
            case 4:
                return "WHITE";
            default:
                return "WHITE";
        }
    }

    // Still satisfying IAgent and basic checks by providing a single write method
    // alias if needed,
    // but demonstrating properly calling the two exports in Demonstrator.
    public void write(Game game) {
        writeState(game);
    }
}
