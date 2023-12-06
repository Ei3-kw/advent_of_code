import time

def map(t, x):
    for dst, src, n in t:
        if src <= x <src+n:
            return x + dst - src
    return x

def mapping(t, r):
    bruh = []
    for dst, src, n in t:
        new_r = []
        while r:
            stt, end = r.pop()
            b = (stt, min(end, src))
            i = (max(stt, src), min(src + n, end))
            a = (max(src + n, stt), end)
            new_r.extend(filter(lambda x: x[1] > x[0], [b, a]))
            bruh.append((i[0] - src + dst, i[1] - src + dst)) if i[1] > i[0] else None
        r = new_r
    return bruh + r


if __name__ == '__main__':
    start = time.time()
    seed, *others = open('5.txt').read().split('\n\n')
    seed = [int(x) for x in seed.split(':')[1].split()]

    p1 = []
    for x in seed:
        for pt in others:
            x = map([[int(x) for x in line.split()] for line in pt.split('\n')[1:]], x)
        p1.append(x)
    print(min(p1))

    p2 = []
    for m, n in zip(seed[::2], seed[1::2]):
        x = [(m, m+n)]
        for pt in others:
            x = mapping([[int(x) for x in line.split()] for line in pt.split('\n')[1:]], x)
        p2.append(min(x))
    print(min(p2)[0])

    print("time elapsed: ", time.time()-start)

