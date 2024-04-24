with open('3.in', 'w') as file:
    file.write('2000\n2000\n')
    file.write(' '.join(map(str,range(2,2*2000 + 1, 2))))
    file.write('\n')
    file.write(' '.join(map(str,range(3,3*2000 + 1, 3))))
    file.write('\n')
