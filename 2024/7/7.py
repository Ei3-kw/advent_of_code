s = 0

for line in open('7.txt', 'r').readlines():
	tgt, nums = line.split(': ')
	tgt = int(tgt)
	nums = list(map(int, nums.strip().split(' ')))

	for i in range(2**(len(nums)-1)):
		i = f"{i:0{len(nums)-1}b}"
		x = nums[0]
		for j in range(len(nums)-1):
			if i[j] == '1':
				x *= nums[j+1]
			else:
				x += nums[j+1]
		if x == tgt:
			s += tgt
			break

print(s)

import numpy as np


s = 0

for line in open('7.txt', 'r').readlines():
	tgt, nums = line.split(': ')
	tgt = int(tgt)
	nums = list(map(int, nums.strip().split(' ')))

	for i in range(3**(len(nums)-1)):
		i = np.base_repr(i, base=3)
		i = (len(nums)-1-len(i))*'0' + i

		x = nums[0]
		for j in range(len(nums)-1):
			if i[j] == '2':
				x = int(str(x) + str(nums[j+1]))
			elif i[j] == '1':
				x *= nums[j+1]
			else:
				x += nums[j+1]
		if x == tgt:
			s += tgt
			break

print(s)

