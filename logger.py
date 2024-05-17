
from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные \n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))


    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")

      
def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def modify_data():
    name_to_modify = input("Введите данные для изменения или удаления: ")

    
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()

    
    with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
        for i in range(len(data_first)):
            if name_to_modify in data_first[i]:
                action = input("Выберите 'change' для изменения или 'delete' для удаления данных: ")
                if action == 'change':
                    new_data = input("Введите новые данные: ")
                    data_first[i] = new_data + '\n'
                elif action == 'delete':
                    data_first[i] = ''
        f.writelines(data_first)

 
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()

   
    with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
        for i in range(len(data_second)):
            if name_to_modify in data_second[i]:
                action = input("Выберите 'change' для изменения или 'delete' для удаления данных: ")
                if action == 'change':
                    new_data = input("Введите новые данные: ")
                    data_second[i] = new_data + '\n'
                elif action == 'delete':
                    data_second[i] = ''
        f.writelines(data_second)