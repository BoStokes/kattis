#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int V, Q;
vector<vii> AL;

int main() {
    int TC; scanf("%d", &TC);
    for (int tc = 0; tc < TC; tc++) {
        scanf("%d", &V);
        AL.assign(V, vii());
        for (int u = 0; u < V; u++) {
            int X; scanf("%d", &X);
            for (int i = 0; i < X; i++) {
                int v, w; scanf("%d %d", &v, &w);
                AL[u].emplace_back(v, w);
            }
        }
        scanf("%d", &Q);
        for (int q = 0; q < Q; q++) {
            int s, t, k; scanf("%d %d %d", &s, &t, &k);
            printf("-1\n\n");
        }
    }

}
