import re

if __name__ == '__main__':
    f = open("1.txt", "r")
    s = 0
    for line in f.readlines():
        s += int(line[re.search(r"\d", line).start()] + line[::-1][re.search(r"\d", line[::-1]).start()])

    print(s)

