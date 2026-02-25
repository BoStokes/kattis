#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

typedef pair<int, ll> il;
typedef vector<il> vil;

const ll INF = LLONG_MAX;
int V;
vector<vil> AL;
vector<ll> dist;

ll SSSP(int s, int t, int k) {
    dist.assign(V, INF);
    queue<il> q;

    dist[s] = 0;
    q.emplace(s,0);
    while (!q.empty()) {
        auto &[u, d] = q.front(); q.pop();
        if (d > dist[s]) {
            
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int TC; cin >> TC;
    for (int tc = 0; tc < TC; tc++) {
        cin >> V;

        AL.assign(V, vil());

        for (int u = 0; u < V; u++) {
            int X; cin >>X;
            for (int i = 0; i < X; i++) {
                int v; cin >> v;
                ll w; cin >> w;
                AL[u].emplace_back(v, w);
                AL[v].emplace_back(u, w);
            }
        }
        int Q; cin >> Q;
        for (int q = 0; q < Q; q++) {
            int s, t, k; scanf("%d %d %d", &s, &t, &k);
            cout << SSSP(s, t, k) << '\n';
        }
    }
}

