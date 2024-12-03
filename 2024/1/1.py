l = []
r = []
for line in open("1.txt", "r").readlines():
	x, y = line.split('   ')
	l.append(int(x))
	r.append(int(y))

# l.sort()
# r.sort()
# s = 0
# for i in range(len(l)):
# 	s += abs(r[i]-l[i])


s = 0
for i in l:
	s += r.count(i) * i

print(s)



