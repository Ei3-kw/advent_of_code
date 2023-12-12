lines = open("12.txt").read().splitlines()
from functools import lru_cache

@lru_cache(maxsize=None)
def possibilities(row, chunks):
    if len(chunks) == 0:
        return 1 if "#" not in row else 0
    n = chunks[0]
    total = 0
    for i in range(len(row)):
        if row[i] == ".":
            continue
        else:
            if "." not in row[i:i+n] and i+n <= len(row):
                if i+n == len(row) or row[i+n] != "#":
                    total += possibilities(row[i+n+1:],tuple(list(chunks)[1:]))
            if row[i] == "#":
                break

    return(total)

s1 = 0
s2 = 0

for line in lines:
    row, nums = line.split()
    chunks = []
    for c in nums:
        try:
            chunks.append(int(c))
        except ValueError:
            pass

    s1 += possibilities(row,tuple(chunks))
    s2 += possibilities("?".join([row]*5),tuple(chunks*5))

print(s1,s2)