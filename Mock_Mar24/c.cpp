#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v, dist;
    bool operator<(const Edge& other) const {
        return dist < other.dist;
    }
};

int find(vector<int>& parents, int node) {
    if (parents[node] == node) return node;
    return parents[node] = find(parents, parents[node]);
}

void union_uv(vector<int>& parents, int u, int v) {
    parents[find(parents, u)] = find(parents, v);
}

int main(){
    int n;
    cin >> n;

    vector<Edge> edges;
    vector<int> parents(n + 1);
    for (int i = 1; i <= n; i++) {
        parents[i] = i;
    }

    for (int u = 1; u <= n; u++) {
        for (int v = 1; v <= n; v++) {
            int dist;
            cin >> dist;
            if (u != v) {
                edges.push_back({u, v, dist});
            }
        }
    }

    sort(edges.begin(), edges.end());

    for (const Edge& edge : edges) {
        if (find(parents, edge.u) != find(parents, edge.v)) {
            union_uv(parents, edge.u, edge.v);
            cout << edge.u << " " << edge.v << '\n';
        }
    }
}