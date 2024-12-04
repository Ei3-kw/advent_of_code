import re

xmas = rf"(?=(XMAS|SAMX))"

s = 0


grid = open("4.txt", "r").readlines()
# for line in grid:
#     s += len(re.findall(xmas, line))

# for col in range(len(line)):
#     s += len(re.findall(xmas, ''.join(line[col] for line in grid)))


# n = len(grid)

# # top-left <-> bottom-right
# for sr in range(n):
#     line = ''.join(grid[sr + i][i] for i in range(n - sr))
#     s += len(re.findall(xmas, line))

# for sc in range(1, n):
#     line = ''.join(grid[i][sc + i] for i in range(n - sc))
#     s += len(re.findall(xmas, line))


# # Anti-diagonals (top-right <-> bottom-left)
# for sr in range(n):
#     line = ''.join(grid[sr + i][n - 1 - i] for i in range(n - sr))
#     s += len(re.findall(xmas, line))

# for sc in range(n - 1, -1, -1):
#     line = ''.join(grid[i][sc - i] for i in range(n - (n - sc)))
#     s += len(re.findall(xmas, line))

with open('4.txt') as f:
    data = f.read()
    rows = data.splitlines()
    column_lists = ["".join(col) for col in zip(*rows)]
    padded_grid1 = [" " * i + row + " " * (len(rows) - i - 1) for i, row in enumerate(rows)]
    padded_grid2 = [" " * i + row + " " * (len(rows) - i - 1) for i, row in enumerate(rows[::-1])]
    diagonals1 = [''.join(chars).strip() for chars in zip(*padded_grid1)]
    diagonals2 = [''.join(chars).strip() for chars in zip(*padded_grid2)]

    for c in rows + column_lists + diagonals1 + diagonals2:
        matches = re.findall(xmas, c)
        s += int(len(matches))

print(s)

s = 0
for i in range(len(grid)):
    for j in range(len(grid[0].strip())):
        if grid[i][j] == 'A':
            if i-1 >=0 and j-1 >= 0 and i+1 < len(grid) and j+1 < len(grid[0].strip()):
                if (grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S') or (grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M'):
                    if (grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S') or (grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M'):
                        s += 1
print(s)
