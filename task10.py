# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть.
#
# Пример:
# 5 -> 1 0 1 1 0
# 2

from random import randint
number = int(input('Введите количество монеток: '))
coin_num = []
for _ in range(number):
    coin_num.append(randint(0, 1))
print(coin_num)

if coin_num.count(0) < coin_num.count(1):
    print(coin_num.count(0))
else:
    print(coin_num.count(1))




