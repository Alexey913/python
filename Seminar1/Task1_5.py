# Число кратно 5 и 10 или 15, но не кратно 30
number = int(input())
if (number%5 == 0 and number%10 == 0 or number%15 == 0) and (number%30 != 0):
    print ('yes')
else:
    print ('no')