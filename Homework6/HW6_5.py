# 5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# in
# 10 True

# out

# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый', 'город позавчера утопичный']

# in
# 10 False

# ['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый',
# 'город вчера утопичный', 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый',
# 'огонь позавчера яркий', 'огонь где-то утопичный', 'автомобиль где-то мягкий']

from inspect import Parameter
import random
from itertools import zip_longest

def form_jokes (quan, param = False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    min_len = min (len(nouns), len(adverbs), len(adjectives))
    list_joke = []
    random.shuffle(nouns), random.shuffle(adverbs), random.shuffle(adjectives)
    if param:
        if quan > min_len:
            quan = min_len
        list_joke = [item for i, item in enumerate((zip_longest (nouns, adverbs, adjectives))) if i < quan]
    else:
        for i in range(quan):
            temp = random.choice(nouns), random.choice(adverbs), random.choice(adjectives)
            list_joke.append (temp)

    new_list = []
    for i in list_joke:
        new_list.append(' '.join(i))

    return new_list

qunt_e = int(input ('Введите количество необходимых шуток:\n'))
param_u = input ('Введите параметр уникальности значений True/False:\n')

print(form_jokes(qunt_e, param_u))