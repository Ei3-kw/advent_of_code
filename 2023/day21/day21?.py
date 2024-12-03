g = {complex(i,j): c for j, r in enumerate(open('21?.txt')) for i, c in enumerate(r.strip())}

DIM = 11

d = [-1, 1, 1j, -1j]


for k, v in g.items():
    if v == 'S':
        start = k

pos = {start}
for _ in range(50):
    meow = set()    
    for t in pos:
        for i in d:
            m = complex((t+i).real%DIM,(t+i).imag%DIM)
            if g[m] in '.S':
                meow.add(t+i)

    pos = meow


print(len(pos))


