
# # s = 0
# t = [ [] for _ in range(256) ]
# d = {}
# for b in range(256):
#     d[b] = []


# for i in open('15.txt').read().strip().split(','):
#     m = 0

#     for c in i:
#         m += ord(c)
#         m *= 17
#         m = m%256

#     t[m].append(i)
#     # s += m


# for i in t:
#     for c in i:
#         if '=' in c:

#         if '-' in c:

# Initialize boxes
boxes = {i: [] for i in range(256)}

# Parse and process initialization sequence
# initialization_sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

#!/bin/python3

import sys
from typing import DefaultDict, List
from collections import defaultdict

FILE = '15.txt'


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(line.split(","))

    return lines[0]


def run_hash(s: str) -> int:
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value %= 256

    return value


def part_one():
    ops = read_lines_to_list()
    answer = 0

    for op in ops:
        answer += run_hash(op)

    print(f"Part 1: {answer}")


def part_two():
    ops = read_lines_to_list()
    answer = 0

    boxes: DefaultDict[int, List[str, int]] = defaultdict(list)

    for op in ops:
        if "-" in op:
            val = op[:-1]
            hash = run_hash(val)

            for i in reversed(range(len(boxes[hash]))):
                if boxes[hash][i][0] == val:
                    boxes[hash].pop(i)

        elif "=" in op:
            [val, focal] = op.split("=")
            focal = int(focal)
            hash = run_hash(val)

            for lens in boxes[hash]:
                if lens[0] == val:
                    lens[1] = focal
                    break
            else:
                boxes[hash].append([val, focal])

    for key, lenses in boxes.items():
        for itx, lens in enumerate(lenses):
            val = (key + 1) * (itx + 1) * lens[1]
            answer += val

    print(f"Part 2: {answer}")


part_one()
part_two()
