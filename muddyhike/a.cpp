#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef tuple<int, int, int> iii;

vector<ii> dirs = {{-1,0},{0,-1},{0,1},{1,0}};

int main() {
    int R, C;
    scanf("%d %d", &R, &C);

    priority_queue<iii, vector<iii>, greater<iii>> pq;
    int grid[R][C];
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &grid[i][j]);
            if (j == 0) pq.emplace(grid[i][j], i, j);
        }
    }

    vector<vi> visited(R, vi(C, 0));
    int deepest = 0;
    while (!pq.empty()) {
        auto [d, r, c] = pq.top(); pq.pop();
        if (visited[r][c]) continue;
        visited[r][c] = 1;
        deepest = max(deepest, d);
        if (c == C-1) break;
        
        for (auto [dr, dc] : dirs) {
            if (0 <= r+dr && r+dr < R && 0 <= c+dc && c+dc < C && !visited[r+dr][c+dc]) {
                pq.emplace(grid[r+dr][c+dc], r+dr, c+dc);
            }
        }
    }
    printf("%d\n", deepest);
}