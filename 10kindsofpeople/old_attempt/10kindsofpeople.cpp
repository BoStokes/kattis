#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Pos {
    int row;
    int col;
};

vector<Pos> neighbors(Pos pos) {
    int x = pos.row, y = pos.col;
    return {Pos{x, y-1}, 
            Pos{x-1, y}, 
            Pos{x+1, y},
            Pos{x, y+1}};
}
bool inbounds(Pos pos, vector<vector<int>> &grid) {
    return 0 <= pos.row && pos.row < grid.size()
        && 0 <= pos.col && pos.col < grid[pos.row].size();
}

bool dfs(Pos pos, Pos dest, vector<vector<int>> &grid, vector<vector<bool>> &visited) {
    for (auto neighbor : neighbors(pos)) {
        if (inbounds(neighbor, grid) && visited[neighbor.row][neighbor.col] == false && grid[pos.row][pos.col] == grid[neighbor.row][neighbor.col]) {
            visited[neighbor.row][neighbor.col] = true;
            if (neighbor.row == dest.row && neighbor.col == dest.col || dfs(neighbor, dest, grid, visited)) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    int r, c;
    cin >> r >> c;
    vector<vector<int>> grid(r, vector<int>(c));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            char x;
            cin >> x;
            grid[i][j] = x - '0';
        }
    }
    int n; cin >> n;
    while (0 < n--) {
        vector<vector<bool>> visited(r, vector<bool>(c));
        int x1, y1, x2, y2;
        cin >> x1;
        cin >> y1;
        cin >> x2;
        cin >> y2;
        if (grid[--x1][--y1] != grid[--x2][--y2]) {
            cout << "neither" << endl;
        }
        else {
            visited[x1][y1] = true;
            Pos src{x1, y1}, dest{x2, y2};

            if (x1 == x2 && y1 == y2 || dfs(src, dest, grid, visited)) {
                if (grid[x1][y1] == 0)
                    cout << "binary" << endl;
                else
                    cout << "decimal" << endl;
            }
            else {
                cout << "neither" << endl;
            }
        }
    }

}