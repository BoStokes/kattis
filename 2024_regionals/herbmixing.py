green, red = map(int, input().split())
points = 0

while green >= 1 and red >= 1:
    points += 10
    green -= 1
    red -= 1
while green >= 3:
    points += 10
    green -= 3
while green >= 2:
    points += 3
    green -= 2
while green >= 1:
    points += 1
    green -= 1
print(points)