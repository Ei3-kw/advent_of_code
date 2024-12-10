from itertools import combinations
from collections import defaultdict
from math import gcd


class T(tuple):
    def __add__(self, other):
        return T(x + y for x, y in zip(self, other))

    def __sub__(self, other):
        return T(x - y for x, y in zip(self, other))

    def __floordiv__(self, other):
        return T(x // other for x in self)


def p1(f):
    grid = {
        T((i, j)): c
        for i, r in enumerate(f.read().splitlines())
        for j, c in enumerate(r)
    }

    antennae = defaultdict(list)
    for p, c in grid.items():
        if c != ".":
            antennae[c].append(p)

    pos = set()

    for thing, ps in antennae.items():
        for a, b in combinations(ps, 2):
            pos.add(b + (b - a))
            pos.add(a + (a - b))

    return sum(p in grid for p in pos)


def p2(f):
    grid = {
        T((i, j)): c
        for i, r in enumerate(f.read().splitlines())
        for j, c in enumerate(r)
    }

    antennae = defaultdict(list)
    for p, c in grid.items():
        if c != ".":
            antennae[c].append(p)

    pos = set()

    for thing, ps in antennae.items():
        for a, b in combinations(ps, 2):
            diff = b - a
            diff //= gcd(*diff)
            while b in grid:
                pos.add(b)
                b += diff
            while a in grid:
                pos.add(a)
                a -= diff

    return len(pos)

print(p2(open('8.txt', 'r')))