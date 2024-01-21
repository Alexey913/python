
# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from random import choice

def write_polinomical(degree):
    list_ratio = range(11)
    polinomical = choice(' -')
    with open ("Seminar4\Homework4\polinomical.txt",'a', encoding='UTF-8') as my_file:
        for i in range (degree, 1, -1):
            ratio = choice(list_ratio)
            if ratio:
                polinomical+=f"{ratio}*x^{i} {choice('+-')} "
        polinomical=my_file.write(f"{polinomical}{choice(list_ratio)} = 0\n")

def quntity_realization (count):
    while count<3:
        count = int(input('The number of implementations should not be less than 3. Please repeat enter:\n'))
    else:
        for i in range (count):
            user_number = int(input(f'Enter degree k for {i+1} polinomical:\n'))
            while user_number<2:
                user_number=int(input('Please enter degree k > 1:\n'))
            else:
                with open ("Seminar4\Homework4\polinomical.txt",'a', encoding='UTF-8') as my_file:
                    my_file.write(f"\n Многочлен № {i+1}\n")
                write_polinomical((user_number))
                

user_count = int (input('How many times do you want to implement the algorithm? Enter number:\n'))
quntity_realization (user_count)