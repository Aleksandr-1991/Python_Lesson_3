print("\033[H\033[J", end="")

def sum_str(*args):
    res=''
    for i in args:
        res += i
    return res

print(sum_str('q', 'w', 'l'))
print(sum_str('q', 'w', 'l', 'r', 'f'))

# т.о. м-объединять строки, но не числа.