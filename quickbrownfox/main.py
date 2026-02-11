from collections import *
from string import *

for _ in range(int(input())):
    line = input().lower()
    count = Counter(line)
    output = ''
    for c in ascii_lowercase:
        if count[c] == 0:
            output += c
    
    if len(output) > 0:
        print(f'missing {output}')
    else:
        print('pangram')