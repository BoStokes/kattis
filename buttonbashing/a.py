from collections import deque

for _ in range(int(input())):
    n, t = map(int, input().split())
    buttons = list(map(int, input().split()))
    if t == 0:
        print(0, 0)
        continue

    best = (float('inf'), -1)
    q = deque()
    visited = set()
    q.appendleft((0,0))
    visited.add(0)
    while q and best[0] != t:
        time, presses = q.pop()
        for i in range(n):
            new_time = time + buttons[i]
            if 0 <= new_time <= 3600 and new_time not in visited:
                if new_time == t:
                    best = (new_time, presses+1)
                    break
                visited.add(new_time)
                q.appendleft((new_time, presses+1))
                if new_time > t:
                    best = min(best, (new_time, presses+1))
    print(best[1], best[0]-t)