x = 0
y = 0

def init(a, b):
    global x 
    global y 
    x = a
    y = b

def Int():
    return int(input('value = '))
     
def Float():
    return float(input('value = '))

def Complex(x,y):
    x = int(input('value = '))
    y = int(input('value = '))
    return(complex(x,y))
print(Complex(x,y))