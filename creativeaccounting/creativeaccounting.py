n, l, h = map(int, input().split())

days = [int(input()) for _ in range(n)]

prefix = [days[0]]
for i in range(1, len(days)):
    new_val = days[i] + prefix[i-1]
    prefix.append(new_val)
print(prefix)
