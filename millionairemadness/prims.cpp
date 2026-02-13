#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef tuple<int, int, int> iii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 2e9;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);


    int M, N;
    cin >> M >> N;
    vector<vi> height(M, vi(N, 0));
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cin >> height[i][j];
        }
    } 
    vii directions {{-1,0},{0,-1},{0,1},{1,0}};

    vector<vi> cost(M, vi(N, INF));
    priority_queue<iii, vector<iii>, greater<iii>> pq;
    pq.emplace(0, 0, 0);
    cost[0][0] = 0;
    while (!pq.empty()) {
        auto [c, i, j] = pq.top(); pq.pop();

        if (i == M-1 && j == N-1) {
            cout << cost[M-1][N-1] << '\n';
            return 0;
        }

        if (c > cost[i][j]) continue;

        for (auto [di, dj] : directions) {
            int ni = i+di, nj = j+dj;
            
            if (0 <= ni && ni < M && 0 <= nj && nj < N) {
                int nc = max(c, max(0, height[ni][nj] - height[i][j]));
                if (nc < cost[ni][nj]) {
                    cost[ni][nj] = nc;
                    pq.emplace(nc, ni, nj);
                }
            }
        }
    }
}