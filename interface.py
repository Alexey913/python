import input_n
import log
import excep
import summ
import sub
import mult
import div

def menu_1 ():
    print('\nВыберите пункт меню\n \
1 - Калькулятор\n 2 - Вывод логов на экран\n 3 - Выход')
    type_menu_1 = excep.check_menu(4)
    if type_menu_1 == 1:
        log.universal_logger("Калькулятор", data_description = "Запуск")
        menu_3(menu_2())

    elif type_menu_1 == 2:
        log.universal_logger("Вывод логов на экран", data_description = "Запуск")        
        log.print_log()
    else:
        end_prog()


def menu_2 ():
    print('\nС какими числами будем работать?\n \
1 - Целые\n 2 - Вещественные\n 3 - Комплексные')
    type_menu_2 = excep.check_menu(4)
    if type_menu_2 == 1:
        log.universal_logger("Целые числа", data_description = "Выбор")
        input_n.int_num()
    elif type_menu_2 == 2:
        log.universal_logger("Вещественные числа", data_description = "Выбор")
        input_n.float_num()
    elif type_menu_2 == 3:
        log.universal_logger("Комплексные числа", data_description = "Выбор")
        input_n.complex_num()
    return type_menu_2


def menu_3 (type_menu_2):
    if type(input_n.x)==complex or type(input_n.y)==complex:
        print(f'\nКакое действие желаете выполнить с числами "{input_n.x}" и "{input_n.y}"?\n \
1 - Сумма\n 2 - Вычитание\n 3 - Умножение\n 4 - Деление')
    
    else:
        print(f'\nКакое действие желаете выполнить с числами "{input_n.x}" и "{input_n.y}"?\n \
1 - Сумма\n 2 - Вычитание\n 3 - Умножение\n 4 - Деление\n\
 5 - Целочисленное деление\n 6 - Остаток от деления')
 
    if type_menu_2 == 3:
        type_menu_3 = excep.check_menu(5)
    else:
        type_menu_3 = excep.check_menu(7)
    if type_menu_3 in range(1,4) or excep.excep_check_zero() is True:
        print(f'\n{action(type_menu_3)} чисел {input_n.x} и {input_n.y} составляет {res_action(type_menu_3)}')
    else:
        return excep.if_zero()

    
def res_action (ent_menu):
    if ent_menu == 1:
        return summ.summ()
    elif ent_menu == 2:
        return sub.sub()
    elif ent_menu == 3:    
        return mult.mult()
    elif ent_menu == 4:
        return div.float_div()
    elif ent_menu == 5:    
        return div.floor_div()
    else:    
        return div.mod_div()


def action (ent_menu):
    if type_menu_2 == 3:
        action = {1: "Сумма", 2: "Разность", 3: "Произведение", 4: "Частное"}
    else:
        action = {1: "Сумма", 2: "Разность", 3: "Произведение", 4: "Частное",
                  5: "Частное от целочисленного деления", 6: "Остаток от деления"}
    return action.get(ent_menu)
    
    
def end_prog ():
    print('\nВыполнение программы завершено. Спасибо!')
    log.universal_logger("по команде пользователя", data_description = "Выход") 
    exit()


print("Приветствую Вас в программе-калькуляторе!")

log.universal_logger("Вход в программу", data_description = "Запуск")
answer = 1
while answer == 1:
    menu_1()
    print('\nХотите выполнить новую операцию?\n\
 1 - Да\n\
 2 - Нет')
    answer = excep.check_menu(3)
else:
    end_prog()
