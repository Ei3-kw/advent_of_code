import numpy as np


def drop(stack, skip=None):
    tops = np.zeros((12,12))
    falls = 0

    for i, (u,v,w, x,y,z) in enumerate(stack):
        if i == skip: continue
        h = z-w+1

        peak = tops[u:x+1, v:y+1].max()
        tops[u:x+1, v:y+1] = peak+h

        stack[i] = u,v,peak+1, x,y,peak+h
        falls += peak+1 < w

    return not falls, falls


bricks = np.fromregex('22.txt', r'\d+',
            [('',int)]).reshape(-1, 6).astype(int)
bricks = bricks[bricks[:, 2].argsort()]

drop(bricks)

print(*np.sum([drop(bricks.copy(), i)
    for i in range(len(bricks))], axis=0))