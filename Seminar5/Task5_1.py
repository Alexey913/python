# В файле находятся N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i]-1=A[i-1].
# Найдите это число

import random

def form_list ():
    path='file5_1.txt' # уйти от абсолютного адреса
    data = open(path,'r')
    new_list=list(map(int,(data.readline().split())))
    data.close()
    print (new_list)
    new_list.remove(random.choice(new_list))
    print (new_list)
    return new_list

def checklist(enter_list):
    if enter_list[0]!=1:
        return 0
    for i in range (1, len(enter_list)):
        if(enter_list[i]-1)!=enter_list[i-1]:
            return enter_list[i]-1
            break

print(checklist(form_list()))