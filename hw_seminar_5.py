# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# with open('файл для задач.txt', 'r', encoding='utf-8') as file:    
#     text = file.read().split()
#     print(text)
   
# new_text = list(filter(lambda word: 'а' not in word and 'б' not in word and 'в' not in word, text))
# print(new_text)      

# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.




with open('file 2.txt', 'r', encoding='utf-8') as file:
    my_text = file.read()
    print(my_text)

def code_rle(rle):
    code = ''
    prev_char = ''
    count = 1
    for char in rle:
        if char != prev_char:
            if prev_char:
                code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return code
           
code = code_rle(my_text)
print(code)

with open('файл для задач.txt', 'r', encoding='utf-8') as file:
    my_text2 = file.read()

def decoding(rle):
    count = ''
    decode = ''
    for char in rle:
        if char.isdigit():
            count += char 
        else:
            decode += char * int(count)
            count = ''
    return decode

decode = decoding(my_text2)
print(decode)