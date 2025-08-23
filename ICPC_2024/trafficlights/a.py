n = int(input())
lights = [tuple(map(int, input().split())) for _ in range(n)]
status = [False] * n
time = 0
while True:
    time += 1
    num_green = 0
    for i, light_data in enumerate(lights):
        red_time, green_time = light_data
        cycle_duration = time % (red_time+green_time)
        if cycle_duration >= red_time:
            status[i] = True
            num_green += 1
        else:
            status[i] = False

    if num_green == n:
        print(time)
        exit()