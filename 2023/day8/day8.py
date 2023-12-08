import numpy as np
d, _, *lines = open('8.txt').readlines()

meow = {k: v.strip()[1:-1].split(', ') for k, v in (l.split(' = ') for l in lines)}

current, i = 'AAA', 0
while current != 'ZZZ':
    for c in d[:-1]:
        if current == 'ZZZ': 
            break
        i += 1
        current = meow[current][0] if c == 'L' else meow[current][1]

print(i)

current = [m + n + 'A' for m in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

i = np.zeros(len(current), dtype=int)
for b, a in enumerate(current):
    if a in meow:
        while a[-1] != 'Z':
            for c in d[:-1]:
                if a[-1] == 'Z': 
                    break
                i[b] += 1
                a = meow[a][0] if c == 'L' else meow[a][1]

print(np.lcm.reduce(i[i != 0]))


