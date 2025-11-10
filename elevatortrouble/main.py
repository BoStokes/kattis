from collections import deque


floors, start, goal, up, down = map(int, input().split())

visited = set()
q = deque()
q.append((start, 0))
visited.add(0)

while q:
    current, presses = q.popleft()
    if current == goal:
        print(presses)
        exit()

    if current + up <= floors and current + up not in visited:
        visited.add(current + up)
        q.append((current + up, presses + 1))
    if current - down > 0 and current - down not in visited:
        visited.add(current - down)
        q.append((current - down, presses + 1))

print("use the stairs")