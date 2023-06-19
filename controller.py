import view
import database

def main():
    while True:
        operation = view.get_op()
        if operation == 1:
            data_worker = view.get_data()
            database.add_data(data_worker)

        if operation == 2:
            change = int(input("1-весь список\n2-выборочно\n"))
            if change == 1:
                database.export_all_data()
            else:
                find_str = view.find_post()
                database.find_post(find_str)

        if operation == 3:
            change = int(input("1-удаление\n2-изменение\n"))
            if change == 1:
                change = int(input("1-удаление записи\n2-удаление всего журнала\n"))
                if change == 1: 
                    database.remove_post()
                else:
                    database.delete_all_data()
            else:
                database.change_data()

        if operation == 4:
            break

main()
