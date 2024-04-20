data = input().strip()
if data.isdigit():
    height = int(data)
    print(2**(height+1) - 1)
else:
    height, path = data.split()
    height = int(height)

    num = 0
    for dir in path:
        if dir == 'L':
            num = num*2 + 1
        else:
            num = num*2 + 2



    print(2**(height+1) - num - 1)