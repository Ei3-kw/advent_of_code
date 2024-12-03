import re

mul = r'mul\(\d+,\d+\)'
do = r'do\(\)'
dont = r'don\'t\(\)'

ins = re.findall(f'{mul}|{do}|{dont}', open("3.txt", "r").read())

enabled = 1
s = 0
for i in ins:
    print(i)
    if i.startswith('mul(') and enabled:
        x, y = i[4:-1].split(',')
        s += int(x) * int(y)
    elif i == 'do()':
        enabled = 1
    elif i == 'don\'t()':

        enabled = 0

print(s)
    