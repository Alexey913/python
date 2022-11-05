import excep
import interface
import log


def create_contact(num_book):
    surname_c = input ('Введите фамилию:\n')
    while excep.check_name_cont(surname_c) is False:
        print('Невернй ввод! Повторите')
        surname_c = input ('Введите фамилию:\n')
    
    name_c = input ('Введите имя:\n')
    while excep.check_name_cont(name_c) is False:
        print('Невернй ввод! Повторите')
        name_c = input ('Введите имя:\n')
    
    prot_c = input ('Введите отчество:\n') #намеренно не ставлю проверку отчества, учитывая, что пишется не всегда
    
    num_ph = excep.check_phone(input ('Введите номер телефона:\n'))
    while num_ph is False:
        num_ph = excep.check_phone(input ('Введите номер телефона:\n'))

    with open(*num_book, 'a', encoding='utf-8') as list_b:
        list_b.write(f'{surname_c}, {name_c}, {prot_c} - {num_ph}\n')
    list_b.close()
    print (f'Контакт сохранен в справочнике "{num_book}"!')
    log.universal_logger(f'{surname_c} {name_c} {prot_c}', data_description = "Создан контакт")


count_find_cont = 0    
def find_contact(num_book):
    with open(*num_book, 'r', encoding='utf-8') as book:
        data = book.readlines()
    
    def search(data):        
        flag = 1
        name = input('Введите имя, фамилию, или номер телефона:\n')
        global count_find_cont
        count_find_cont = 0
        for line in data:               
            if name in line:
                flag = 0
                count_find_cont+=1
                print(f"\033[32m {line} \033[39m")
                temp_cont = line
                log.universal_logger(name, data_description = "Поиск контакта")
        if flag:
            print('Совпадений не найдено')
            temp_cont = ''
            log.universal_logger(name, data_description = "Поиск контакта, совпадений не найдено")
        return temp_cont
    temp_cont = search(data)
    book.close()
    return temp_cont


def del_contact(num_book):
    print ('Какой контакт хотите удалить?')
    cont_for_del = find_contact(num_book)
    if cont_for_del == '':
        interface.main_menu()
    else:
        print ('Вы уверены?\n 1 - Да\n 2 - Нет')
        answer_del = excep.check_menu(3)
        if answer_del == 1:
            if count_find_cont == 1:
                with open(*num_book, 'r', encoding='utf-8') as book:
                    data = book.readlines()
                book.close()
                with open(*num_book, 'w', encoding='utf-8') as book:
                    for line in data:
                        if cont_for_del != line:
                            book.write(line)
                log.universal_logger(cont_for_del, data_description = "Удаление контакта")
                book.close()
            else:
                print (f'Найдено {count_find_cont} контактов! Уточните запрос!')
                log.universal_logger(cont_for_del, data_description = "Удаление не выполнено")
        else: interface.main_menu()