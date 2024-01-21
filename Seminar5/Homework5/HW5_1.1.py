# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

import random

def enter_word (number):
    word_list = []
    for i in range(number):
        temp = ''.join(random.sample("абв", k=3))
        word_list.append(temp)
    return(word_list)
    
def delete_elements(enter_list):
    while 'абв' in enter_list:
        enter_list.remove('абв')    
    final_text = ' '.join(enter_list)
    return final_text
    
def input_print (user_quantity):
    if user_quantity>0:
        word_set = (enter_word(quantity))
        print(f'Набор случайных слов:')
        print(*word_set)
        print(f'Удаляем слово "абв" из текста:\n{delete_elements(word_set)}')
    else:
        print('Неверный ввод')

    
quantity = int(input('Введите количество слов текста:\n'))
input_print(quantity)