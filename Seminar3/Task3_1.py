#Задайте список, состоящий из произвольных чисел, количество задает пользователь.
#Напишите программу, которая определяет, присутствует ли в задданном списке число,
# полученное от пользователя

from random import sample

def find_number(number, quantity=0):
    quantity = quantity if quantity > 0 else -quantity
    num_list = sample(range(1, quantity*2), quantity)
    print (num_list)
    if number in num_list:
        return True
    return False

print(find_number(2, 5))