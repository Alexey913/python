#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#- 6 -> да
#- 7 -> да
#- 1 -> нет


print('Введите номер дня недели, и я определю, является ли он выходным')
day = int(input('Введите номер дня недели: '))
if day<6 and day>0:
    print('Нет, это будний день')
elif day<1 or day>7:
    print('Некорректный ввод, номера дней недели лежат в диапозоное от 1 до 7')
else:
    print('ДА, это выходной!')