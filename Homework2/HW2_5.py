# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randint

print('Введите размер N списка. Я составлю список из элементов от 1 до N и осуществлю их перемешивание')
N = int(input())
num_list = []
for i in range(1, N+1):
    num_list.append(i)

print('У нас есть такой список: \n', num_list)

for i in range(N):
    rand_index = randint(0, N-1)
    temp = num_list[i]
    num_list[i] = num_list[rand_index]
    num_list[rand_index] = temp

print('Новый список:\n', num_list)
