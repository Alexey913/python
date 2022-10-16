import input_n
import log
import excep
import summ
import sub
import mult
import div

def check_menu(quan):
    ent_menu = (input())
    try:
        ent_menu = int(ent_menu)
        if not ent_menu in range(1,quan):
            print ('Неверный ввод! Повторите ввод:')
            check_menu(quan)
    except ValueError:
        print ('Неверный формат! Повторите ввод:')
        check_menu(quan)
    return (ent_menu)

def menu_1 ():
    print('Выберите пункт меню\n \
1 - Калькулятор\n 2 - Вывод логов на экран\n 3 - Выход')
    
def menu_2 ():
    print('С какими числами будем работать?\n \
1 - Целые\n 2 - Вещественные\n 3 - Комплексные')

def menu_3 ():
    print(f'Какое действие желаете выполнить с числами "{input_n.x}" и "{input_n.y}"?\n \
1 - Сумма\n 2 - Вычитание\n 3 - Умножение\n 4 - Деление\n\
 5 - Целочисленное деление\n 6 - Остаток от деления')

def end_prog ():
    print('Выполнение программы завершено. Спасибо!')

def res_action (ent_menu):
    res_action = {
              1: summ.summ(), 2: sub.sub(), 3: mult.mult(),
              4: div.float_div(), 5: div.floor_div(), 6: div.mod_div()}
    return res_action.get(ent_menu)

def action (ent_menu):
    action = {1: "Сумма", 2: "Разность", 3: "Произведение", 4: "Частное",
              5: "Частное от целочисленного деления", 6: "Остаток от деления"}
    return action.get(ent_menu)

print("Приветствую Вас в программе-калькуляторе!")
answer = 1
while answer == 1:
    menu_1()
    type_menu_1 = check_menu(4)
    if type_menu_1 == 1:
        
        menu_2()
        type_menu_2 = check_menu(4)
        if type_menu_2 == 1:
            input_n.int_num()
        elif type_menu_2 == 2:
            input_n.float_num()
        else:
            input_n.complex_num()
        
        menu_3()
        type_menu_3 = check_menu(7)
        print(f'{action(type_menu_3)} чисел {input_n.x} и {input_n.y} составляет {res_action(type_menu_3)}')
    
    elif type_menu_1 == 2:
        log.universal_logger(action(type_menu_1), data_description = "действие")
    else:
        end_prog()
        exit()
    print('\nХотите выполнить новую операцию?\n\
 1 - Да\n\
 2 - Нет')
    answer = check_menu(3)
else:
    end_prog()
