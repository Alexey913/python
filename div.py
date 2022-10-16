# Глобальных имен переменных не объявлял, т.к. локальные импортируются вместе с модулем.

# float/true division
def float_div(num1, num2):
    return num1 / num2


# floor division
def floor_div(num1, num2):
    return num1 // num2


# modulo division
def mod_div(num1: int, num2: int):
    return num1 % num2


# Как вариант с использованием встроенных функций
# import operator as oper
#
#
# def float_div(num1, num2):
#     return oper.truediv(num1, num2)
#
#
# def floor_div(num1, num2):
#     return oper.floordiv(num1, num2)
#
#
# def mod_div(num1: int, num2: int):
#     return oper.mod(num1, num2)


