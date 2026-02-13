#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;


    set<int> tree;
    vector<ll> depth(N+1, 0);
    ll counter = 0;
    for (int i = 0; i < N; i++) {
        int num; cin >> num;
        
        tree.insert(num);
        auto iter = tree.find(num);

        
        if (*iter != *tree.begin()) { // node has predecessor
            int predecessor = *prev(iter);
            depth[num] = depth[predecessor] + 1;
        }
        if (*iter != *tree.rbegin()) { // node has successor
            int successor = *next(iter);
            depth[num] = max(depth[num], depth[successor] + 1);
        }

        counter += depth[num];
        cout << counter << '\n';
    }
}