#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 1e9;

int main() {
    while (1) {
        int V, E, Q, s; scanf("%d %d %d %d", &V, &E, &Q, &s);
        if (V == 0) return 0;
        vector<vii> AL(V, vii());
        for (int i = 0; i < E; i++) {
            int u, v, w; scanf("%d %d %d", &u, &v, &w);
            AL[u].emplace_back(v, w);
        }

        vi dist(V, INF); dist[s] = 0;
        
        for (int i = 0; i < V-1; i++) {
            bool modified = false;
            for (int u = 0; u < V; u++) {
                if (dist[u] != INF) {
                    for (auto [v, w] : AL[u]) {
                        if (dist[u]+w >= dist[v]) continue;
                        dist[v] = dist[u]+w;
                        modified = true;
                    }
                }
            }
            if (!modified) break;
        }

        for (int i = 0; i < V-1; i++) {
            bool modified = false;
            for (int u = 0; u < V; u++) {
                if (dist[u] != INF) {
                    for (auto [v, w] : AL[u]) {
                        if (dist[u]+w >= dist[v]) continue;
                        dist[v] = -INF;
                        modified = true;
                    }
                }
            }
            if (!modified) break;
        }

        for (int i = 0; i < Q; i++) {
            int e; scanf("%d", &e);
            if (dist[e] == INF) {
                printf("Impossible\n");
            }
            else if (dist[e] == -INF) {
                printf("-Infinity\n");
            }
            else {
                printf("%d\n", dist[e]);
            }
        }
    }
}