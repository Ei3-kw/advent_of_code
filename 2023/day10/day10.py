# from collections import deque
# import sys

# sys.setrecursionlimit(999999999)


# lines = open('10.txt').readlines()
# lines = [l.strip() for l in lines]

# class Node:
#     def __init__(self, coord, t, n1=None, n2=None, n3=None, n4=None):
#         self.coord = coord
#         self.n1 = n1
#         self.n2 = n2
#         self.n3 = n3
#         self.n4 = n4
#         self.t = t

#     def __str__(self):
#         return self.t

#     def __repr__(self):
#         return self.__str__()

# grid = []

# for k in range(len(lines)):
#     grid.append([None] * len(lines[0]))

# for i in range(len(lines)):
#     for j in range(len(lines[0])):
#         grid[i][j] = Node((i, j), lines[i][j])

# d = {'-': [[-1, 0], [1, 0]],
#      'L': [[0, -1], [1, 0]],
#      'J': [[-1, 0], [0, -1]],
#      'F': [[0, 1], [1, 0]],
#      '|': [[0, 1], [0, -1]],
#      '7': [[-1, 0], [0, 1]]
# }

# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if d.get(grid[i][j].t):
#             d1, d2 = d.get(grid[i][j].t)
#             j1, i1 = d1[0] + j, d1[1] + i
#             if len(lines[0]) > j1 >= 0 and len(lines) > i1 >= 0:
#                 grid[i][j].n1 = grid[i1][j1]

#             j2, i2 = d2[0] + j, d2[1] + i
#             if len(lines[0]) > j2 >= 0 and len(lines) > i2 >= 0:
#                 grid[i][j].n2 = grid[i2][j2]
#         elif grid[i][j].t == 'S':
#             i1, j1 = i+1, j
#             i2, j2 = i-1, j
#             i3, j3 = i, j+1
#             i4, j4 = i, j-1

#             if len(lines) > i1 >= 0:
#                 grid[i][j].n1 = grid[i1][j1]
#             if len(lines) > i2 >= 0:
#                 grid[i][j].n2 = grid[i2][j2]
#             if len(lines[0]) > j3 >= 0:
#                 grid[i][j].n3 = grid[i3][j3]
#             if len(lines[0]) > j4 >= 0:
#                 grid[i][j].n4 = grid[i4][j4]

# def dfs(current_node, visited, path):
#     if current_node.t == 'S' and path:
#         return path

#     if current_node in visited:
#         return None

#     visited.add(current_node)

#     for neighbor in [current_node.n1, current_node.n2, current_node.n3, current_node.n4]:
#         if neighbor:
#             result = dfs(neighbor, visited, path + [neighbor.coord])
#             if result:
#                 return result

#     return None

# def find_loop(start_node):
#     visited = set()
#     return dfs(start_node, visited, [])


# # Find the starting node with 'S'
# start_node = None
# for row in grid:
#     for node in row:
#         if node.t == 'S':
#             start_node = node
#             break

# if start_node:
#     loop_path = find_loop(start_node)

#     if loop_path:
#         print("Loop found:", loop_path)
#         print(len(loop_path)/2)
#     else:
#         print("No loop found.")
# else:
#     print("Starting node 'S' not found.")


# def enclose(coord, path):
#     if coord in path:
#         return False
#     x, y = coord
#     x1 = x
#     b1, b2 = False, False
#     while x1 >= 0:
#         if (x1, y) in path:
#             b1 = not b1
#         x1 -= 1

#     x1 = x 
#     while x1 <=len(lines[0]):
#         if (x1, y) in path:
#             b2 = not b2
#         x1 += 1

#     y1 = y
#     c1, c2 = False, False
#     while y1 >= 0:
#         if (x, y1) in path:
#             c1 = not c1
#         y1 -= 1

#     y1 = y
#     while y1 <= len(lines):
#         if (x, y1) in path:

#             c2 = not c2
#         y1 += 1

#     # print(coord, [b1, b2, c1, c2])
#     return all([b1, b2, c1, c2])

# tiles = 0
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if enclose((i, j), loop_path):
#             tiles += 1

# print(tiles)






P="10.txt"
with open(P,"r") as f:
    R=f.read()
G=R.split("\n")
H=len(G)
W=len(G[0])

O = [[0]*W for _ in range(H)] # part 2

ax = -1
ay = -1
for i in range(H):
    for j in range(W):
        if "S" in G[i]:
            ax=i
            ay=G[i].find("S")

# rightward downward leftward upward
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
happy = ["-7J", "|LJ", "-FL", "|F7"]
Sdirs = []
for i in range(4):
    pos = dirs[i]
    bx = ax+pos[0]
    by = ay+pos[1]
    if bx>=0 and bx<=H and by>=0 and by<=W and G[bx][by] in happy[i]:
        Sdirs.append(i)
Svalid = 3 in Sdirs # part 2

# rightward downward leftward upward
transform = {
    (0,"-"): 0,
    (0,"7"): 1,
    (0,"J"): 3,
    (2,"-"): 2,
    (2,"F"): 1,
    (2,"L"): 3,
    (1,"|"): 1,
    (1,"L"): 0,
    (1,"J"): 2,
    (3,"|"): 3,
    (3,"F"): 0,
    (3,"7"): 2,
}

curdir = Sdirs[0]
cx = ax + dirs[curdir][0]
cy = ay + dirs[curdir][1]
ln = 1
O[ax][ay] = 1 # Part 2
while (cx,cy)!=(ax,ay):
    O[cx][cy] = 1 # Part 2
    ln += 1
    curdir = transform[(curdir,G[cx][cy])]
    cx = cx + dirs[curdir][0]
    cy = cy + dirs[curdir][1]
print(ln//2)

# End Part 1
# Begin Part 2

ct = 0
for i in range(H):
    inn = False
    for j in range(W):
        if O[i][j]:
            if G[i][j] in "|JL" or (G[i][j]=="S" and Svalid): inn = not inn
        else:
            ct += inn
print(ct)
