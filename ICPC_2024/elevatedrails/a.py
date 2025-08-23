from collections import defaultdict, deque

num_stations, num_questions = map(int, input().split())

graph = [[] for _ in range(num_stations+1)]

for _ in range(num_stations-3):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


# seperate graph into the three islands
get_island = dict() # get_island[i] = the corresponding island for station i
island_sets = []
for station in range(1, num_stations+1):
    if len(island_sets) == 3:
        break
    if station in get_island:
        continue

    island_num = len(island_sets)+1 # either 1, 2, or 3 based on how many have been made so far

    # perform bfs from this station, give every reachable station same island
    q = deque()
    q.append(station)
    island_set = set()
    while q:
        curr = q.popleft()
        get_island[curr] = island_num
        island_set.add(curr)
        for nbr in graph[curr]:
            if nbr not in get_island: # if we haven't seen neighbor yet, add to queue
                q.append(nbr)
    island_sets.append(island_set)



# Precompute the distance from center for every node in each seperate graph
# Center = middle node(s) of longest path through the tree
# Iteratively remove leaf nodes until you are left with either one or two

dist_from_center_to_leave = dict() # steps from center of tree to leave
dist_to_center = dict() # steps from node to center of its tree
center_lists = [None] # lists with center(s) of tree corresponding to island_num
for island_num, island in enumerate(island_sets, start=1):
    degrees = dict()
    q = deque()
    steps = 0
    for node in island:
        degrees[node] = len(graph[node])
        if len(graph[node]) == 1:
            q.append(node)

    while len(degrees) > 2:
        nodes = len(q)
        for _ in range(nodes):
            node = q.popleft()
            for nbr in graph[node]:
                if nbr not in degrees:
                    continue
                degrees[nbr] -= 1
                if degrees[nbr] == 1:
                    q.append(nbr)
            del degrees[node] # remove the "leaf" node in current graph state
        steps += 1
    dist_from_center_to_leave[island_num] = steps

    centers = list(degrees.keys())
    center_lists.append(centers)
    # All thats left in degrees are the centers (1 or 2 of them)
    q = deque(degrees.keys())
    # print(q)
    # bfs from the center and store the distance from center for each node
    steps = 0
    while q:
        nodes = len(q)
        for _ in range(nodes):
            node = q.popleft()
            if node in dist_to_center:
                continue
            dist_to_center[node] = steps # store distance from center
            for nbr in graph[node]:
                if nbr not in dist_to_center: # if not visited yet, add to queue
                    q.append(nbr)
        steps += 1
# print(dist_to_center)
# print(dist_from_center_to_leave)
# print(center_lists)
# print()

for _ in range(num_questions):
    start, end = map(int, input().split())
    start_island = get_island[start]
    end_island = get_island[end]
    mid_island = start_island ^ end_island # clever XOR logic - gets the unused island
    
    leave_start = dist_to_center[start] + dist_from_center_to_leave[start_island] + len(center_lists[start_island])
    enter_end = dist_to_center[end] + dist_from_center_to_leave[end_island] + len(center_lists[end_island])
    through_middle = 2 * dist_from_center_to_leave[mid_island] + len(center_lists[mid_island])

    # print(f'{leave_start} + {through_middle} + {enter_end}')
    print(leave_start + through_middle + enter_end)
    