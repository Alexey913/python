# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

from decimal import *

def print_num_accuracy(enter_number, enter_accuracy):
    print_num = Decimal(enter_number).quantize(Decimal(enter_accuracy))
    return print_num


number = input('Введите число: \n')
accuracy = input('Введите необходимую точность в формате "0.0001": \n')
print(print_num_accuracy(number,accuracy))