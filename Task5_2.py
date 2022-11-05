# Дан список чисел. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность.
# Менять порядок элементов нельзя

# in 8

# out 
# [10 0 5 11 6 1 15 10]
# [10 11 15]   [0 5 11 15]
# [5 11 15] [11 15] [6 15]
# [1 15]

from random import choices

def get_list (size):
    return choices (range(size*2), k=size)

def form_equences (enter_list):
    new_list = []
    for i in range (len(enter_list)):
        max = enter_list[i]
        temp_list = [max]
        for j in range (i+1, len(enter_list)):
            if enter_list[j]>max:
                temp_list.append(enter_list[j])
                max = enter_list[j]
        if len(temp_list)>1:
            new_list.append(temp_list)
    return new_list


user_list = get_list(8)
print (user_list)
print (form_equences(user_list))
