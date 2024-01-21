#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#in -> out
#- 6782 -> 23
#- 0.67 -> 13
#- 198.45 -> 27

user_number = float(input('Введите число:\n'))

integer = abs(int(user_number))
rounding = len(str(abs(user_number)))-(len(str(integer)))
fraction = round((abs(user_number)-integer), rounding)

sum_digit = 0
count = 0

while integer>9:
    sum_digit = sum_digit+integer%10
    integer=integer//10
else:
    if user_number>0:
        sum_digit = sum_digit+integer%10
    else:
        sum_digit = sum_digit-integer%10

while fraction>0:
    sum_digit = sum_digit+int(fraction*10)
    count+=1
    fraction = round (fraction*10 - int(fraction*10), rounding-count)

print ('Сумма цифр числа {} равна: {}'.format (user_number, sum_digit))