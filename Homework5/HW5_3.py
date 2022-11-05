def paint_board(list_res):
    fields = [1,2,3,4,5,6,7,8,9]
    for i in range (0,9):
        if list_res[i] in range(10):
            fields[i] = ' ' + str(list_res[i])
        else:
            fields[i] = list_res[i]

    print(f'\
о----о----о----о\n\
| {fields[0]} | {fields[1]} | {fields[2]} |\n\
о----+----+----о\n\
| {fields[3]} | {fields[4]} | {fields[5]} |\n\
о----+----+----о\n\
| {fields[6]} | {fields[7]} | {fields[8]} |\n\
о----о----о----о')

def check_enter_name(n_1, n_2):
    if n_1 == n_2:
        return 0
    else:
        return 1


def check_enter_field(num):
    while True:
        try:
            while int(num) not in range (10):
                print ('\nНеверный ввод! Повторите ввод:\n')
                num = (input())
            return int(num)
        except ValueError:
            print ('\nНеверный формат! Повторите ввод:')
            num = (input())


def check_enter(answ):
    while True:
        try:
            while int(answ) not in range (3):
                print ('\nНеверный ввод! Повторите ввод:\n')
                answ = (input())
            return int(answ)
        except ValueError:
            print ('\nНеверный формат! Повторите ввод:')
            answ = (input())


def check_win(list_res):
    if list_res[0] == list_res[1] == list_res[2] or\
       list_res[3] == list_res[4] == list_res[5] or\
       list_res[6] == list_res[7] == list_res[8] or\
       list_res[0] == list_res[3] == list_res[6] or\
       list_res[1] == list_res[4] == list_res[7] or\
       list_res[2] == list_res[5] == list_res[8] or\
       list_res[0] == list_res[4] == list_res[8] or\
       list_res[2] == list_res[4] == list_res[6]:
        return 1
    else:
        return 0

def steps (user_name, list_res, fig):
    print (f'{user_name}, делайте свой ход (введите номер незанятого поля):\n')
    step = check_enter_field(input())
    if step in range(10):
        while list_res[step-1] not in range(10):
            print ('Поле занято! Повторите ввод!')
            step = int(input())
        else:
            list_res[step-1] = fig
            paint_board(list_res)
            print ('Отлично!')
    return list_res

def game ():
    name_1 = input ('Введите имя первого игрока:\n')
    name_2 = input ('Введите имя второго игрока:\n')
    while check_enter_name (name_1, name_2) == 0:
        print ('Имена не должны совпадать!')
        name_2 = input ('Введите имя второго игрока:\n')

    list_res = [1,2,3,4,5,6,7,8,9]
    paint_board(list_res)
    count_steps = 1
    while count_steps < 10:
        if check_win(list_res) == 0:
            if count_steps%2 != 0:
                figure = '❌'
                steps(name_1, list_res, figure)
            else:
                figure = '⭕'
                steps(name_2, list_res, figure)
            count_steps+=1   
        else:
            if count_steps%2 != 0:
                print (f"ПОЗДРАВЛЯЮ! {name_2} ВЫИГРАЛ!")
            else:
                print (f"ПОЗДРАВЛЯЮ! {name_1} ВЫИГРАЛ!")
            repeat_menu()
    else:
        if check_win(list_res) == 1:
            print (f"ПОЗДРАВЛЯЮ! {name_1} ВЫИГРАЛ!")
        else:
            print ('ИГРА ЗАВЕРШЕНА! НИЧЬЯ!')
        repeat_menu()

def repeat_menu():
    print ('Сыграть еще раз? 1 - Да / 2 - Нет')
    while check_enter(input()) == 1:
        game()
    else:
        print ('Приходите еще!')
        exit()

print ('Добро пожаловать в игру "Крестики-нолики"\n')

game()