
# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.

# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match!

def completion_sum_poli(first_part:list, second_part:list):
    with open("Seminar4\Homework4\poli.txt", "a", encoding="utf-8") as data_3:
        for i, temp in enumerate(first_part):
            if second_part[i][0] == '-':
                data_3.write(f"{temp[:-5]} - {second_part[i][1:-1]}\n")
            else:
                data_3.write(f"{temp[:-5]} + {second_part[i]}\n")

def sum_poli(file_1: str, file_2: str):
    with open(file_1, "r", encoding="utf-8") as data_1, open(file_2, "r", encoding="utf-8") as data_2:
        first_part = data_1.readlines()
        second_part = data_2.readlines()
        if len(first_part) == len(second_part):
            completion_sum_poli(first_part, second_part)
        else:
            print(f"The contents of the files do not match! Sum is complete for \
{min(len(first_part), len(second_part))} lines")
            if len(second_part)>len(first_part):
                completion_sum_poli(first_part, second_part)
            else:
                completion_sum_poli(second_part, first_part)

sum_poli("Seminar4\Homework4\poli_1.txt", "Seminar4\Homework4\poli_2.txt")