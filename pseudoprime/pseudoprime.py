from math import floor, sqrt

while True:
    p, a = map(int, input().split())
    if p == 0 and a == 0:
        break
    for i in range(2, floor(sqrt(p)) + 1):
        if p % i == 0:
            if pow(a, p, p) == a:
                print('yes')
            else:
                print('no')

            break
    else:
        print('no')
    