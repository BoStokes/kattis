from sys import stdin
from collections import deque

line = lambda: next(stdin).strip()

numsticks, lines = map(int, line().split())
sticks_on_top = [0] * numsticks
graph = [[] for _ in range(numsticks)]
for _ in range(lines):
    top, bottom = map(int, line().split())
    graph[top-1].append(bottom-1)
    sticks_on_top[bottom-1] += 1

available = deque()
for stick_num, on_top in enumerate(sticks_on_top):
    if on_top == 0:
        available.append(stick_num)

topo_order = []
while available:
    curr_stick = available.popleft()
    topo_order.append(curr_stick + 1)
    for stick in graph[curr_stick]:
        sticks_on_top[stick] -= 1
        if sticks_on_top[stick] == 0:
            available.append(stick)

for num in sticks_on_top:
    if num > 0:
        print('IMPOSSIBLE')
        exit()

print(*topo_order, sep='\n')