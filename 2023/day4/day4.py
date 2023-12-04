

# if __name__ == '__main__':
#     lines = open("4.txt", "r").read().split('\n')

#     a = 0
#     f = 0

#     d = {}

#     for l in lines:
#         l = l.split(': ')
#         d[int(l[0][5:])] = 1

#     for l in lines:
#         m = -1

#         l = l.split(': ')
#         i = int(l[0][5:])
#         w, n = l[1].split(' | ')
#         w = w.strip().split(' ')
#         n = n.strip().split(' ')

#         for t in n:
#             if t in w and len(t)>0:
#                 m += 1
        
#         if m >= 0:
#             a += 2**m

#         for j in range(i+1, i+m+2):
#             if d.get(j):
#                 d[j] += d[i]

#     for k, v in d.items():

#         f += v

#     print(a, f)

if __name__ == '__main__':
    lines = [l.split(': ') for l in open("4.txt", "r").read().split('\n')]
    d = {int(l[0][5:]): 1 for l in lines}

    a = f = 0

    for l in lines:
        i = int(l[0][5:])
        w, n = map(str.split, l[1].split(' | '))
        m = sum(1 for t in n if t in w and t) - 1

        a += 2**m if m >= 0 else 0

        for j in range(i + 1, i + m + 2):
            if d.get(j): 
                d[j] += d[i]

    f = sum(v for v in d.values())

    print(a, f)


    
    