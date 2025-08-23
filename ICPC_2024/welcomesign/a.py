r, c = map(int, input().split())

c_parity = c % 2
add_right = True

for _ in range(r):
    word = input()
    word_parity = len(word) % 2

    if c_parity != word_parity:
        centered = f'{word:.^{c-1}}'
        if add_right:
            print(centered + '.')
        else:
            print('.' + centered)
        add_right = not add_right
    else:
        print(f'{word:.^{c}}')