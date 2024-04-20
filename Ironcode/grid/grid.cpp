#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Pos {
    int row;
    int col;
    int hops;
};

bool const inbounds(vector<vector<int>> &grid, Pos &pos) {
    return 0 <= pos.row && pos.row < grid.size() 
        && 0 <= pos.col && pos.col < grid[0].size();
}
vector<Pos> const get_neighbors(Pos &pos, int &hop) {
    return vector<Pos> {
        Pos{pos.row+hop, pos.col, pos.hops+1},
        Pos{pos.row-hop, pos.col, pos.hops+1},
        Pos{pos.row, pos.col+hop, pos.hops+1},
        Pos{pos.row, pos.col-hop, pos.hops+1}

    };
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> grid;
    bool visited[n][m];
    for (int i = 0; i < n; i++) {
        grid.push_back(vector<int>{});
        for (int j = 0; j < m;  j++) {
            char num;
            cin >> num;
            grid[i].push_back(num-'0');
            visited[i][j] = false;
        }
    }
    visited[0][0] = true;
    
    queue<Pos> q;
    q.push(Pos{0, 0, 0});
    int ans = -1;
    while (!q.empty()) {
        Pos pos = q.front();
        q.pop();
        if (pos.row == n-1 && pos.col == m-1) {
            ans = pos.hops;
            break;
        }
        visited[pos.row][pos.col] = true;
        for (auto neighbor : get_neighbors(pos, grid[pos.row][pos.col])) {
            if (inbounds(grid, neighbor) && !visited[neighbor.row][neighbor.col]) {
                q.push(neighbor);
                visited[neighbor.row][neighbor.col] = true;
            }
        }
    }
    cout << ans << endl;
}