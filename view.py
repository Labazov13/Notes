def get_op():
    operation = int(input("Выберите действие: \n 1-импорт \n 2-экспорт \n 3-удаление/изменение \n 4-выход \n"))
    return operation

def get_data():
    name = input("Введите заголовок заметки: \n")
    body = input("Введите тело заметки: \n")
    full_data= (name + ' ' + body)+"\n"
    return full_data

def find_post():
    data=int(input("Введите номер статьи (нумерация с 0): "))
    return data