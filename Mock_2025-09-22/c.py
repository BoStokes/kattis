message = input()
n = len(message)
first_half, second_half = [message[i] for i in range(n//2)], [message[i] for i in range(n//2, n)]

value = lambda c: ord(c) - ord('A')
letter = lambda n: chr(n + ord('A'))

rot = sum(value(c) for c in first_half)
for i in range(n//2):
    new_val = (value(first_half[i]) + rot) % 26
    first_half[i] = letter(new_val)

rot = sum(value(c) for c in second_half)
for i in range(n//2):
    new_val = (value(second_half[i]) + rot) % 26
    second_half[i] = letter(new_val)

add = lambda c1, c2: letter((value(c1) + value(c2)) % 26)
for c1, c2 in zip(first_half, second_half):
    print(add(c1, c2), end='')
print()