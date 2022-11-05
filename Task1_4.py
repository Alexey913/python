#Выводпервой цифры после запятой
a = float (input())
a = a * 10 % 10
print (int(a))