from math import isclose
x, y = map(int, input().split())
n = int(input())
shield_barriers = []
shield_values = []
for i in range(n):
    shield = input().split()
    shield_barriers.append(int(shield[0]))
    shield_barriers.append(int(shield[1]))
    shield_values.append(float(shield[2]))

def position(speed):
    height = 0
    pos = 0
    in_shield = False
    idx = 0
    modifier = 1
    while height < y:
        if idx < n * 2:
            if not in_shield:
                if height >= shield_barriers[idx]:
                    in_shield = True
                    modifier = shield_values[idx // 2]
                    idx += 1
            else:
                if height >= shield_barriers[idx]:
                    in_shield = False
                    modifier = 1
                    idx += 1
            # if height >= shield_barriers[idx]:
            #     if not in_shield:
            #         in_shield = True
            #         modifier = shield_values[idx // 2]
            #     else:
            #         in_shield = False
            #         modifier = 1
            #     idx += 1
        pos += speed * modifier
        height += 1
    return pos, height


# speed = x / 2
# increment = x / 4
# ending_pos = position(speed)[0]
# while not isclose(ending_pos, x):
#     i += 1
#     if ending_pos > x:
#         speed -= increment
#     else:
#         speed += increment
#     increment /= 2
#     ending_pos = position(speed)[0]

# print(speed)

# print(position(1.0))

print(position(1.96078431373))
# print(position(1.33333333333))