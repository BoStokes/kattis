students, _ = map(int, input().split())

throws = []
commands = input().split()
index = 0

while index < len(commands):
    command = commands[index]
    if command == 'undo':
        for _ in range(int(commands[index + 1])):
            throws.pop()
        index += 1
    else:
        throws.append(int(command))
    index += 1

print(sum(throws) % students)