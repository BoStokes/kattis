from sys import*
setrecursionlimit(20000)
a = [z.strip() for z in stdin.readlines()]
i = 0
v = set()


def g(x, y):
    return (x, y-1), (x-1, y), (x+1, y), (x, y+1)
def n(s, x, y):
    return 0 <= x < len(s) and 0 <= y < len(s[x])
def dfs(s, x, y):
        if not n(s, x, y) or (x, y) in v or s[x][y] != '-':
            return
        v.add((x, y))
        for neighbor in g(x, y):
            dfs(s, neighbor[0], neighbor[1])

case_num = 1
while i < len(a):
    v = set()  
    m, n = map(int, a[i].split())
    s = [a[i] for i in range(i+1, i+m+1)]
    
   
    stars = 0
    for x in range(len(s)):
        for y in range(len(s[0])):
                if n(s, x, y) and (x, y) not in v:
                    a = s[x][y]
                    if a == '-':
                        stars += 1
                        dfs(s, x, y)

    print(f'Case {case_num}: {stars}')

    i += m + 1
    case_num += 1
