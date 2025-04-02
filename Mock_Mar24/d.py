N, K = map(int, input().split())
mem = [0] * (N+1)

# FENWICK TREE / BINARY INDEXED TREE https://cp-algorithms.com/data_structures/fenwick.html
tree = [0] * (N+1)

# Gets sum in range [0, r]
def getsum(r):
    res = 0
    while r >= 0:
        res += tree[r]

        # operation g(j) (to get to next item in tree maybe? idk)
        # remove all trailing binary ones: eg. 1011 becomes 1000
        r = (r & (r+1)) - 1
    return res
def sumrange(l, r):
    return getsum(r) - getsum(l-1)

def change(idx, delta):
    while idx < len(tree):
        tree[idx] += delta # change node with desired operation

        # must iterate over all  j's, such that  g(j) <= i <= j
        # flips last unset bit
        idx = idx | (idx+1)

for _ in range(K):
    instr = input().split()
    if instr[0] == 'F':
        idx = int(instr[1])
        if mem[idx] == 0:
            mem[idx] = 1
            change(idx, 1)
        else:
            mem[idx] = 0
            change(idx, -1)
    elif instr[0] == 'C':
        l, r = int(instr[1]), int(instr[2])
        print(sumrange(l, r))