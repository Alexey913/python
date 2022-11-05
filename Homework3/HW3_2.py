# # 2. Напишите программу, которая найдёт произведение пар чисел списка.
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

from random import sample
import math

def fill_list(quantity_elements):
    num_list = sample(
        range(-quantity_elements, quantity_elements), k=quantity_elements)
    return num_list

def multiplicate_couple(enter_list):
    quantity_elements = len(enter_list)
    for i in range(int(quantity_elements/2)):
        enter_list[i] = enter_list[i]*enter_list[quantity_elements-1-i]
        del enter_list[quantity_elements-1-i]
    return enter_list

print('Введите размер списка, я сформирую его из случайных чисел и премножу попарно его элементы')
N = abs(int(input()))
new_list = fill_list(N)
print('У нас получился такой список: \n', new_list)
print('Новый список произведений элементов таков:\n',
      multiplicate_couple(new_list))