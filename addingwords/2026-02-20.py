from sys import *
from collections import *

var_to_value = {}
value_to_var = {}

for line in stdin.readlines():
    statement, *tokens = line.split()

    if statement == 'def':
        var, val = tokens
        if var in var_to_value:
            del value_to_var[var_to_value[var]]
        var_to_value[var] = int(val)
        value_to_var[int(val)] = var
    
    elif statement == 'calc':
        itr = iter(tokens)

        total = 0
        op = '+'

        exists = True
        while op != '=':
            var = next(itr)
            print(var, end=' ')

            if var in var_to_value:
                total += var_to_value[var] if op == '+' else -var_to_value[var]
            else:
                exists = False

            op = next(itr)
            print(op, end=' ')
        
        if total in value_to_var and exists:
            print(value_to_var[total])
        else:
            print('unknown')
    
    else:
        var_to_value = {}
        value_to_var = {}