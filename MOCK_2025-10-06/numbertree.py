from sys import stdin

inp = input()
space = inp.find(' ')

h = int(inp[:space])
path = inp[space+1:]

num = 1
for dir in path:
    num = num * 2 + (dir == 'R')

print(2**(h+1) - num)