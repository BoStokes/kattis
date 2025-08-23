from collections import deque

n, m, k = map(int, input().split())
memory = set()
for i in range(1, n+1):
    num = int(input())
    if i == k:
        currency = num
    else:
        memory.add(num)

operations = []
for i in range(1, m+1):
    op, val = input().split()
    operations.append((op, int(val))) # value, index of operation

q = deque() 
q.append((currency, 0, tuple())) # value, num operations, path
while q:
    val, num_ops, path = q.popleft()
    if val not in memory:
        print(num_ops)
        print(*path, sep='\n')
        exit()
    for i, data in enumerate(operations, start=1):
        op, v = data
        if op == '+': new_val = val + v
        elif op == '-': new_val = val - v
        elif op == '*': new_val = val * v
        elif op == '/': new_val = val // v

        if new_val < 0: continue

        q.append((new_val, num_ops+1, path+(i,)))
print(-1)