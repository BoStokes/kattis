n, m = map(int, input().split())
houses = [i for i in range(n+1)]
connections = [map(int, input().split()) for _ in range(m)]

def find(x):
    if houses[x] == x:
        return x
    houses[x] = find(houses[x])
    return houses[x]
def union(x, y):
    houses[find(x)] = find(y)

for house_num1, house_num2 in connections:
    union(house_num1, house_num2)

disconnected = []
for house_num, house in enumerate(houses):
    if house_num != 0 and find(house_num) != find(1):
        disconnected.append(house_num)
if disconnected:
    print(*disconnected, sep='\n')
else:
    print('connected')