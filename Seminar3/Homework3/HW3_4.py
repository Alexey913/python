# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76


from random import uniform

def fill_list(quantity_elements):
    num_list=[]
    for i in range(quantity_elements):
        num_list.append (round(uniform(-quantity_elements*2, quantity_elements*2),3))
    return num_list

def pull_fraction (enter_list):
    for i in range (len(enter_list)):
        integer = abs(int(enter_list[i]))
        enter_list[i] = round((abs(enter_list[i])-integer), 3)
    return enter_list

def max_min_fraction (enter_list):
    maximum = enter_list[0]
    minimum = enter_list[0]
    for i in range (len(enter_list)):
        if enter_list[i] > maximum:
            maximum = enter_list[i] 
        elif enter_list[i] < minimum:
            minimum = enter_list[i]
        diff_max_min = round((maximum-minimum), 3)
    print('Разница между максимальным {} и минимальным {} значениями дробной части чисел равна {}'.format \
        (maximum, minimum, diff_max_min))

N = int(input('Введите размер списка:\n'))
my_list = fill_list(N)
print (my_list)
# my_list_fraction = pull_fraction(my_list)
# print (my_list_fraction)
max_min_fraction(pull_fraction(my_list))