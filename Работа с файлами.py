#open(папка/input.txt,"r")
#r - чтение
#w - создание/запись + уничтожение предыдущих записей
#a - создание/запись без уничтожения записей

# file = open("input.txt","a", encoding = "utf-8")
# file.write("Заебал\n") # запись строки
# a = ["45\n","gdfgfd\n","салют\n"]
# file.writelines(a) #запись элементоа списка в файл
# file.close()


# with open("input.txt","w", encoding = "utf-8") as file1:
#           a = ["45\n","gdfgfd\n","салют\n"]
#           file1.writelines(a) # запись элементоа списка в файл

with open("input.txt","r", encoding = "utf-8") as file1:
    # list1 = file1.readlines() # берем из файла в список  - каждый элемент списка это строка в файле
    file1.seek(0) #- возвращает курсов на нулевую позицию
    # list1 =[string.strip() for string in list1]
    # print(list1)
    # print(file1.readlines())
    # print(file1.read()) возвращает все как одну строку
    # print(file1.readline(10)) #читает файл построчно
    