r, c = map(int, input().split())
flag = False
for _ in range(r):
    word = input()
    dots = c - len(word)

    print('.' * (dots // 2), end='')

    if dots % 2 == 1:
        if flag:
            print('.', end='')
        print(word, end='')
        if not flag:
            print('.', end='')
        flag = not flag
    else:
        print(word, end='')
    
    print('.' * (dots // 2))
