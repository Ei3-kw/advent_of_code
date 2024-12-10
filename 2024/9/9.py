m = list(map(int, list(open("9.txt", "r").read().strip())))
l = []

for i in range(len(m)):
    if i%2:
        l.extend(['_']*m[i])
    else:
        l.extend([i//2]*m[i])

t = len(l) - 1


for a in range(len(l)):
    if l[a] == '_':
        while l[t] == '_':
            t -= 1
        l[a] = l[t]
        l[t] = '_'
        t -= 1
    if a >= t:
        break

s = 0
for a in range(len(l)):
    if l[a] == '_':
        break
    s += a*l[a]

print(s)


l = []

for i in range(len(m)):
    if i%2:
        l.extend(['_']*m[i])
    else:
        l.extend([i//2]*m[i])

def compact_filesystem(init):
    # Convert initial state to list of files
    fs = []
    curr = 0
    while curr < len(init):
        if init[curr] != '_':
            f = init[curr]
            start = curr
            while curr < len(init) and init[curr] == f:
                curr += 1
            fs.append((f, start, curr - start))
        else:
            curr += 1

    # Sort files by file ID in descending order
    fs.sort(key=lambda x: x[0], reverse=True)

    # Create mutable state to track filesystem
    state = init.copy()

    # Compact each file
    for f, start, length in fs:
        # Find leftmost free space that can accommodate this file
        best = None
        for left in range(len(state) - length + 1):
            if all(state[i] == '_' for i in range(left, left + length)):
                best = left
                break

        # If suitable space found, move file
        if best is not None and best < start:
            # Clear original position
            for i in range(start, start + length):
                state[i] = '_'

            # Place file in new position
            for i in range(length):
                state[best + i] = f

    return state

s = compact_filesystem(l)

print(sum(i * int(char) for i, char in enumerate(s) if s[i] != '_'))
