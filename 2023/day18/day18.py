lava = [(0, 0)]
vala = [(0, 0)]
d = {'R': (1, 0), 'D': (0, -1), 'L': (-1, 0), 'U': (0, 1)}

s1 = p1 = s2 = p2 = 0

for i, j, k in (map(str.split, open("18.txt").readlines())):
    x, y = lava[-1]
    m, n = vala[-1]
    x, y = x + d[i][0]*int(j), y + d[i][1]*int(j)
    lava.append((x, y))
    s1 += (lava[-2][0] - x) * (lava[-2][1] + y)
    p1 += int(j)

    a = list(d.values())[int(k[-2])]
    m, n = m + a[0]*int(k[2:-2], 16), n + a[1]*int(k[2:-2], 16)
    vala.append((m, n))
    s2 += (vala[-2][0] - m) * (vala[-2][1] + n)
    p2 += int(k[2:-2], 16)


# To account for the four corners you miss
print(abs(s1/2) + p1/2+1)
print(abs(s2/2) + p2/2+1)
