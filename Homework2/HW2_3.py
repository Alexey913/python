# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13


n = int(input('Введите число:\n'))
new_list = []
sum_new_list = 0
q_round = int(input('Введите количество разрядов после запятой для результатов\n'))
for i in range(n):
    temp=(1+1/(i+1))**(i+1)
    new_list.append(round(temp, q_round))
    sum_new_list+=temp
print("Полученный список: {} \n Сумма элементов равна: {}".format(new_list, round(sum_new_list, q_round)))