from sys import stdin
from collections import deque


lines = [line.strip() for line in stdin]

index = 0
visited = set()


def get_neighbors(row, col):
    return (row-1, col), (row, col-1), (row, col+1), (row+1, col)
def in_bounds(sky, row, col):
    return 0 <= row < len(sky) and 0 <= col < len(sky[row])


case_num = 1
while index < len(lines):
    m, n = map(int, lines[index].split())
    index += 1
    sky = [lines[i] for i in range(index, index+m)]
    
    visited = set()
    stars = 0
    for row in range(len(sky)):
        for col in range(len(sky[0])):
            if (row, col) in visited or sky[row][col] != '-':
                continue
            stack = [(row, col)]
            stars += 1
            while stack:
                current_row, current_col = stack.pop()
                if sky[row][col] != '-' or (row, col) in visited:
                    continue
                for neighbor in get_neighbors(current_row, current_col):
                    stack.append(neighbor)
                    if in_bounds(sky, current_row, current_col) and sky[current_row][current_col] == '-' and (current_row, current_col) not in visited:
                        visited.add((current_row, current_col))


    print(f'Case {case_num}: {stars}')

    index += m
    case_num += 1
