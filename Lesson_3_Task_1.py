print("\033[H\033[J", end="")

def sum_number(n, y='Значение по-умолчанию.'):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
    print('Данный текст не выведется.')
print(sum_number(10, 'Данный передаваемый аргумент перебьёт значение по-умолчанию.'))