import numpy as np

def geo(l):
    return len(l) <= 1 or all(l[i + 1] - l[i] == l[1] - l[0] for i in range(len(l) - 1))


s = 0

for line in open('9.txt').readlines():
    m = [int(a.strip()) for a in line.split()]

    t = 0
    j = [m]
    while not geo(m):
        t += 1
        m = [m[i + 1] - m[i] for i in range(len(m) - 1)]
        j.append(m)

    j[-1] = [j[-1][0] - (j[-1][-1]-j[-1][-2])] + j[-1]

    for e in reversed(range(len(j) - 1)):
        j[e] = [j[e][0] - j[e + 1][0]] + j[e]


    s += j[0][0]


print(s)
