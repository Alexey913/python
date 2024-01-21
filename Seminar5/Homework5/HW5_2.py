# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

from itertools import groupby, starmap
import os.path

def input_text_file (file_with_text):
    list_string = []
    if os.path.exists(file_with_text):
        with open(file_with_text, "r", encoding="utf-8") as text_for_code:
            for line in text_for_code:
                list_string.append(line)
        for i in range (len(list_string)):
            if '\n' in list_string[i]:
                list_string[i] = list_string[i][:-1]
        text_for_code.close()
        return list_string
    else:
        print('Файл не найден!')
        exit()

def code_text (list_string, code_text_file):
    for i in range (len(list_string)):
        code_string = ''
        for k, g in groupby(list_string[i]):
            code_string += str(len(list(g))) + k
        with open(code_text_file, "a", encoding="utf-8") as text_code:
            text_code.write(f"{code_string}\n")
        text_code.close()
        
def decode_text (list_string, decode_text_file):          
    with open(decode_text_file, "a", encoding="utf-8") as text_decode:
        num=''
        for i in list_string:
            decode_string = []
            for j in i.strip():
                if j.isdigit():
                    num+=j
                else:
                    decode_string.append([int(num),j])
                    num=''
            print(f'{"".join(starmap(lambda x, y: x * y, decode_string))}')
            text_decode.write(f'{"".join(starmap(lambda x, y: x * y, decode_string))}\n')
        
def run_code ():
    name_file = input('Введите имя файла с текстом:\n')
    list_for_code = input_text_file(name_file)
    code_name_file = input ('Введите название файла для загрузки результата кодирования:\n')
    code_text(list_for_code, code_name_file)
    decode_name_file = input ('Введите название файла для загрузки результата декодирования:\n')
    decode_text(input_text_file(code_name_file), decode_name_file)
        
run_code()