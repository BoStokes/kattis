#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

vii dirs {{-1,0},{0,-1},{0,1},{1,0}};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, N; cin >> R >> C >> N;
    queue<ii> q;
    vector<vi> visited(R, vi(C, 0));
    int num_visited = 0;
    for (int i = 0; i < N; i++) {
        int r, c; cin >> r >> c;
        if (visited[r-1][c-1]) continue;
        visited[r-1][c-1] = 1;
        num_visited++;
        q.emplace(r-1, c-1);
    }
    
    int days = -1;
    for (days = 1; !q.empty() && num_visited < R*C; days++) {
        int size = q.size();

        for (int i = 0; !q.empty() && i < size; i++) {
            auto [r, c] = q.front(); q.pop();

            for (auto[dr, dc] : dirs) {
                int nr = r+dr, nc = c+dc;
                if (nr < 0 || nr >= R || nc < 0 || nc >= C || visited[nr][nc]) continue;

                visited[nr][nc] = 1;
                num_visited++;
                q.emplace(nr, nc);
            }
        }
    }
    if (num_visited == R*C) {
        cout << days << '\n';
        return 0;
    }
    // Do this so kattis will give runtime error when num_visited != R*C
    visited[R+200][C+500] = 6;
}