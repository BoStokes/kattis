#include <bits/stdc++.h>
using namespace std;
typedef tuple<int, int, int, int> edge;
typedef vector<int> vi;
typedef pair<int, int> ii;
const int INF = INT_MAX;
int N;
vector<edge> edge_list;
vector<vi> adj;
vi distances;
vector<ii> parent_edge;
bool spfa(int s, int t) {
    distances.assign(N, INF);
    distances[s] = 0;
    queue<int> q({s});
    vi in_queue(N, 0);
    in_queue[s] = true;
    parent_edge.assign(N, {-1, -1});
    while (!q.empty()) {
        int u = q.front(); q.pop();
        in_queue[u] = false;
        for (auto &edge : adj[u]) {
            auto &[v, capacity, cost, flow] = edge_list[edge];
            if (capacity > flow && distances[v] > distances[u] + cost) {
                distances[v] = distances[u] + cost;
                parent_edge[v] = {u, edge};
                if (!in_queue[v]) {
                    q.push(v);
                    in_queue[v] = 1;
                }
            }
        }
    }
    return distances[t] != INF;
}
int min_cost = 0;
int send_flow(int s, int t, int f = INF) {
    if (s == t) return f;
    auto &[prev, edge] = parent_edge[t];
    auto &[v, capacity, cost, flow] = edge_list[edge];
    int pushed = send_flow(s, prev, min(f, capacity-flow));
    flow += pushed;
    auto &rflow = get<3>(edge_list[edge^1]);
    rflow -= pushed;
    min_cost += pushed*cost;
    return pushed;
}
int edmonds_karp(int source, int sink) {
    int max_flow = 0;
    while (spfa(source, sink)) {
        int f = send_flow(source, sink);
        if (f == 0) break;
        max_flow += f;
    }
    return max_flow;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int nodes, edges, source, sink;
    cin >> nodes >> edges >> source >> sink;
    N = nodes;
    adj.assign(N, vi{});
    for (int i = 0; i < edges; i++) {
        int u, v, capacity, cost;
        cin >> u >> v >> capacity >> cost;
        edge_list.emplace_back(v, capacity, cost, 0);
        adj[u].push_back(edge_list.size()-1);
        edge_list.emplace_back(u, 0, -cost, 0);
        adj[v].push_back(edge_list.size()-1);
    }
    int max_flow = edmonds_karp(source, sink);
    cout << max_flow << ' ' << min_cost << '\n';
}
