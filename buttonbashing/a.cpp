#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main() {
    int A; scanf("%d", &A);
    for (int a = 0; a < A; a++) {
        int N, T; scanf("%d %d", &N, &T);
        int buttons[N];
        for (int i = 0; i < N; i++) scanf("%d", &buttons[i]);

        vi visited(3601, 0);
        queue<ii> q;
        ii best {3601, 0};
        q.emplace(0,0);
        visited[0] = 1;
        while (!q.empty()) {
            auto [time, presses] = q.front(); q.pop();
            if (time >= T && time < best.first) {
                best = {time, presses};
            }
            if (best.first == T) break;
            for (int i = 0; i < N; i++) {
                int ntime = max(0, min(3600, time+buttons[i]));
                if (!visited[ntime]) {
                    visited[ntime] = 1;
                    q.emplace(ntime, presses+1);
                }
            }
        }
        printf("%d %d\n", best.second, best.first-T);
    }
}
