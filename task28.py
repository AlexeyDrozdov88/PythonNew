# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.


def sum(a, b):
    if a == 0:
        return b
    return 1 + sum(a - 1, b)


a = int(input("Введи a  - "))
b = int(input("Введи b  - "))
print(sum(a, b))
