n = int(input())
words = [input() for _ in range(n)]

if n < 3:
    print(0)
    exit()

dice1, dice2, dice3 = [], [], []

for word in words:
    pass