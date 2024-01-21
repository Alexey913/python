# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

def fill_fibonacci(N):
    fibonacci = [1,0,1]
    for i in range(3,N*2,2):
        fib_n = fibonacci[i-1]+fibonacci[i-2]
        fibonacci.append (fib_n)
        fibonacci.insert(0, ((-1)**int((i/2)+2)*fib_n))
    return fibonacci

N = int(input('Введите количество элементов последовательности:\n'))
my_fibonacci = fill_fibonacci(N)
print ('Последовательность Фибоначчи для {} элементов:\n{}'.format(N,my_fibonacci))