from collections import Counter

for i in range(1, 6):
    n = int(input())
    if n == 0:
        break
    animals = []
    for _ in range(n):
        animals.append(input().split()[-1].lower())
    counted = Counter(animals)
    print(f'List {i}:')
    for a in sorted(counted):
        print(f'{a} | {counted[a]}')
