ps = list(map(str.split, open('13.txt').read().split('\n\n')))

def f(p, t):
    for i in range(len(p)):
        if sum(x != y 
            for l, m in zip(p[i-1::-1], p[i:])
            for x, y in zip(l, m)) == t:
            return i
    return 0

for t in 0, 1: 
    print(sum(100 * f(p, t) + f(list(zip(*p)), t) for p in ps))
