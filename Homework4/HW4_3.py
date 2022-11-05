# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

import random

def form_list (quntity):
    list_num = []
    for i in range (quntity):
        list_num.append (random.randint(0,quntity))
    return list_num

def delete_repeat (user_list):

    for i in range (len(user_list)):
        if user_list.count(user_list[i])>1:
            temp = user_list[i]
            for j in range (i, len(user_list)):
                if user_list[j] == temp:
                    user_list[j] = -1
    while -1 in user_list:
        user_list.remove(-1)
    return user_list

user_number = int(input('Введите размер списка, и я заполню его случайными числами:\n'))
user_list = form_list(user_number)
print (user_list)
print ('А теперь я удалю элементы списка, количество которых больше одного')
print (delete_repeat(user_list))
