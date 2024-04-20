import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CountingStars {

    static boolean[][] visited;
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(System.in);

        int caseNum = 0;
        int stars;
        while (sc.hasNext()) {
            caseNum++;
            stars = 0;
            int m = sc.nextInt();
            int n = sc.nextInt();
            visited = new boolean[m][n];
            sc.nextLine();
            List<String> sky = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                sky.add(sc.nextLine());
            }

            for (int row = 0; row < m; row++) {
                for (int col = 0; col < n; col++) {
                    if (! visited[row][col] && sky.get(row).charAt(col) == '-') {
                        stars++;
                        markVisited(sky, row, col);
                    }
                }
            }
            System.out.println("Case " + caseNum + ": " + stars);
        }
        sc.close();
    }
    public static int[][] getNeighbors(int row, int col) {
        return new int[][]{
            {row-1, col}, {row, col-1}, {row, col+1}, {row+1, col}
        };
    }
    public static boolean inBounds(List<String> sky, int row, int col) {
        return 0 <= row && row < sky.size() && 0 <= col && col < sky.get(row).length();
    }
    public static void markVisited(List<String> sky, int row, int col) {
        if (!inBounds(sky, row, col) || visited[row][col] || sky.get(row).charAt(col) != '-')
            return;
        
        visited[row][col] = true;
        for (int[] pos : getNeighbors(row, col)) {
            markVisited(sky, pos[0], pos[1]);
        }
    }
}