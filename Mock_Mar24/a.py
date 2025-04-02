n = int(input())
nums = list(map(int, input().split()))

stack = []
for num in nums:
    if not stack or stack[-1] != num  % 2:
        stack.append(num % 2)
    else:
        stack.pop()
print(len(stack))