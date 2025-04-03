x1, y1, x2, y2 = map(int, input().split())

on_corner = 0
corners = ((0, 0), (0, 2024), (2024, 0), (2024, 2024))
if (x1, y1) in corners:
    on_corner += 1
if (x2, y2) in corners:
    on_corner += 1
print(2 - on_corner)