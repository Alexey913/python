#Проверяем, является ли одно число квадратом другого

a = int(input())
b = int(input())

if a == b ** 2 or b == a ** 2:
    print("yes")
else:
    print("no")