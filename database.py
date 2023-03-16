import view

def add_data(full_data):
    with open("file.txt", "a", encoding = "UTF-8") as file:
        file.write(full_data)

def find_worker(find_str):
    with open("file.txt", "r", encoding = "UTF-8") as file:
        list_str = file.readlines()
        for worker in list_str:
            if find_str in worker:
                print(worker)

def remove_worker():
    with open("file.txt", "r+", encoding = "UTF-8") as file:
        list_str = file.readlines()
        list_worker = []
        for worker in list_str:
            list_worker.append(worker)
            print(worker)

    with open("file.txt", "w", encoding = "UTF-8") as file:   
        number = int(input('Введите номер записи (нумерация с 0), которую необходимо удалить: '))
        for i in range(len(list_worker)):
            if number == i:
                continue
            file.writelines(list_worker[i])
    print("Готово!")
        
def export_all_data():
    with open("file.txt", "r", encoding = "UTF-8") as file:
        list_str = file.readlines()
        for worker in list_str:
            print(worker)

def delete_all_data():
    with open("file.txt", "w", encoding = "UTF-8") as file:
        print("Готово!")

def change_data():
    with open("file.txt", "r+", encoding = "UTF-8") as file:
        list_str = file.readlines()
        list_worker = []
        for worker in list_str:
            list_worker.append(worker)
            print(worker)

    with open("file.txt", "w", encoding = "UTF-8") as file:   
        number = int(input('Введите номер записи (нумерация с 0), которую необходимо изменить: '))
        for i in range(len(list_worker)):
            if number == i:
                list_worker[i] = view.get_data()
            file.writelines(list_worker[i])
    print("Готово!")
    
        

