# Задайте два числа. Напишите программу, которая должна находить НОК двух чисел.

from math import gcd

num_1 = int(input())
num_2 = int(input())
print ((num_1*num_2)//gcd(num_1, num_2))