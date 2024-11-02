from sys import stdin

for num in map(lambda n: int(n.strip()), stdin.readlines()):
    a = 1
    num_digits = 1
    while a % num != 0:
        # a = a * 10 + 1
        # identity: (a * 10 + 1) % n == ((a % n) * 10 + 1) % n
        a = (a % num) * 10 + 1
        num_digits += 1
    print(num_digits)
    