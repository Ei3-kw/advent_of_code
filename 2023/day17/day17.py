# *lines, = open('16.txt')

DIR = [-1, 1j, 1, -1j]

g = {complex(i,j): c for j, r in enumerate(open('17.txt'))
                     for i, c in enumerate(r.strip())}

dst = list(g.keys())[-1]

def fn(todo):
    done = []
    total_cost = -int(todo[0][1])
    dirs = []
    while todo:
        pos, cost = todo.pop()
        loss = int(cost)
        cost = loss + norm(pos-list(g.keys())[-1])
        print(pos)

        if pos == dst:
            break

        while not (pos, cost) in done:
            l = [pos-1,pos+1j,pos+1,pos-1j]
            total_cost += cost
            if len(done) > 0:
                dirs.append(pos-done[-1][0])
            done.append((pos, cost))
            for i in range(4):
                if l[i] in g:
                    try:
                        if DIR[i-2] != dirs[-1] and not (DIR[i] == dirs[-1] == dirs[-2]):
                            todo.append((l[i], g[l[i]]))
                    except IndexError:
                        dirs.append(DIR[i])
                        todo.append((l[i], g[l[i]]))



    return total_cost 





                

            


print(fn([(0, 0)]))




# print(max(map(fn, ([(pos-dir, dir)] for dir in (1,1j,-1,-1j)
                        # for pos in g if pos-dir not in g))))



