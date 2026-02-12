#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef tuple<int, int, int> iii;
typedef vector<int> vi;
typedef vector<ii> vii;

vector<vii> AL;
vi visited;
priority_queue<iii, vector<iii>, greater<iii>> pq; // holds (weight, src, dest)

void process(int u) {
    visited[u] = true;
    for (auto &[v, w] : AL[u]) {
        if (!visited[v])
            pq.emplace(w, u, v);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (1) {
        int V, E;
        cin >> V >> E;
        if (V == 0 && E == 0) break;

        AL.assign(V, vii());
        for (int i = 0; i < E; i++) {
            int u, v, w;
            cin >> u >> v >> w;
            AL[u].emplace_back(v, w);
            AL[v].emplace_back(u, w);
        }

        vii mst;
        visited.assign(V, false);
        process(0);
        int total_weight = 0;
        int edges_used = 0;
        while (!pq.empty() && edges_used < V-1) {
            auto [w, u, v] = pq.top(); pq.pop();
            if (visited[v]) continue;

            mst.emplace_back(min(u, v), (max(u, v)));
            total_weight += w;
            edges_used++;
            process(v);
        }

        if (edges_used < V-1 || E < V-1) {
            cout << "Impossible\n";
        }
        else {
            sort(mst.begin(), mst.end());
            cout << total_weight << '\n';
            for (auto &[u, v] : mst) {
                cout << u << ' ' << v << '\n';
            }
        }
    }
}