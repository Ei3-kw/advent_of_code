g = {complex(i,j): c for j, r in enumerate(open('16.txt'))
                     for i, c in enumerate(r.strip())}

def fn(todo):
    done = set()
    while todo:
        pos, d = todo.pop()
        while not (pos, d) in done:
            done.add((pos, d))
            pos += d
            match g.get(pos):
                case '|': d = 1j; todo.append((pos, -d))
                case '-': d = -1; todo.append((pos, -d))
                case '/': d = -complex(d.imag, d.real)
                case '\\': d = complex(d.imag, d.real)
                case None: break

    return len(set(pos for pos, _ in done)) - 1

print(fn([(-1, 1)]))
print(max(map(fn, ([(pos-d, d)] 
    for d in (1, -1 ,1j, -1j)
    for pos in g if pos-d not in g))))
