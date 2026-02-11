grid = [input() for _ in range(5)]

nbrs = (1,-2), (2,-1), (2,1), (1,2)
def check(r, c):
    for dr, dc in nbrs:
        if 0 <= r+dr < 5 and 0 <= c+dc < 5 and grid[r+dr][c+dc] == 'k':
            return False
    return True
    
count = 0

for r in range(5):
    for c in range(5):
        if grid[r][c] == 'k':
            count += 1
            if check(r, c) == False:
                print('invalid')
                exit()
if count != 9:
    print('invalid')
else:
    print('valid')