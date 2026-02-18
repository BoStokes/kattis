#include <bits/stdc++.h>
using namespace std;

using T = tuple<int,int,int>;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<pair<int, int>>> adj;
    for (int src = 0; src < n; src++) {
        adj.push_back(vector<pair<int, int>>{});
        for (int dest = 0; dest < n; dest++) {
            int cost;
            cin >> cost;
            pair<int, int> data {dest, cost};
            if (src != dest) {
                adj[src].push_back(data);
            }
        }
    }


    priority_queue<T, vector<T>, greater<T>> pq; // cost, src, dest
    for (auto [nbr, cost] : adj[0]) {
        pq.push({cost, 0, nbr});
    }
    int connected = 1;
    bool visited[n] = {0};
    while (pq.size() && connected < n) {
        auto[cost, src, dest] = pq.top();
        pq.pop();

        if (visited[dest]) continue;
        visited[dest] = true;
        connected += 1;

        for (auto[nbr, nbr_cost] : adj[dest]) {
            if (visited[nbr] == false) {
                pq.push({nbr_cost, dest, nbr});
            }
        }
    }
}