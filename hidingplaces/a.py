from functools import cache
from collections import *
from itertools import permutations

def get_coords(location):
    return ord(location[0]) - ord('a'), int(location[1]) - 1
def get_location(x, y):
    return f'{chr(x + ord("a"))}{y+1}'

moves = [
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2)
]
def get_moves(x, y):
    return [(x+dx, y+dy) for dx, dy in moves if 0 <= x+dx < 8 and 0 <= y+dy < 8]


@cache
def main(location):
    q = deque()
    q.append(get_coords(location))
    visited = set()
    steps = -1
    while q:
        spots = []
        l = len(q)
        for _ in range(l):
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            spots.append(get_location(x,y))
            visited.add((x, y))

            for nbr_x, nbr_y in get_moves(x, y):
                if (nbr_x, nbr_y) not in visited:

                    q.append((nbr_x, nbr_y))
        steps += 1
    spots.sort(key=lambda pos: (-int(pos[1]), pos[0]))
    print(steps, *spots)

    


for _ in range(int(input())):
    main(input())