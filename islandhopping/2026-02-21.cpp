#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef pair<double, double> dd;
typedef pair<double, int> di;

typedef vector<int> vi;
typedef vector<ii> vii;




double dist(dd &u, dd &v) {
    auto [x1, y1] = u;
    auto [x2, y2] = v;
    return hypot(x1-x2, y1-y2);
}

int main() {
    int n; scanf("%d", &n);
    for (int a = 0; a < n; a++) {
        int V; scanf("%d", &V);
        
        vector<dd> coords;
        for (int i = 0; i < V; i++) {
            double x, y; scanf("%lf %lf", &x, &y);
            coords.emplace_back(x, y);
        }

        double length = 0.0;
        vi visited(V, 0);
        priority_queue<di, vector<di>, greater<di>> pq;
        pq.emplace(0.0, 0);
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (visited[u]) continue;
            visited[u] = 1;
            length += d;

            for (int v = 0; v < V; v++) {
                if (visited[v]) continue;
                pq.emplace(dist(coords[u], coords[v]), v);
            }
        }
        printf("%f\n", length);
    }
}
