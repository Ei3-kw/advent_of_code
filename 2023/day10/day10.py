from collections import deque
import sys

sys.setrecursionlimit(999999999)


lines = open('10.txt').readlines()
lines = [l.strip() for l in lines]

class Node:
    def __init__(self, coord, t, n1=None, n2=None, n3=None, n4=None):
        self.coord = coord
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.t = t

    def __str__(self):
        return self.t

    def __repr__(self):
        return self.__str__()

grid = []

for k in range(len(lines)):
    grid.append([None] * len(lines[0]))

for i in range(len(lines)):
    for j in range(len(lines[0])):
        grid[i][j] = Node((i, j), lines[i][j])

d = {'-': [[-1, 0], [1, 0]],
     'L': [[0, -1], [1, 0]],
     'J': [[-1, 0], [0, -1]],
     'F': [[0, 1], [1, 0]],
     '|': [[0, 1], [0, -1]],
     '7': [[-1, 0], [0, 1]]
}

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if d.get(grid[i][j].t):
            d1, d2 = d.get(grid[i][j].t)
            j1, i1 = d1[0] + j, d1[1] + i
            if len(lines[0]) > j1 >= 0 and len(lines) > i1 >= 0:
                grid[i][j].n1 = grid[i1][j1]

            j2, i2 = d2[0] + j, d2[1] + i
            if len(lines[0]) > j2 >= 0 and len(lines) > i2 >= 0:
                grid[i][j].n2 = grid[i2][j2]
        elif grid[i][j].t == 'S':
            i1, j1 = i+1, j
            i2, j2 = i-1, j
            i3, j3 = i, j+1
            i4, j4 = i, j-1

            if len(lines) > i1 >= 0:
                grid[i][j].n1 = grid[i1][j1]
            if len(lines) > i2 >= 0:
                grid[i][j].n2 = grid[i2][j2]
            if len(lines[0]) > j3 >= 0:
                grid[i][j].n3 = grid[i3][j3]
            if len(lines[0]) > j4 >= 0:
                grid[i][j].n4 = grid[i4][j4]

def dfs(current_node, visited, path):
    if current_node.t == 'S' and path:
        return path

    if current_node in visited:
        return None

    visited.add(current_node)

    for neighbor in [current_node.n1, current_node.n2, current_node.n3, current_node.n4]:
        if neighbor:
            result = dfs(neighbor, visited, path + [neighbor.coord])
            if result:
                return result

    return None

def find_loop(start_node):
    visited = set()
    return dfs(start_node, visited, [])


# Find the starting node with 'S'
start_node = None
for row in grid:
    for node in row:
        if node.t == 'S':
            start_node = node
            break

if start_node:
    loop_path = find_loop(start_node)

    if loop_path:
        print("Loop found:", loop_path)
        print(len(loop_path)/2)
    else:
        print("No loop found.")
else:
    print("Starting node 'S' not found.")


def enclose(coord, path):
    if coord in path:
        return False
    x, y = coord
    x1 = x
    b1, b2 = False, False
    while x1 >= 0:
        if (x1, y) in path:
            b1 = not b1
        x1 -= 1

    x1 = x 
    while x1 <=len(lines[0]):
        if (x1, y) in path:
            b2 = not b2
        x1 += 1

    y1 = y
    c1, c2 = False, False
    while y1 >= 0:
        if (x, y1) in path:
            c1 = not c1
        y1 -= 1

    y1 = y
    while y1 <= len(lines):
        if (x, y1) in path:

            c2 = not c2
        y1 += 1

    # print(coord, [b1, b2, c1, c2])
    return all([b1, b2, c1, c2])

tiles = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if enclose((i, j), loop_path):
            tiles += 1

print(tiles)




