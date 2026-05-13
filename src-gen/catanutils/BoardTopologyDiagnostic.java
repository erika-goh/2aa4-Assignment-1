package catanutils;

import java.util.Set;
import java.util.TreeSet;

public class BoardTopologyDiagnostic {

    public static void main(String[] args) {
        // T, TR, BR, B, BL, TL
        int[][] mapping = {
                { 5, 0, 1, 2, 3, 4 }, // Tile 0: Wood 10 (Center)
                { 1, 6, 7, 8, 9, 2 }, // Tile 1: Wheat 11
                { 3, 2, 9, 10, 11, 12 }, // Tile 2: Brick 8
                { 15, 4, 3, 12, 13, 14 }, // Tile 3: Ore 3
                { 18, 16, 5, 4, 15, 17 }, // Tile 4: Sheep 11
                { 21, 19, 20, 0, 5, 16 }, // Tile 5: Sheep 5
                { 20, 22, 23, 6, 1, 0 }, // Tile 6: Sheep 12
                { 7, 24, 25, 26, 27, 8 }, // Tile 7: Wheat 3
                { 9, 8, 27, 28, 29, 10 }, // Tile 8: Ore 6
                { 11, 10, 29, 30, 31, 32 }, // Tile 9: Wood 4
                { 13, 12, 11, 32, 33, 34 }, // Tile 10: Ore 6
                { 37, 14, 13, 34, 35, 36 }, // Tile 11: Wheat 9
                { 39, 17, 15, 14, 37, 38 }, // Tile 12: Wood 5
                { 42, 40, 18, 17, 39, 41 }, // Tile 13: Brick 9
                { 44, 43, 21, 16, 18, 40 }, // Tile 14: Brick 8
                { 45, 47, 46, 19, 21, 43 }, // Tile 15: Wheat 4
                { 46, 48, 49, 22, 20, 19 }, // Tile 16: Desert
                { 49, 50, 51, 52, 23, 22 }, // Tile 17: Wood 2
                { 23, 52, 53, 24, 7, 6 } // Tile 18: Sheep 10
        };

        System.out.println("TILE NODES DIAGNOSTIC (Clockwise: T, TR, BR, B, BL, TL)");
        Set<String> edges = new TreeSet<>();
        Set<Integer> nodes = new TreeSet<>();

        for (int i = 0; i < mapping.length; i++) {
            System.out.printf("Tile %d (Resource, Roll):", i);
            for (int j = 0; j < 6; j++) {
                int n1 = mapping[i][j];
                int n2 = mapping[i][(j + 1) % 6];
                int low = Math.min(n1, n2);
                int high = Math.max(n1, n2);
                edges.add(low + "-" + high);
                nodes.add(n1);
                System.out.printf(" Corner %d -> Node %d |", j, n1);
            }
            System.out.println();
        }

        System.out.println("\nTotal Unique Nodes: " + nodes.size());
        System.out.println(
                "Nodes Range: " + ((TreeSet<Integer>) nodes).first() + " to " + ((TreeSet<Integer>) nodes).last());
        System.out.println("Total Periodic Edges: " + edges.size());

        System.out.println("\nEdges List (for createEdges):");
        int count = 0;
        System.out.print("{ ");
        for (String edge : edges) {
            String[] parts = edge.split("-");
            System.out.print("{ " + parts[0] + ", " + parts[1] + " }, ");
            if (++count % 9 == 0)
                System.out.println();
        }
        System.out.println("}");
    }
}
