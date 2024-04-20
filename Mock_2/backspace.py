line = input()
stack = []
for c in line:
    if c == '<':
        if stack:
            stack.pop()
    else:
        stack.append(c)
print(''.join(stack))