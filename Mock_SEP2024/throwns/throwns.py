n, k = map(int, input().split())

stack = []
commands = input().split()

index = 0
while index < len(commands):
    command = commands[index]
    if command == 'undo':
        for _ in range(int(commands[index + 1])):
            stack.pop()
        index += 1
    else:
        stack.append(int(command))
    index += 1

print(sum(stack) % n)