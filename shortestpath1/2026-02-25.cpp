#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 1e9;

int V, E, Q, s;
vector<vii> AL;
vi dist;

void SSSP() {
    dist.assign(V, INF);
    priority_queue<ii, vii, greater<ii>> pq;
    dist[s] = 0;
    pq.emplace(0, s);
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : AL[u]) {
            if (d+w >= dist[v]) continue;
            dist[v] = d+w;
            pq.emplace(d+w, v);
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    while (1) {
        cin >> V >> E >> Q >> s;
        if (V == 0) return 0;
        AL.assign(V, vii());
        for (int i = 0; i < E; i++) {
            int u, v, w; cin >> u >> v >> w;
            AL[u].emplace_back(v, w);
        }
        SSSP();
        for (int i = 0; i < Q; i++) {
            int t; cin >> t;
            if (dist[t] < INF) {
                cout << dist[t] << '\n';
            }
            else {
                cout << "Impossible" << '\n';
            }
        }
    }
}
