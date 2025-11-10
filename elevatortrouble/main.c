/*
 * Elevator Trouble
 */

#include "myQueue.h" // implementation in myQueue.c

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int floors, start, goal, up, down;
    scanf("%d %d %d %d %d", &floors, &start, &goal, &up, &down);

    int *visited = calloc(floors + 1, sizeof(int));
    queue *q = makeQueue();
    enqueue(q, start, 0);
    visited[start] = 1;

    int current, num_presses;

    while (!isEmpty(q)) {
        extract(q, &current, &num_presses); // places output values in current and num_presses
        if (current == goal) {
            printf("%d\n", num_presses);
            exit(0);
        }

        if (current + up <= floors && !visited[current + up]) {
            visited[current + up] = 1;
            enqueue(q, current + up, num_presses + 1);
        }
        if (current - down > 0 && !visited[current - down]) {
            visited[current - down] = 1;
            enqueue(q, current - down, num_presses + 1);
        }
    }
    printf("use the stairs\n");
}
