#include "myQueue.h"

#include <stdlib.h>
#include <stdio.h>


queue *makeQueue(void)
{
    queue *q = malloc(sizeof(queue));

    q->head = malloc(sizeof(node));
    q->head->next = NULL;
    q->head->floor = -1;
    q->tail = q->head;

    return q;
}

void enqueue(queue *q, int in_floor, int in_presses)
{
    node *new = malloc(sizeof(node));
    new->floor = in_floor;
    new->num_presses = in_presses;

    q->tail->next = new;
    new->next = NULL;
    q->tail = q->tail->next;
}

void extract(queue *q, int *out_floor, int *out_presses)
{
    if (isEmpty(q)) {
        fprintf(stderr, "empty queue\n");
        return;
    }
    node *popped = q->head->next;
    q->head->next = popped->next;
    *out_floor = popped->floor;
    *out_presses = popped->num_presses;
    free(popped);

    if (isEmpty(q)) {
        q->tail = q->head;
    }
}

int isEmpty(queue *q)
{
    return q->head->next == NULL;
}
