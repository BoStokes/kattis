import java.io.File;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        for (int a = 0; a < n; a++) {
            int numIslands = sc.nextInt();
            sc.nextLine();
            int[][] islands = new int[numIslands][2];
            for (int i = 0; i < numIslands; i++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                sc.nextLine();
                islands[i] = new int[]{x, y};
            }
            System.out.println(Arrays.toString(islands));
        }
        sc.close();
    }
}