#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef tuple<int, int, int> iii;
typedef vector<int> vi;
typedef vector<ii> vii;

int V;
vi visited;
vector<iii> dishes;

typedef pair<double, int> di;
priority_queue<di, vector<di>, greater<di>> pq;

void process(int u) {
    visited[u] = true;
    auto[u_x, u_y, u_r] = dishes[u];

    for (int v = 0; v < V; v++) {
        if (visited[v]) continue;
        auto[v_x, v_y, v_r] = dishes[v];
        double cost = hypot((v_x-u_x), (v_y-u_y)) - u_r - v_r;
        pq.emplace(cost, v);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> V;
    for (int i = 0; i < V; i++) {
        int x, y, r; cin >> x >> y >> r;
        dishes.emplace_back(x, y, r);
    }

    visited.assign(V, false);
    process(0);
    double total_cost = 0.0;
    int edges_used = 0;
    while (!pq.empty() && edges_used < V-1) {
        auto [c, u] = pq.top(); pq.pop();
        if (visited[u]) continue;
        total_cost += c;
        edges_used++;
        process(u);
    }
    // cout << total_cost << '\n';
    cout << format("{}", total_cost);
}