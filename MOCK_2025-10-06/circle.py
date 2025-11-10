from math import dist
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if dist(points[i], points[j]) == 2018:
            print(points[i], points[j])