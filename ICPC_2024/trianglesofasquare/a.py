x1, y1, x2, y2 = map(int, input().split())

corners = (0,0), (0, 2024), (2024, 0), (2024, 2024)

num_lines = 2
if (x1, y1) in corners:
    num_lines -= 1
if (x2, y2) in  corners:
    num_lines -= 1
print(num_lines)