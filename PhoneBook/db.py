# функции для работы с базой данных

# Запись контакта
def write_contact(cont1):
    with open("PhoneBook/data.txt","a", encoding = "utf-8") as file_in:
        file_in.write(cont1+"\n")

# Поиск контакта
def find_contact(cont2):
    with open("PhoneBook/data.txt","r", encoding = "utf-8") as file_in:
        list1 = file_in.readlines()
        list1 =[string.strip() for string in list1]
        count = 1
        for i in range(len(list1)):
            if cont2 in list1[i]:
                print(f'{i+1}. {list1[i]}')
                count +=1

#Показать весь справочник
def show_contacts():
     with open("PhoneBook/data.txt","r", encoding = "utf-8") as file_in:
         return file_in.read()