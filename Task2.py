# Задача 2
# Найдите сумму цифр трехзначного числа.
#
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))
num_three = number % 10
num_one = number // 100
num_two = (number // 10) % 10

print(num_one + num_two + num_three)