def get_op():
    operation = int(input("Выберите действие: \n 1-импорт \n 2-экспорт \n 3-удаление/изменение \n 4-выход \n"))
    return operation

def get_data():
    name = input("Введите имя: \n")
    surname = input("Введите фамилию: \n")
    phone = input("Введите телефон в формате +7 без пробелов: \n")
    full_data= (surname + ' ' + name + ' ' + phone)+"\n"
    return full_data

def find_worker():
    data=input("Введите искомый параметр: ")
    return data