from heapq import heappop, heappush

intersections, start, end = map(int, input().split())
distances = []
for _ in range(intersections):
    distances.append(list(map(int, input().split())))
final_distances = [-1 for _ in range(intersections)]

current_distances = []
heappush(current_distances, (0, start))
while current_distances:
    dist, index = heappop(current_distances)
    if final_distances[index] != -1:
        continue
    final_distances[index] = dist
    for i in range(intersections):
        if i == index:
            continue
        if final_distances[i] == -1:
            # try to improve distance f it is not final
            heappush(current_distances, (dist + distances[index][i], i))
print(final_distances[end])