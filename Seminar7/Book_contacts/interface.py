from timeit import repeat
import excep
import log
import books
import contacts


def repeat_menu ():
    print('\nХотите выполнить новую операцию?\n \
1 - Да\n \
2 - Нет')
    answer = excep.check_menu(3)
    if answer == 1:
        return main_menu()
    else:
        end_prog()


def book_list():
    print ('Выберите пункт меню:\n 1 - Вывести перечень справочников\n 2 - Главное меню\n 3 - Выход')
    type_book_list = excep.check_menu(4)
    if type_book_list == 1:
        books.print_book_list()
        repeat_menu()
    elif type_book_list == 2:
        main_menu()
    else:
        end_prog()


def create_book_list():
    print ('Выберите пункт меню:\n 1 - Создать новый справочник\n 2 - Главное меню\n 3 - Выход')
    type_create_book = excep.check_menu(4)
    if type_create_book == 1:
        books.create_book()
        repeat_menu()
    elif type_create_book == 2:
        main_menu()
    else:
        end_prog()


def open_book():
    print ('Выберите пункт меню:\n 1 - Открыть справочник\n 2 - Главное меню\n 3 - Выход')
    type_book_list = excep.check_menu(4)
    if type_book_list == 1:
        books.open_book()
        repeat_menu()
    elif type_book_list == 2:
        main_menu()
    else:
        end_prog()
        
        
def del_book_list():
    print ('Выберите пункт меню:\n 1 - Удалить справочник\n 2 - Главное меню\n 3 - Выход')
    type_del_book = excep.check_menu(4)
    if type_del_book == 1:
        books.print_book_list()
        books.del_book()
        repeat_menu()
    elif type_del_book == 2:
        main_menu()
    else:
        end_prog()


def add_cont():
    print ('Выберите пункт меню:\n 1 - Выбрать справочник\n 2 - Главное меню\n 3 - Выход')
    type_book_list = excep.check_menu(4)
    if type_book_list == 1:
        contacts.create_contact(books.open_book_for_work())
        repeat_menu()
    elif type_book_list == 2:
        main_menu()
    else:
        end_prog()


def find_book_cont():
    print ('Выберите пункт меню:\n 1 - Выбрать справочник\n 2 - Главное меню\n 3 - Выход')
    type_book_list = excep.check_menu(4)
    if type_book_list == 1:
        contacts.find_contact(books.open_book_for_work())
        repeat_menu()
    elif type_book_list == 2:
        main_menu()
    else:
        end_prog()
        
        
def del_cont():
    print ('Выберите пункт меню:\n 1 - Выбрать справочник\n 2 - Главное меню\n 3 - Выход')
    type_book_list = excep.check_menu(4)
    if type_book_list == 1:
        contacts.del_contact(books.open_book_for_work())
        repeat_menu()
    elif type_book_list == 2:
        main_menu()
    else:
        end_prog()


def end_prog ():
    print('\nВыполнение программы завершено. Спасибо!')
    log.universal_logger("по команде пользователя", data_description = "Выход") 
    exit()


def main_menu():
    print('Какое действие Вы хотите выполнить?\n \
1 - Вывести список справочников\n 2 - Создать новый справочник\n \
3 - Открыть справочник\n 4 - Удалить справочник\n 5 - Добавить контакт\n 6 - Поиск контактов\n 7 - Удалить контакт\n 8 - Выход')

    type_main_menu = excep.check_menu(9)

    if type_main_menu == 1:
        return book_list()
    elif type_main_menu == 2:
        return create_book_list()
    elif type_main_menu == 3:
        return open_book()
    elif type_main_menu == 4:
        return del_book_list()
    elif type_main_menu == 5:
        return add_cont()
    elif type_main_menu == 6:
        return find_book_cont()
    elif type_main_menu == 7:
        return del_cont()
    else:
        end_prog()
        
main_menu()