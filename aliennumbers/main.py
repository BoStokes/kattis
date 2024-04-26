from collections import deque
T = int(input())

for i in range(T):
    num, source, target = input().split()
    source_dict = {character: index for index, character in enumerate(source)}
    source_base = len(source_dict)
    target_base = len(target)

    base10 = 0
    for place, digit in enumerate(num[::-1]):
        base10 += source_dict[digit] * source_base**place
    
    translated = deque()

    while base10 > 0:
        value = base10 % target_base
        translated.appendleft(target[value])
        base10 //= target_base
    print(f'Case #{i+1}: {"".join(translated)}')


