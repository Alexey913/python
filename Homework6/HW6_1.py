# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import sample

def form_user_list (user_quantity):
    return sample(range(-user_quantity, user_quantity), k = quantity)
    
def form_list_upper_el (num_list):
    return [num_list[i] for i in range(1, len(num_list)) if num_list[i]>num_list[i-1]]
    
quantity = int(input('Введите количество элементов массива:\n'))

new_list = form_user_list(quantity)    
print (new_list)
print (f'Искомый массив:\n{form_list_upper_el(new_list)}')