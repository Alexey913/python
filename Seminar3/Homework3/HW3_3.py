# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000


def dec_to_binary(number):
    binary_number=[]
    while number>0: 
        binary_number.insert(0, number%2)
        number = int(number/2)
    for i in range(len(binary_number)):
        print (binary_number[i], end='')

user_number = int (input('Введите число, и я переведу его в двоичную систему счисления:\n'))
print ('Чмсло', user_number, 'в двоичной систее счисления равно',end=': ')
dec_to_binary (user_number)