from math import atan

p = int(input())

for i in range(p):
  ax,ay, bx,by, cx,cy = map(float, input().split()[1:])

  angle_a = atan(ay/ax)
  angle_b = atan(by/bx)
  angle_c = atan(cy/cx)

  angle_ab = angle_a - angle_b
  angle_bc = angle_b - angle_c
  angle_ca = angle_c - angle_a

  angles = list(map(abs, (angle_ab, angle_bc, angle_ca)))
  print(i, sum(angles)/3)
