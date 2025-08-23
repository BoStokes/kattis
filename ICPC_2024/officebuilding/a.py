rows, cols = map(int, input().split())
tree_heights = [[*map(int, input().split())] for _ in range(rows)]

plan_rows, plan_cols = map(int, input().split())
floor_plan = [input() for _ in range(plan_rows)]

def get_ages_sum(plan, r, c):
    s = 0
    for i in range(rows):
        for j in range(cols):
            if i < r or i >= r+len(plan) or j < c or j >= c+len(plan[0]) or floor_plan[i-r][j-c] == '.':
                s += tree_heights[i][j]
    # print(s)
    return s
best_sum = 0
for _ in range(4):
    floor_plan = list(zip(*floor_plan[::-1]))
    for i in range(rows - len(floor_plan) + 1):
        for j in range(cols - len(floor_plan[0]) + 1):
            best_sum = max(best_sum, get_ages_sum(floor_plan, i, j))
# print()
print(best_sum)