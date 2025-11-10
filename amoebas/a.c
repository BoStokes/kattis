#include <stdio.h>
#include <stdlib.h>

int rows, cols;

void dfs(int **grid, int **visited, int i, int j);
void print_grid(int **grid);


int main(void)
{
    scanf("%d %d\n", &rows, &cols);
    
    // allocate space for visited and grid
    int **visited = malloc(sizeof(int *) * (unsigned long)rows);
    int **grid = malloc(sizeof(int *) * (unsigned long)rows);
    for (int i = 0; i < rows; i++) {
        visited[i] = malloc(sizeof(int) * (unsigned long)cols);
        grid[i] = malloc(sizeof(int) * (unsigned long)cols);
    }
    
    // input grid
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            grid[i][j] = getchar();
        }
        getchar(); // ignore newline
    }
    
    int count = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == '#' && visited[i][j] == 0) {
                dfs(grid, visited, i, j);
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

void dfs(int **grid, int **visited, int i, int j)
{
    if (visited[i][j])
        return;
    visited[i][j] = 1;

    for (int nbr_i = i-1; nbr_i <= i+1; nbr_i++) {
        for (int nbr_j = j-1; nbr_j <= j+1; nbr_j++) {
            if (!inbounds(nbr_i, nbr_j) || grid[i][j] != '#')
                continue;
            dfs(grid, visited, nbr_i, nbr_j);
        }
    }
    return;
}

void print_grid(int **grid)
{
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%2d ", grid[i][j]);
        }
        printf("\n");
    }
}