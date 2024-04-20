x, y = zip(*[map(int, input().split()) for _ in range(3)])
print(min(x, key=x.count), min(y, key=y.count))

