n, k = map(int, input().split())
commands = iter(input().split())

stack = []

while k > 0:
    c = next(commands)
    k -= 1
    if c == 'undo':
        for _ in range(int(next(commands))):
            stack.pop()
    else:
        stack.append(int(c))

print(sum(stack) % n)