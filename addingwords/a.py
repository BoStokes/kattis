from sys import stdin
from operator import add, sub

var_to_num = dict()
num_to_var = dict()


lines = [line.strip() for line in stdin.readlines()]
ops = {
    '+': add,
    '-': sub
}
for instr in lines:
    line = instr.split()
    if line[0] == 'def':
        var, num = line[1], int(line[2])
        var_to_num[var] = num
        num_to_var[num] = var
    elif line[0] == 'calc':
        val = 0
        op = '+'
        i = 1
        while op != '=':
            var = line[i]
            if var not in var_to_num:
                ans = 'unknown'
                break
            val = ops[op](val, var_to_num[var])
            op = line[i+1]
            i += 2
        else:
            if val not in num_to_var:
                ans = 'unknown'
            else:
                ans = num_to_var[val]
        print(f'{" ".join(line[1:])} {ans}')
    else:
        var_to_num.clear()
        num_to_var.clear()