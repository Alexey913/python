#Создать список длин n, значения формируются по формуле 3k+1, где k принимает значения от 1 до n включительно.

n = int(input('Введите n: '))
numbers = []
for k in range(1,n+1):
    numbers.append(3*k+1)
print (numbers)