from math import dist, sin, cos, radians

def get_dest(x, y, directions):
    angle = radians(float(directions[1]))
    state = 'start'
    for instr in directions[2:]:
        if instr == 'turn' or instr == 'walk':
            state = instr
            continue
        if state == 'turn':
            angle += radians(float(instr))
        if state == 'walk':
            dist = float(instr)
            dx, dy = dist * cos(angle), dist * sin(angle)
            x += dx
            y += dy
    return x, y

        


while True:
    n = int(input())
    if n == 0:
        exit()

    positions = []
    total_x, total_y = 0, 0
    for _ in range(n):
        x, y, *dirs = input().split()
        dest_x, dest_y = get_dest(float(x), float(y), dirs)
        positions.append((dest_x, dest_y))
        total_x += dest_x
        total_y += dest_y
    avg = (total_x / n, total_y / n)
    worst = max(map(lambda x: dist(x, avg), positions))
    print(*avg, worst)
    