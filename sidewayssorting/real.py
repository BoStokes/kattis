r, c = map(int, input().split())
while r != 0:
    grid = []
    for _ in range(r):
        grid.append(input())
    words = [''.join(word) for word in zip(*grid)]
    words.sort(key=lambda s:s.lower())
    print(*(''.join(word) for word in zip(*words)), sep='\n')
    r, c = map(int, input().split())
    if r != 0:
        print()