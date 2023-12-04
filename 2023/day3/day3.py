# 560670 91622824


SYMBOLS = "!@#$%^&*()_+=-|[];':<>,?/`~"


def neighbors(f, k, cols, symbols):
    for d in [-cols-1, -cols, -cols+1, -1, 1, cols-1, cols, cols+1]:
        if 0 <= k+d < len(f) and f[k+d] in symbols:
            return k+d


if __name__ == '__main__':
    lines = open("3.txt", "r").read().split('\n')
    cols, f = len(lines[0]), ''.join(lines)
    m = {t: [] for t in range(len(f)) if f[t] == '*'}
    s = i = 0

    while i < len(f):
        if f[i].isdigit():
            j = i
            t = ''
            while j // cols == i // cols and f[j].isdigit():
                t += f[j]
                j += 1

            for k in range(i, i + len(t)):
                if neighbors(f, k, cols, SYMBOLS) is not None:
                    s += int(t)
                    break
            # s += int(t) if (result := next((neighbors(f, k, cols, SYMBOLS) for k in range(i, i + len(t)) if neighbors(f, k, cols, SYMBOLS) is not None), None)) is not None else 0


            for k in range(i, i + len(t)):
                if neighbors(f, k, cols, '*') is not None:
                    m[neighbors(f, k, cols, '*')].append(int(t))
                    break
            # m[next((neighbors(f, k, cols, '*') for k in range(i, i + len(t)) if neighbors(f, k, cols, '*') is not None), None)].append(int(t)) if next((neighbors(f, k, cols, '*') for k in range(i, i + len(t)) if neighbors(f, k, cols, '*') is not None), None) is not None else None

            i += len(t)
        else:
            i += 1


    print(s, sum(v[0] * v[1] for v in m.values() if len(v) == 2))

