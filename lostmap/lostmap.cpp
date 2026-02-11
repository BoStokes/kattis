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

void myunion(vector<int>& parents, int u, int v) {
    parents[find(parents, u)] = find(parents, v);
}

int main() {
    int n;
    cin >> n;

    vector<int> parents(n);
    for (int i = 0; i < n; i++) {
        parents[i] = i;
    }

    int dist;
    vector<Edge> edges;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> dist;
            if (i != j)
                edges.push_back(Edge{i, j, dist});
        }
    }
    sort(edges.begin(), edges.end());

    for (Edge &edge : edges) {
        int src = edge.u, dest = edge.v;
        if (find(parents, src) == find(parents, dest))
            continue;
        
        myunion(parents, src, dest);
        cout << src+1 << ' ' << dest+1 << '\n';
    }
}