from collections import *

NUM_STREETS = int(input())

forward_graph = defaultdict(list)
reverse_graph = defaultdict(list)
input_order = []

for _ in range(NUM_STREETS):
    street_id, num_nbrs, *nbrs = map(int, input().split())
    input_order.append(street_id)
    for nbr in nbrs:
        forward_graph[street_id].append(nbr)
        reverse_graph[nbr].append(street_id)

# find unreachable: bfs in regular graph from 0, mark streets as reachable along the way
unreachable = defaultdict(lambda: True)
queue = deque([0])
while queue:
    street = queue.popleft()
    if not unreachable[street]:
        continue
    unreachable[street] = False

    for nbr in forward_graph[street]:
        if unreachable[nbr]:
            queue.append(nbr)

# find trapped: bfs in reverse graph from 0, mark streets as untrapped along the way
trapped = defaultdict(lambda: True)
queue = deque([0])
while queue:
    street = queue.popleft()
    if not trapped[street]:
        continue
    trapped[street] = False

    for nbr in reverse_graph[street]:
        if trapped[nbr]:
            queue.append(nbr)

if any(trapped[i] for i in input_order) or any(unreachable[i] for i in input_order):
    print(*(f'TRAPPED {i}' for i in input_order if trapped[i]), sep='\n')
    print(*(f'UNREACHABLE {i}' for i in input_order if unreachable[i]), sep='\n')
else:
    print('NO PROBLEMS')
