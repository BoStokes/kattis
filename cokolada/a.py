K = int(input())

n = 1
while n < K:
    n *= 2
print(n, end=' ')


breaks = 0
total = 0
need = K
while need > 0:
    if need >= n:
        total += n
        need -= n
    if need == 0:
        break
    breaks += 1
    n //= 2
print(breaks)
