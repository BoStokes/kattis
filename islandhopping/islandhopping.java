import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class islandhopping {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        for (int a = 0; a < n; a++) {
            // Parse input, put into 2d array
            int numIslands = Integer.parseInt(sc.nextLine());
            double[][] islands = new double[numIslands][2];
            for (int i = 0; i < numIslands; i++) {
                String line = sc.nextLine();
                islands[i] = Arrays.stream(line.split(" ")).mapToDouble(Double::parseDouble).toArray();
            }
            
            // Preload distances to every other edge
            Edge[][] edges = new Edge[numIslands][numIslands];
            for (int i = 0; i < numIslands; i++) {
                for (int j = 0; j < numIslands; j++) {
                    if (i == j) continue;
                    double dist = distance(islands[i], islands[j]);
                    edges[i][j] = new Edge(i, j, dist);
                }
            }


            boolean[] visited_islands = new boolean[numIslands];
            visited_islands[0] = true; int num_visited = 1;
            double totalCost = 0.0;
            PriorityQueue<Edge> curr_edges = new PriorityQueue<>((Edge e1, Edge e2) -> Double.compare(e1.cost, e2.cost));
            for (Edge e : edges[0]) {
                if (e != null)
                curr_edges.add(e);
            }

            while (curr_edges.isEmpty() == false && num_visited < numIslands) {
                Edge curr = curr_edges.poll();
                if (visited_islands[curr.dest] == false) {
                    visited_islands[curr.dest] = true; num_visited++;
                    totalCost += curr.cost;

                    for (Edge next : edges[curr.dest]) {
                        if (next != null && visited_islands[next.dest] == false) {
                            curr_edges.add(next);
                        }
                    }
                }
            }
            System.out.println(totalCost);
        }
        sc.close();
    }

    static double distance(double[] island1, double[] island2) {
        double dx = island1[0] - island2[0];
        double dy = island1[1] - island2[1];
        return Math.sqrt(dx*dx + dy*dy);
    }

    static class Edge {
        int src, dest;
        double cost;

        Edge(int src, int dest, double cost) {
            this.src = src;
            this.dest = dest;
            this.cost = cost;
        }

        public String toString() {
            return "cost: " + cost + " source: " + src + " dest: " + dest;
        }
    }
}