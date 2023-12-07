lines = open('7.txt').readlines()

# pt1
rank = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
meow = []
for l in lines:
    h, b = map(str.strip, l.split())
    d = max([h.count(c) for c in h], default=0)
    meow.append((d, 
        (d == 2) * sum(1 for c in set(h) if h.count(c) == d) + \
        + (d == 3) * any(h.count(c) == 2 for c in set(h)),
        *[-rank.index(c) for c in h], 
        int(b)))

print(sum((i + 1) * values[-1] for i, values in enumerate(sorted(meow))))

# pt2
rank = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
meow = []
for l in lines:
    h, b = map(str.strip, l.split())
    d = max([h.count(c) for c in h if c != 'J'], default=0) + h.count('J')
    r = next((c for c in h if h.count(c) == d - h.count('J') and c != 'J'), None)

    meow.append((d, 
        (d == 2) * sum(1 for c in set(h) if h.count(c) == d and c != 'J') + ('J' in h) \
        + (d == 3) * any(h.count(c) == 2 and c != 'J' and c != r for c in set(h)),
        *[-rank.index(c) for c in h], 
        int(b)))

print(sum((i + 1) * values[-1] for i, values in enumerate(sorted(meow))))

# 248569531
# 250382098


