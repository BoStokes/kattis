#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef tuple<int, int, int> edge;

vi p;
vi ranks;

int find_parent(int i) {
    if (p[i] == i) return i;
    p[i] = find_parent(p[i]);
    return p[i];
}

void union_set(int i, int j) {
    int x = find_parent(i), y = find_parent(j);
    if (x == y) return;
    if (ranks[x] > ranks[y])
        swap(x, y);
    p[x] = y;
    if (ranks[x] == ranks[y]) ranks[y]++;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int V, E; cin >> V >> E;
    vector<edge> edges;
}