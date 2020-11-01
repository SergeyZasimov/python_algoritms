# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

alphabet = string.ascii_lowercase
num = int(input("Введите номер символа английского алфавита "))
res = alphabet[num - 1] 
print(res)
