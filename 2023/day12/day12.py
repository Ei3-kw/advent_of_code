from functools import cache
from time import time

start = time()

*lines, = open('12.txt')

C = cache(lambda l,r: r \
    and (t:=r[0]) \
    and ~sum(
        ~C(l[i+t+1:], r[1:]) 
            for i in range(len(l)-t+1) 
                if {'#'} - {l[i+t: i+t+1], *l[:i]}
                    and {'.'} - {*l[i:i+t]}) \
    or ~('#'in l)^1)

for n in 1, 5:
    print(sum(~C('?'.join(n*[l]), eval(r)*n) for l,r in map(str.split, lines)))
    print(time()-start)