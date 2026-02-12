#include <bits/stdc++.h>
using namespace std;

typedef tuple<int, int, int> edge; // dest, capacity, flow
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
            auto &[nbr, capacity, flow] = edge_list[edge];
            if (capacity - flow > 0 && distances[nbr] == -1) {
                distances[nbr] = distances[node] + 1;
                q.push(nbr);
                path[nbr] = {node, edge}; // store node and edge we came from
            }
        }
    }

    return distances[t] != -1;  // return true if path was found
}

/*
 * Send a flow from s -> t, using the path that bfs found
 *
 * Works backwards from t, recursively until it reaches s
 * Then, backtrack through the path and update edges
 * 
 * Returns the flow through that path
 */
int send_flow(int s, int t, int f = INT_MAX) {
    if (s == t) return f;

    auto &[prev, edge] = path[t];
    auto &capacity = get<1>(edge_list[edge]);
    auto &flow = get<2>(edge_list[edge]);

    int pushed = send_flow(s, prev, min(f, capacity-flow));

    flow += pushed;     // reference; actually edits edge
    auto &rflow = get<2>(edge_list[edge^1]);
    // auto &rflow = get<2>(edge_list[edge+1]);
    rflow -= pushed;    // reference; actually edits edge

    return pushed;
}

int edmonds_karp(int source, int sink) {
    int max_flow = 0;
    while (bfs(source, sink)) {
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
    adj.assign(N, vi{}); // fill adj with empty vectors

    for (int i = 0; i < edges; i++) {
        int u, v, capacity, cost;
        cin >> u >> v >> capacity >> cost; // not worrying about cost right now
         
        // Add forward edge
        edge_list.emplace_back(v, capacity, 0); // add edge
        adj[u].push_back(edge_list.size()-1);                    // store index of this edge

        // Add backwards edge
        edge_list.emplace_back(v, 0, 0); // add edge
        adj[v].push_back(edge_list.size()-1);                    // store index of this edge

        // Note: The reverse of edge i will be at i+1
    }

    cout << edmonds_karp(source, sink) << '\n';
}