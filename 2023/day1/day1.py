import re

if __name__ == '__main__':
    d =  {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }

    s = 0 

    for line in open("1.txt", "r").readlines():
        l = line
        t = line[::-1]
        for i in range(len(line)):
            for k, v in d.items():
                if k in line[i:i+5]:
                    l = l.replace(k, v)
                    break
        for i in range(len(line)):
            for k, v in d.items():
                if k[::-1] in line[::-1][i:i+5]:
                    t = t.replace(k[::-1], v)
                    break
        s += int(l[re.search(r"\d", l).start()] + t[re.search(r"\d", t).start()])

    
    print("pt1: ", sum([int(line[re.search(r"\d", line).start()] + line[::-1][re.search(r"\d", line[::-1]).start()]) for line in open("1.txt", "r").readlines()]))
    print("pt2: ", s)

