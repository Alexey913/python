# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

from random import sample


def fill_list(quantity_elements):
    num_list = sample(range(-quantity_elements*2, quantity_elements*2), k=quantity_elements)
    return num_list


def sum_elements(enter_list):
    sum_list = 0
    for i in range(0, len(enter_list), 2):
        sum_list += enter_list[i]
    return sum_list


print('Введите размер списка, я сформирую его из случайных чисел и выведу сумму элементов, стоящих на нечетных позициях')
N = int(input())
new_list = fill_list(N)
print('У нас получился такой список: \n', new_list)
print('Сумма элементов, стоящих на нечетных позициях: ',sum_elements(new_list))
