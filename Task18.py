# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
number1 = int(input('Введите количество элементов: '))
lst1 = [randint(1, 100) for i in range(number1)]
print(lst1)

number2 = int(input('Близкий по величине элемент к числу: '))

inp_set = set(lst1)
temp = 0
if number2 > max(inp_set):
    print(max(inp_set))
elif number2 < min(inp_set):
    print(min(inp_set))
else:
    while True:
        if number2 - temp in inp_set and number2 + temp in inp_set and number2 - temp != number2 + temp:
            print(number2 - temp, number2 + temp)
            break
        elif number2 - temp in inp_set:
            print(number2 - temp)
            break
        elif number2 + temp in inp_set:
            print(number2 + temp)
            break
        else:
            temp += 1
