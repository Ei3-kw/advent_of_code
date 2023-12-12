from functools import cache

*lines, = open('12.txt')

def possibility(l, r):
    return r \
    and (c:=r[0]) \
    and ~sum(
        ~C(l[i+c+1:], r[1:]) 
            for i in range(len(l)-c+1) 
                if {'#'} - {l[i+c: i+c+1], *l[:i]}
                    and {'.'} - {*l[i:i+c]}) \
    or ~('#'in l)^1

C = cache(lambda l,r: possibility(l, r))

for n in 1, 5:
    print(sum(~C('?'.join(n*[l]), eval(r)*n) for l,r in map(str.split, lines)))