#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    multiset<int, greater<int>> tree;
    unordered_map<int, priority_queue<int>> best_gold; 
    int N; cin >> N;
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        
        if (s == "add") {
            int e, g; cin >> e >> g;
            tree.insert(e);
            best_gold[e].push(g);
        }
        else {
            int x; cin >> x;
            long long gold = 0;
            while (1) {
                auto it = tree.lower_bound(x);
                if (it == tree.end()) break;

                int e = *it;
                if (x <= 0 || e > x) break;
                int g = best_gold[e].top(); best_gold[e].pop();

                x -= e;
                gold += g;

                tree.erase(it);
            }
            cout << gold << '\n';
        }
    }
}
