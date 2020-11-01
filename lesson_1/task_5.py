# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, 
# и сколько между ними находится букв.

import string

alphabet = string.ascii_lowercase

char1 = input("Введите первый символ английского алфавита в нижнем регистре ")
char2 = input("Введите второго символа английского алфавита в нижнем регистре ")

ind1 = alphabet.index(char1) + 1
ind2 = alphabet.index(char2) + 1

count = ind2 - ind1 - 1

print(f'{char1} = {ind1}, {char2} = {ind2}, количество букв между ними {count}')
