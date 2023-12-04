import ast
    
def compare(l1, l2):
    try:
        return l1 <= l2
    except TypeError:
        for j in range(min(len(l1), len(l2))):
            if type(l1[j]) == type(l2[j]):
                x, y = l1[j], l2[j]    
            elif isinstance(l1[j], int):
                x, y = [l1[j]], l2[j]    
            else:
                x, y = l1[j], [l2[j]]

            if not isinstance(x, int) and not isinstance(y, int):
                if len(x) < len(y):
                    return True
                if len(x) > len(y):
                    return False

            if not compare(x, y):
                return False
        return True

if __name__ == '__main__':
    f = open("13.txt", "r").read().split('\n\n')
    s=0
    for i in range(len(f)):
        l1, l2 = f[i].split('\n')
        l1 = ast.literal_eval(l1)
        l2 = ast.literal_eval(l2)
        
        print('\n', i+1)
        print(l1)
        print(l2)

        if compare(l1, l2):
            print(':turtlecat:\n')

            s += (i+1)

    print(s)

# from functools import cmp_to_key
# pairs = [[eval(a) for a in b.splitlines()] for b in open('13.txt').read().split('\n\n')]


# def compare(left, right):
#     l_int = isinstance(left, int)
#     r_int = isinstance(right, int)
#     if l_int and r_int:
#         return (left > right) - (left < right)
#     elif l_int and not r_int:
#         return compare([left], right)
#     elif not l_int and r_int:
#         return compare(left, [right])
#     else:
#         for a, b in zip(left, right):
#             if (comp := compare(a, b)) != 0:
#                 return comp
#         return (len(left) > len(right)) - (len(left) < len(right))


# results = {i: compare(*x) for i, x in enumerate(pairs)}
# print(sum([k + 1 for k, v in results.items() if v == -1]))

# packets = sorted([a for a, _ in pairs] + [b for _, b in pairs] + [[[2]], [[6]]],
#                  key=cmp_to_key(compare))
# print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))