# Нужно найти Н-ое число Фибонначи:

# 0 1 2 3 4 5 6 7 8
# 0 1 1 2 3 5 8 13 21

# def f(n):
#     if n <=2:
#         return n
#     return f(n-1) + f(n-2)

# print(f(int(input('Введи N-ый элемент - '))))

# ------------------------------------------------------------------------------------------------------
# Заменить оценки в журнале все максимальные на минимальные

# Вход   1 2 3 4 3 2 3 4
# Выход  1 2 3 1 3 2 3 1

# n = int(input("Введи кол-во оценок  - "))
# list1 = []
# x = int(input(f"Введите 1-ю оценку - "))
# list1.append(x)
# max = x
# min = x
# for i in range(1,n):
#     x = int(input(f"Введите {i+1}-ю оценку - "))
#     if x < min:
#         min = x
#     if x >max:
#         max = x
#     list1.append(x)
# print(list1)

# for i in range(len(list1)):
#     if list1[i]==max:
#         list1[i]=min
# print(list1)

# - 2 вариант
# list1 = []
# n = int(input("Введи кол-во оценок  - "))
# for i in range(n):
#     x = int(input(f"Введите {i+1}-ю оценку - "))
#     list1.append(x)
# print(list1)

# for i in range(n):
#     if list1[i]==max(list1):
#         list1[i]=min(list1)
# print(list1)

# - 3 вариант
# n = int(input("Введи кол-во оценок  - "))
# list1 = [int(input(f"Введите {i+1}-ю оценку - ")) for i in range(n)]
# print(list1)
# min1 = min(list1)
# max1 = max(list1)
# list1 = [min1 if i==max1 else i for i in list1]
# print(list1)


# --------------------------------------------------------------------------
# проверить является ли число простым
# n = int(input("Введи число  - "))
# k=0
# for i in range(2,n):
#     if n % i == 0:
#         k+=1
# if k==0:
#     print('Число является простым')
# else:
#     print('Число не является простым')

# Дано натуральное число N и массив из N элементов.
# Вывести последовательность в обратном порядке без циклов и массивов

# in  3 4
# out 4 3



def f(n):
    if n == 0:
        return ''
    x = int(input(f"Введите число- "))
    return f(n - 1) + " " + str(x)

n = int(input("Введи количество символов  - "))
print(f(n))


#     if n <=2:
#         return n
#     return f(n-1) + f(n-2)

# print(f(int(input('Введи N-ый элемент - '))))
