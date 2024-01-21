# Напишите программу, которая принимает на вход 5 чисел и находит маскимальное из них

max = 0
for i in range (5):
    number = int(input('Введите число  '))
    if number > max:
        max = number
print("Максимальное число равно ", + max)