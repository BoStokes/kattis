#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

unordered_map<int, unordered_map<int, int>> adj;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    adj.clear();
    adj[6][7] = 8;
    printf("%d\n", adj[6][7]);
}
