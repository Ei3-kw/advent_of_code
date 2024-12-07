grid = [list(line.strip()) for line in open("6.txt", "r").readlines()]
n = len(grid)
m = len(grid[0])
obs = []
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
p = set()
p2 = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] in "^>v<":
            start = guard = (i,j)
            p.add(guard)
            d = "^v<>".index(grid[i][j])
        if grid[i][j] == '#':
            obs.append((i,j))

# while guard[0] in range(n) and guard[1] in range(m):
#     x, y = DIR[d]
#     x += guard[0]
#     y += guard[1]
#     if (x, y) in obs:
#         d += 1
#         d %= 4
#     else:
#         guard = x, y
#         p.add(guard)

# print(len(p)-1)

for o_r in range(n):
    for o_c in range(m):
        if (o_r, o_c) in obs:
            continue
        obs_ = obs + [(o_r,o_c)]
        SEEN = set()
        guard = start
        while guard[0] in range(n) and guard[1] in range(m):
            if (guard[0],guard[1],d) in SEEN:
                p2 += 1
                break
            SEEN.add((guard[0],guard[1],d))
            x, y = DIR[d]
            x += guard[0]
            y += guard[1]
            if (x, y) in obs_:
                d = (d+1)%4
            else:
                guard = x, y


print(p2)


