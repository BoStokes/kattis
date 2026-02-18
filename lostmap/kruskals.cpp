#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef tuple<int, int, int> edge;

int V;

vi p, height;

int findSet(int i) {
    if (p[i] == i) return i;
    p[i] = findSet(p[i]);
    return p[i];
}
void unionSet(int x, int y) {
    x = findSet(x);
    y = findSet(y);
    if (height[x] > height[y]) swap(x, y);
    p[x] = y;
    if (height[x] == height[y]) height[y]++;
}

int main() {
    cin >> V;
    int adj[V][V];
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            scanf("%d", &adj[i][j]);
        }
    }

    priority_queue<edge, vector<edge>, greater<edge>> edges;
    for (int i = 1; i < V; i++) {
        for (int j = 0; j < i; j++) {
            edges.emplace(adj[i][j], i, j);
        }
    }

    int edges_used = 0;
    p.assign(V, 0);
    for (int i = 0; i < V; i++) p[i] = i;
    height.assign(V, 1);
    while (edges_used < V-1) {
        auto [w, u, v] = edges.top(); edges.pop();
        if (findSet(u) == findSet(v)) continue;
        unionSet(u, v);
        edges_used++;
        printf("%d %d\n", u+1, v+1);
    }
}