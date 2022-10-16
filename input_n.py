x = 0
y = 0

def init(a, b):
    global x 
    global y 
    x = a
    y = b

def int_num():
    a = int(input('Введите число 1: '))
    b = int(input('Введите число 2: '))
    init (a, b)
     
def float_num():
    a = float(input('Введите число 1: '))
    b = float(input('Введите число 2: '))
    init (a, b)

def complex_num ():
    d_1 = float(input('Введите действительную часть числа 1: '))
    m_1 = float(input('Введите мнимую часть числа 1: '))
    a = complex(d_1, m_1)
    d_2 = float(input('Введите действительную часть числа 2: '))
    m_2 = float(input('Введите мнимую часть числа 2: '))
    b = complex(d_2, m_2)
    init (a, b)