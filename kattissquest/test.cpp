#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    multiset<int, greater<int>> tree;

    for (int i = 1; i < 10; i++) {
        tree.insert(i);
    }
    tree.insert(5);
    
    auto it = tree.lower_bound(100);
    if (it != tree.end())
        cout << *it << endl;
    else
        cout << "nope\n";
}
