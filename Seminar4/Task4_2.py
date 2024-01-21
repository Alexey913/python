#  Найдите корни квадратного уравнения Ах2+Вх+С=0, с помощью модуля.
# Запросите значения А, В, С 3 раза.
# Уравнениия и корни записать в файл

from math import sqrt

def resh (a, b, c):
    D = b**2 - 4*a*c
    with open ("result.txt",'a', encoding='UTF-8') as my_file:
        my_file.write(f"{a}x^2 + {b}x + {c} = 0"+"\n")
        if D>0 and a:
            my_file.write('x1 ='+str((-b+sqrt(D))/(2*a))+"\n")
            my_file.write('x2 ='+str((-b-sqrt(D))/(2*a))+"\n")
        elif D == 0 and b:
            my_file.write('x =', str((-b)/(2*a))+"\n")
        else:
            my_file.write('Корней нет'+"\n")

for i in range(3):
    resh(int(input()),int(input()), int(input()))