n = int(input())
while n != 0:
    print(*sorted([input() for _ in range(n)], key=lambda x:x[:2]), sep='\n')
    print()
    n = int(input())