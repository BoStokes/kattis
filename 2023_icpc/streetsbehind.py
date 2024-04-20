from math import floor, ceil
import sys
sys.setrecursionlimit(1_000_000_000)
# c = a / b
# (y + 1) / c
def convert(ser, cas, a, b, count):
    if cas == 0:
        return count
    n = find_best(ser, cas, a, b)
    return convert(ser+n, cas-n, a, b, count+1)

def find_best(ser, cas, a, b):
    n = floor((b*ser - a*ser) / a)
    if n >= cas:
        return cas
    return n

t = int(input())

for _ in range(t):
    ser, cas, a, b = map(int, input().split())
    if ser / (ser+1) < a/b:
        print(-1)
        continue

    print(convert(ser, cas, a, b, 0))