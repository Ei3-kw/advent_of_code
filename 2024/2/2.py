s = 0
for line in open("2.txt", "r").readlines():
	nya = 0
	l = [int(i) for i in line.split(' ')]
	dec = (l[0] > l[1])
	for i in range(1, len(l)):
		if dec:
			if l[i-1] - l[i] > 3 or l[i] >= l[i-1]:
				nya = 1
				break
		else:
			if l[i] - l[i-1] > 3 or l[i] <= l[i-1]:
				nya = 1
				break
	if not nya:
		s += 1

print(s)

s = 0
for line in open("2.txt", "r").readlines():

	l = [int(i) for i in line.split(' ')]
	ls = []
	for j in range(len(l)):
		ls.append([l[i] for i in range(len(l)) if i != j])

	for l in ls:
		nya = 0
		dec = (l[0] > l[1])
		for i in range(1, len(l)):
			if dec:
				if l[i-1] - l[i] > 3 or l[i] >= l[i-1]:
					nya = 1
					break
			else:
				if l[i] - l[i-1] > 3 or l[i] <= l[i-1]:
					nya = 1
					break
		if not nya:
			s += 1
			break


print(s)


