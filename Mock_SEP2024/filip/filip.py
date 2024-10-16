line = input()

reverse = line[::-1]  # reverse = str(reversed(line))

num1, num2 = map(int, reverse.split())

print(max(num1, num2))