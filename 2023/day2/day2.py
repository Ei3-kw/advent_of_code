if __name__ == '__main__':
    s1 = s2 = 0

    for line in open("2.txt", "r").readlines():
        d = {'r': [0], 'b': [0], 'g': [0]}
        
        l = line.rstrip().split(': ')
        game = int(l[0][5:])

        for s in l[1].split('; '):
            for t in s.split(', '):
                value, color = map(str.strip, t.split(' '))
                d[color[0]].append(int(value))

        if max(d['r']) <= 12 and max(d['b']) <= 14 and max(d['g']) <= 13:
            s1 += game

        s2 += max(d['r']) * max(d['b']) * max(d['g'])

    print(s1)
    print(s2)


# 1931
# 83105
