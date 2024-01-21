# Задайте список, состоящий из произвольных слов, количество задает пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщает, что его нет.

from random import choices


def fill_elements(quantity, elements):
    list_str = []
    for i in range(quantity):
        str = choices(elements, k=3)
        list_str.append("".join(str))
    return list_str


list_for_find_str = fill_elements(15, 'abc')
print(list_for_find_str)


def find_str(element, list_elements: list):
    if list_elements.count(element) > 1:
        index_element = list_elements.index(element)
        print(list_elements.index(element, index_element+1))
    else:
        print(-1)


find_str(input(), list_for_find_str)