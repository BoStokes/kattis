#include <bits/stdc++.h>
using namespace std;

typedef tuple<int, int, int, int> edge; // dest, capacity, cost, flow
typedef vector<int> vi;
typedef pair<int, int> ii;

int N;
vector<edge> edge_list;
vector<vi> adj;

vi distances;
vector<ii> path; // {previous node, edge}

/*
 * Performs bfs to find the (unweighted) shortest path from node s to node t
 * Uses distances vector to store distances from s
 * Uses path vector to store the path
 * 
 * Returns true if a path was found using positive edges, otherwise false
 */
bool bfs(int s, int t) {
    distances.assign(N, -1);
    distances[s] = 0;

    queue<int> q({s});
    path.assign(N, {-1, -1});
    while (!q.empty()) {
        int node = q.front(); q.pop();
        if (node == t) break;

        for (auto &edge : adj[node]) {
            auto &[nbr, capacity, cost, flow] = edge_list[edge];
            if (capacity > flow && distances[nbr] == -1) {
                distances[nbr] = distances[node] + 1;
                q.push(nbr);
                path[nbr] = {node, edge}; // store node and edge we came from
            }
        }
    }

    return distances[t] != -1;  // return true if path was found
}

bool bellman_ford(int s, int t) {
    distances.assign(N, INT_MAX);
    distances[s] = 0;

    path.assign(N, {-1, -1});
    for (int i = 0; i < N-1; i++) {
        for (int u = 0; u < N; u++) {
            if (distances[u] != INT_MAX) {
                for (auto &edge : adj[u]) {
                    auto &[v, capacity, cost, flow] = edge_list[edge];
                    if (capacity > flow && distances[u] + cost < distances[v]) {
                        distances[v] = distances[u] + cost;
                        path[v] = {u, edge};
                    }
                }
            }
        }
    }
    return distances[t] < INT_MAX;
}

/*
 * Send a flow from s -> t, using the path that bfs found
 *
 * Works backwards from t, recursively until it reaches s
 * Then, backtrack through the path and update edges
 * 
 * Returns the flow through that path
 */
ii send_flow(int s, int t, int f = INT_MAX) {
    if (s == t) return {f, 0};

    auto &[prev, edge] = path[t];
    auto &capacity = get<1>(edge_list[edge]);
    auto &cost = get<2>(edge_list[edge]);
    auto &flow = get<3>(edge_list[edge]);
    
    auto [pushed, c] = send_flow(s, prev, min(f, capacity-flow));

    flow += pushed;     // reference; actually edits edge
    auto &rflow = get<3>(edge_list[edge^1]);
    rflow -= pushed;    // reference; actually edits edge
    return {pushed, c + cost};
}

ii edmonds_karp(int source, int sink) {
    int max_flow = 0;
    int total_cost = 0;
    while (bellman_ford(source, sink)) {
        auto [f, c] = send_flow(source, sink);
        if (f == 0) break;
        max_flow += f;
        total_cost += c * f;
    }

    return {max_flow, total_cost};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int nodes, edges, source, sink;
    cin >> nodes >> edges >> source >> sink;
    N = nodes;
    adj.assign(N, vi{}); // fill adj with empty vectors

    for (int i = 0; i < edges; i++) {
        int u, v, capacity, cost;
        cin >> u >> v >> capacity >> cost;
         
        // Add forward edge
        edge_list.emplace_back(v, capacity, cost, 0); // add edge
        adj[u].push_back(edge_list.size()-1);                    // store index of this edge

        // Add backwards edge
        edge_list.emplace_back(u, 0, -cost, 0); // add edge
        adj[v].push_back(edge_list.size()-1);                    // store index of this edge

        // Note: The reverse of edge i will be at i+1
    }
    auto [f, c] = edmonds_karp(source, sink);
    cout << f << ' ' << c << '\n';
}