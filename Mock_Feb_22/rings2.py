def lowest_neighbor(grid, r, c):
    if r == 0 or r == len(grid)-1 or c == 0 or c == len(grid[0])-1:
        return 1
    return min(grid[r-1][c], grid[r][c-1], grid[r][c+1], grid[r+1][c]) + 1

n, m = map(int, input().split())

ring_nums = [[0 if c == '.' else float('inf') for c in input()] for _ in range(n)]
num_rings = 0
for r in range(n):
    for c in range(m):
        if ring_nums[r][c] != 0:
            ring_nums[r][c] = lowest_neighbor(ring_nums, r, c)
            num_rings = max(num_rings, ring_nums[r][c])
for r in range(n-1, -1, -1):
    for c in range(m-1, -1, -1):
        if ring_nums[r][c] != 0:
            ring_nums[r][c] = lowest_neighbor(ring_nums, r, c)

if num_rings < 10:
    for line in ring_nums:
        for n in line:
            if n == 0:
                n = '.'
            print(f'{n:.>2}', end='')
        print()
else:
    for line in ring_nums:
        for n in line:
            if n == 0:
                n = '.'
            print(f'{n:.>3}', end='')
        print()


