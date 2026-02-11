from math import ceil

for _ in range(int(input())):
    line = input()
    n = len(line)
    side_len = ceil(n**0.5)
    
    grid = []
    i = 0
    for _ in range(side_len):
        grid.append([])
        for _ in range(side_len):
            grid[-1].append(line[i] if i < n else '*')
            i += 1

    grid = [list(row)[::-1] for row in zip(*grid)]


    print(''.join(c for c in ''.join(''.join(row) for row in grid) if c != '*'))