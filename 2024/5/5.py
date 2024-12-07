import itertools

def valid(meow):
    for i in range(len(meow)):
        if meow[i] in d:
            for j in d[meow[i]]:
                if j in meow[:i]:
                    return False
    return True

mode = 1
d = {}
s = s2 = 0
for line in open("5.txt", "r").readlines():
    if not line.strip():
        mode = 0
        continue
    if mode:
        x, y = line.strip().split('|')
        if x in d:
            d[x].append(y)
        else:
            d[x] = [y]
    else:
        meow = line.strip().split(',')

        if valid(meow):
            s += int(meow[len(meow)//2])
        else:
            for na in list(itertools.permutations(meow)):
                if valid(na):
                    s2 += int(na[len(meow)//2])
                    break

print(s)
print(s2)





