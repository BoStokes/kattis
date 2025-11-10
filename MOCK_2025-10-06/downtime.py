from collections import *
from math import *
from sys import stdin

n, k = map(int, input().split())

lines = [int(line.strip()) for line in stdin.readlines()]
low = lines[0]
high = lines[-1]

start = Counter()
end = Counter()
for time in lines:
    start[time] += 1
    end[time+1000] += 1

active = 0
most = 0
for t in range(low, high+1001):
    active += start[t]
    active -= end[t]
    most = max(most, active)

print(ceil(most / k))