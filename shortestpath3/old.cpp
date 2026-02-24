#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 1e9;

vi predecessor;
int V, E, Q, s;
vector<vii> AL;
vi dist;

bool reach_start(int v) {
    if (v == s) return true;
    int u = predecessor[v];
}

int main() {
    while (1) {
        scanf("%d %d %d %d", &V, &E, &Q, &s);
        if (V == 0) return 0;
        AL.assign(V, vii());
        for (int i = 0; i < E; i++) {
            int u, v, w; scanf("%d %d %d", &u, &v, &w);
            AL[u].emplace_back(v, w);
        }

        dist.assign(V, INF); dist[s] = 0;
        predecessor.assign(V, -1);
        
        for (int i = 0; i < V-1; i++) {
            bool modified = false;
            for (int u = 0; u < V; u++) {
                if (dist[u] != INF) {
                    for (auto [v, w] : AL[u]) {
                        if (dist[u]+w > dist[v]) continue;
                        dist[v] = dist[u]+w;
                        predecessor[v] = u;
                        modified = true;
                    }
                }
            }
            if (!modified) break;
        }

        bool hasNegativeCycle = false;
        for (int u = 0; u < V; u++)
            if (dist[u] != INF)
                for (auto [v, w] : AL[u])
                    if (dist[v] > dist[u]+w)
                        hasNegativeCycle = true;
        
        

        for (int i = 0; i < Q; i++) {
            int e; scanf("%d", &e);
            if (dist[e] == INF) {
                printf("Impossible");
            }
            else {

            }
        }
    }
}
