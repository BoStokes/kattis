/*
 * Sheba's Amoebas
 */

#include <stdio.h>
#include <stdlib.h>

int rows, cols;

void dfs(char **grid, int i, int j);

int main()
{
    scanf("%d %d\n", &rows, &cols);
    
    char **grid = malloc(sizeof(char *) * rows);
    for (int i = 0; i < rows; i++) {
        grid[i] = malloc(sizeof(char) * cols);
    }
    
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            grid[i][j] = (char)getchar();
        }
        getchar(); // ignore newline
    }

    int count = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == '#') {
                dfs(grid, i, j);
                count++;
            }
        }
    }
    printf("%d\n", count);
}

int inbounds(int i, int j)
{
    return 0 <= i && i < rows && 0 <= j && j < cols;
}
void dfs(char **grid, int i, int j)
{
    grid[i][j] = '.';

    for (int nbr_i = i - 1; nbr_i <= i + 1; nbr_i++) {
        for (int nbr_j = j - 1; nbr_j <= j + 1; nbr_j++) {
            if (inbounds(nbr_i, nbr_j) && grid[nbr_i][nbr_j] == '#')
                dfs(grid, nbr_i, nbr_j);
        }
    }
    return;
}
