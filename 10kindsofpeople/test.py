n = 1000

with open('test.in', 'w') as f:
    f.write(f'{n} {n}\n')
    for _ in range(n):
        f.write(f'{"0"*n}\n')
    f.write('1\n')
    f.write(f'1 1 {n} {n}')