#include <iostream>
#include <vector>

using namespace std;

struct Pos {
    int row;
    int col;
};

bool in_bounds(vector<vector<char>> &sky, Pos pos);
vector<Pos> get_neigbors(vector<vector<char>> &sky, Pos pos);
void remove_star(vector<vector<char>> &sky, Pos pos);


int main() {
    int rows = 0, cols = 0;
    int case_num = 1;
    while (cin >> rows >> cols) {
        vector<vector<char>> sky;
        for (int i = 0; i < rows; i++) {
            string line;
            cin >> line;
            vector<char> row;
            for (char c : line) {
                row.push_back(c);
            }
            sky.push_back(row);
        }
        int star_count = 0;
        Pos pos;
        for (pos.row = 0; pos.row < sky.size(); pos.row++) {
            for (pos.col = 0; pos.col < sky[0].size(); pos.col++){
                if (sky[pos.row][pos.col] == '-') {
                    star_count++;
                    remove_star(sky, pos);
                }
            }
        }
        cout << "Case " << case_num << ": " << star_count << '\n';
        case_num++;
    }
}

bool in_bounds(vector<vector<char>> &sky, Pos pos) {
    return 0 <= pos.row && pos.row < sky.size()
        && 0 <= pos.col && pos.col < sky[0].size();
}
vector<Pos> get_neigbors(vector<vector<char>> &sky, Pos pos) {
    return {Pos{pos.row, pos.col-1},
            Pos{pos.row-1, pos.col},
            Pos{pos.row+1, pos.col},
            Pos{pos.row, pos.col+1}};
}
void remove_star(vector<vector<char>> &sky, Pos pos) {
    if (!in_bounds(sky, pos) || sky[pos.row][pos.col] != '-')
        return;
    sky[pos.row][pos.col] = '#';
    for (auto v : get_neigbors(sky, pos)) {
        remove_star(sky, v);
    }
}