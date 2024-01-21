# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

def simple_dividers(user_number):
    list_simple = []
    for i in range (2,user_number):
        while user_number%i==0:
            list_simple.append(i)
            user_number = user_number/i
    return (list_simple)

num = int(input('Введите число: \n'))

print_list = simple_dividers(int(num))
if print_list:
    print (print_list)
else:
    print ('Число {} является простым'.format(num))