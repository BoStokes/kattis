import math
height, max_degrees = map(int, input().split())

length = height/math.sin(math.radians(max_degrees))
print(math.ceil(length))