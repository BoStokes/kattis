#include <vector>
#include <iostream>
#include <string>

using namespace std;

bool binary_dfs(int &r1, int &c1, int &r2, int &c2, vector<vector<int>> &grid, vector<vector<bool>> &visited);
bool decimal_dfs(int &r1, int &c1, int &r2, int &c2, vector<vector<int>> &grid, vector<vector<bool>> &visited);


int main() {
    int rows, cols;
    cin >> rows >> cols;

    vector<vector<int>> grid(rows, vector<int>(cols));

    string line;
    for (int r = 0; r < rows; r++) {
        cin >> line;
        for (int c = 0; c < cols; c++) {
            grid[r][c] = line[c] - '0';
        }
    }

    int test_cases;
    cin >> test_cases;

    int r1, c1, r2, c2;
    for (int i = 0; i < test_cases; i++) {
        cin >> r1 >> c1 >> r2 >> c2;
        r1--; c1--; r2--; c2--;
        int start = grid.at(r1).at(c1), dest = grid.at(r2).at(c2);
        vector<vector<bool>> visited(rows, vector<bool>(cols));
        visited.at(r1).at(c1) = true; 
        if (start == 0 && dest == 0 && (r1 == r2 && c1 == c2 || binary_dfs(r1, c1, r2, c2, grid, visited))) {
            cout << "binary\n";
        }
        else if (start == 1 && dest == 1 && (r1 == r2 && c1 == c2 || decimal_dfs(r1, c1, r2, c2, grid, visited))) {
            cout << "decimal\n";
        }
        else {
            cout << "neither\n";
        }
    }
    
}

bool inbounds(int &r, int &c, vector<vector<int>> &grid) {
    return 0 <= r && r < grid.size() && 0 <= c && c < grid.at(r).size();
}
vector<vector<int>> get_neighbors(int &r, int &c) {
    return vector<vector<int>> {
        vector<int> {r-1, c}, vector<int> {r, c-1}, vector<int> {r, c+1}, vector<int> {r+1, c}
    };
}

bool binary_dfs(int &r1, int &c1, int &r2, int &c2, vector<vector<int>> &grid, vector<vector<bool>> &visited) {
    for (vector<int> neighbor : get_neighbors(r1, c1)) {
        int new_r = neighbor.at(0), new_c = neighbor.at(1);
        if (inbounds(new_r, new_c, grid) && grid.at(new_r).at(new_c) == 0 && visited.at(new_r).at(new_c) == false) {
            visited.at(new_r).at(new_c) = true;
            if (new_r == r2 && new_c == c2 || binary_dfs(new_r, new_c, r2, c2, grid, visited))
                return true;
            visited.at(new_r).at(new_c) == false;
        }
    }
    return false;
}

bool decimal_dfs(int &r1, int &c1, int &r2, int &c2, vector<vector<int>> &grid, vector<vector<bool>> &visited) {
    for (vector<int> neighbor : get_neighbors(r1, c1)) {
        int new_r = neighbor.at(0), new_c = neighbor.at(1);
        if (inbounds(new_r, new_c, grid) && grid.at(new_r).at(new_c) == 1 && visited.at(new_r).at(new_c) == false) {
            visited.at(new_r).at(new_c) = true;
            if (new_r == r2 && new_c == c2 || decimal_dfs(new_r, new_c, r2, c2, grid, visited))
                return true;
            visited.at(new_r).at(new_c) == false;
        }
    }
    return false;
}
