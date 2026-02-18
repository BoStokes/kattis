#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef tuple<int, int, int> iii;
typedef vector<int> vi;
typedef vector<ii> vii;

int V, E;
vi price;
vector<vii> AL;

const int INF = 1e9;

// Issue: do you fill up to a full tank, 
// or only enough to get to the next city?
//
// Solved with "state-space modeling"
// We need to represent a state not only for
// every city, but also for every possible
// fuel level at that city.

int calculate(int capacity, int s, int e) {
    vector<vi> cost(V, vi(101, INF));

    priority_queue<iii, vector<iii>, greater<iii>> pq;
    pq.emplace(0, 0, s); // cost, fuel-level, city


    while (!pq.empty()) {
        auto [c, f, u] = pq.top(); pq.pop();
        if (c > cost[u][f]) continue;
        if (u == e) return c;
        
        for (auto [v, d] : AL[u]) {
            if (d > capacity) continue;
            for (int addl_fuel = max(0, d-f); f+addl_fuel <= capacity; addl_fuel++) {
                int new_cost = addl_fuel*price[u] + c;
                
                if (new_cost < cost[v][f+addl_fuel]) {
                    cost[v][f+addl_fuel] = new_cost;
                    pq.emplace(new_cost, f+addl_fuel, v);
                }
            }
        }
    }

    return -1;
}

int main() {
    scanf("%d %d", &V, &E);

    price = vi(V);
    for (int i = 0; i < V; i++) {
        scanf("%d", &price[i]);
    }
    
    AL = vector<vii>(V);
    for (int i = 0; i < E; i++) {
        int u, v, d;
        scanf("%d %d %d", &u, &v, &d);
        AL[u].emplace_back(v, d);
        AL[v].emplace_back(u, d);
    }

    int q; scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        int c, s, e;
        scanf("%d %d %d", &c, &s, &e);
        int ans = calculate(c, s, e);
        if (ans != -1)
            printf("%d\n", ans);
        else
            printf("impossible\n");
    }
}