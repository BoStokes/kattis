import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class cakeymccakeface {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int m = Integer.parseInt(sc.nextLine());
        ArrayList<Integer> entries = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            entries.add(sc.nextInt());
        }
        ArrayList<Integer> exits = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            exits.add(sc.nextInt());
        }
        sc.close();

        HashMap<Integer, Integer> counts = new HashMap<>();
        for (int entry : entries) {
            for (int exit : exits) {
                int time = exit - entry;
                if (time < 0) continue;
                counts.put(time, counts.getOrDefault(time, 0) + 1);
            }
        }
        int bestCount = -1;
        int bestVal = 0;
        for (int i : counts.keySet()) {
            if (counts.get(i) > bestCount) {
                bestVal = i;
                bestCount = counts.get(i);
            }
            else if (counts.get(i) == bestCount) {
                bestVal = Math.min(bestVal, i);
            }
        }
        System.out.println(bestVal);
    }
}