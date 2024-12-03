from math import prod
from igraph import Graph

G = {v: e.split() for v,e in [l.split(':')
                  for l in open('25.txt')]}

print(prod(Graph.ListDict(G).mincut().sizes()))