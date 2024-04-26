
from random import shuffle
x = list(range(100))
shuffle(x)
for n in x:
    print(n,end='')
    input()
