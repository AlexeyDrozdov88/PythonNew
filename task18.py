# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X


list_1 = [1, 4, 3, 7, 8, 9, 2]
k = 8
near = list_1[0]
dif = abs(list_1[0] - k)

for i in range(1, len(list_1)):
    if abs(list_1[i] - k) < dif:
        near = list_1[i]
        dif = abs(list_1[i] - k)
print(near)
