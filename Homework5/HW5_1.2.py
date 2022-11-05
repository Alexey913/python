import random

def enter_word (number):
    word_list = []
    for i in range(number):
        temp = ''.join(random.sample("абв", k=3))
        word_list.append(temp)
    return(' '.join(word_list))
    
def delete_elements(enter_text):
    return enter_text.replace('абв ','',)

def input_print (user_quantity):
    if user_quantity>0:
        word_set = (enter_word(quantity))
        print(f'Набор случайных слов:\n{word_set}')
        print(f'Удаляем слово "абв" из текста:\n{delete_elements(word_set)}')
    else:
        print('Неверный ввод')

quantity = int(input('Введите количество слов текста:\n'))
input_print(quantity)