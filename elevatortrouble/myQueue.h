#ifndef MY_QUEUE
#define MY_QUEUE

typedef struct node {
    struct node *next;
    int floor;
    int num_presses;
} node;

typedef struct {
    node *head;
    node *tail;
} queue;

queue *makeQueue(void);

void enqueue(queue *q, int in_val, int in_presses);

void extract(queue *q, int *out_val, int *out_presses);

int peek(queue *q);

int isEmpty(queue *q);

#endif
