n = int(input())
qaly = 0
for _ in range(n):
    quality, years = map(float, input().split())
    qaly += quality*years
print(qaly)