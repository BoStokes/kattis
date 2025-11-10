from sys import stdin, stdout
input = stdin.readline
output = []

N, Q = map(int, input().split())

tree = [0] * (N+1)


def query(index):
    total = 0
    while index > 0:
        total += tree[index]
        index -= (index & -index)
    return total

def update(index, value):
    while index <= N:
        tree[index] += value
        index += (index & -index)

for _ in range(Q):
    op = input().rstrip()
    if op[0] == '+':
        idx, val = map(int, op[2:].split())
        update(idx+1, val)

    else:
        idx = int(op[2:])
        output.append(str(query(idx)))
stdout.write('\n'.join(output))