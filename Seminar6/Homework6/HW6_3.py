# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'],
# 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def create_dictionary (name_list):

    dictionary_name = {}
    for j in sorted(name_list):
        if j[0] in dictionary_name:
            dictionary_name[j[0]] += [j]
        else:    
            dictionary_name[j[0]] = [j]
    return dictionary_name

# -------------2 вариант----------------
# import itertools


# def create_dictionary (*namelist):
#     if "" not in namelist:
#         return {k: list(names) for k, names in itertools.groupby(sorted(namelist), key = lambda i: i[0]) if k}
#     return "Error"
# 
# --------------------------------------- 

# name_list = input('Введите список имен через пробел:\n').split()
name_list = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка", "Финтиплюх"]
print(create_dictionary(name_list))
