string = input()

pos = ['', 'A','B','C','AB','BC','AC','ABC']
counts = {key : 0 for key in pos}

priority = {
    'A': ['BC', 'B', 'C', ''],
    'B': ['AC', 'A', 'C', ''],
    'C': ['AB', 'A', 'B', '']
}

most_strings_seen = 0
for c in string:
    for target in priority[c]:
        if counts[target] > 0:
            new_location = ''.join(sorted(target + c))
            counts[new_location] += 1
            counts[target] -= 1
            break
    current = 0
    for i in counts:
        if i == '' or i == 'ABC':
            continue
        current += counts[i]
    most_strings_seen = max(most_strings_seen, current)
print(most_strings_seen)