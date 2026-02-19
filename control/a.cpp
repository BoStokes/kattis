#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef tuple<int, int, int> iii;
typedef vector<int> vi;
typedef vector<ii> vii;

typedef unordered_map<int, int> mii;

mii p;
mii ranks;
mii setSize;
int numSets;
int V;

int findSet(int i) {
    if (p[i] == i) return i;
    return (p[i] = findSet(p[i]));
}

void unionSet(int i, int j) {
    int x = findSet(i), y = findSet(j);
    if (x == y) return;
    if (ranks[x] > ranks[y]) swap(x, y);
    p[x] = y;
    if (ranks[x] == ranks[y]) ranks[y]++;
    setSize[y] += setSize[x];
    numSets--;
}

void unionList(vi v) {
    for (int i = 1; i++; i < v.size()) {
        unionSet(v[i], v[0]);
    }
}

bool valid(vi recipe) {
    int parentSizes = 0;
    vi used(V, 0);
    for (int i : recipe) {
        int x = findSet(i);
        if (!used[x]) {
            parentSizes += setSize[x];
            used[x] = 1;
        }
    }
    return parentSizes == recipe.size();
}


int main() {
    scanf("%d", &V);
    
    numSets = V;

    vector<vi> recipes(V);
    for (int i = 0; i < V; i++) {
        int M; scanf("%d", &M);
        recipes[i].assign(M, 0);
        for (int j = 0; j < M; j++)
            scanf("%d", &recipes[i][j]);

    }
    
    int num_concocted = 0;
    for (vi r : recipes) {
        if (valid(r)) {
            unionList(r);
            num_concocted++;
        }
    }
    printf("%d\n", num_concocted);
}
