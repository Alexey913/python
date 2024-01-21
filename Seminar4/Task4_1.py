# Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве разделителя используйте пробел.


def check_string (line):
    str = line.split()
    for i in str:
        if not i.strip('-').isdigit():
            return []
    return str


def max_min (enter_list):
    if enter_list: # проверяем, есть ли что-то в списке
        return min(enter_list, key=int), max(enter_list, key=int)
    else:
        return ('Uncorrect')

list_user = check_string("2 25 65 -8 kl")
print (list_user)
print (max_min(list_user)) 