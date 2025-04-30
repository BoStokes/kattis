lines = [
    '1 4 3 4 5 6',
    '1 0',
]

for line in lines:
    x, n, *l = map(int, line.split())
    print(x, n, l)