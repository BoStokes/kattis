#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef tuple<int, int, int> iii;
typedef vector<int> vi;
typedef vector<ii> vii;

vi p;
vi ranks;

int findSet(int i) {
    if (p[i] == i) return i;
    p[i] = findSet(p[i]);
    return p[i];
}

void unionSet(int i, int j) {
    int x = findSet(i), y = findSet(j);
    if (x == y) return;
    if (ranks[x] > ranks[y])
        swap(x, y);
    p[x] = y;
    if (ranks[x] == ranks[y]) ranks[y]++;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, Q; cin >> N >> Q;

    ranks.assign(N, 1);
    p.assign(N, 0);
    for (int i = 0; i < N; i++)
        p[i] = i;
    
    for (int i = 0; i < Q; i++) {
        char op;
        int a, b;
        cin >> op >> a >> b;
        if (op == '=') {
            unionSet(a, b);
        }
        else {
            cout << (findSet(a) == findSet(b) ? "yes\n" : "no\n");
        }
    }
}
