#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

vector<vi> grid;

int main() {
    int TC; scanf("%d", &TC);
    while (TC--) {
        int cols, rows; scanf("%d %d", &cols, &rows);
        grid.assign(rows, vi(cols));
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                grid[r][c] = getchar();
                printf("%c", grid[r][c]);
            }
            getchar();
        }
        printf("\n");
    }
}
