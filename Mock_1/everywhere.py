t = int(input())
for _ in range(t):
    cities = set()
    n = int(input())
    for _ in range(n):
        cities.add(input())
    print(len(cities))