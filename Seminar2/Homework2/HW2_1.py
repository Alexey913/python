#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#in -> out
#- 6782 -> 23
#- 0.67 -> 13
#- 198.45 -> 27

user_number = float(input('Введите число:\n'))

quantity_digits = len(str(user_number))-2
temp = (abs(user_number*10**quantity_digits))   # ввожу переменную, чтобы оставить число пользователя для вывода в конце,
                                                # а также для возможности учета отрицательных чисел
sum_digit = 0

while temp>9:                                   # условие не учитывает первую цифру числа
        sum_digit = sum_digit+temp%10
        temp=round(temp//10)
        print(temp, sum_digit)
else:                                           # в зависимости знака числа, принимаем первую цифру либо со знаком "+", либо со знаком "-"
    if user_number>0:
        sum_digit = sum_digit+temp%10
    else:
        sum_digit = sum_digit-temp%10

print ('Сумма цифр числа {} равна: {}'.format (user_number, sum_digit))