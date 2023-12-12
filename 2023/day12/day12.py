from functools import cache
from time import time

start = time()

*lines, = open('12.txt')

C = cache(lambda l,r: r \
    and (c:=r[0]) \
    and ~sum(
        ~C(l[i+c+1:], r[1:]) 
            for i in range(len(l)-c+1) 
                if {'#'} - {l[i+c: i+c+1], *l[:i]}
                    and {'.'} - {*l[i:i+c]}) \
    or ~('#'in l)^1)

for n in 1, 5:
    print(sum(~C('?'.join(n*[l]), eval(r)*n) for l,r in map(str.split, lines)))
    print(time()-start)