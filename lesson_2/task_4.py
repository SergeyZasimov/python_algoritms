# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

# import logging

# logging.basicConfig(level=logging.DEBUG, format = '%(message)s')

print('Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...')

n = int(input('Введите количество элементов последовательности '))
my_sum = 0
tmp = 1
for i in range(n):
    my_sum += tmp
    tmp = tmp / -2
#     logging.debug(f'i = {i}, tmp = {tmp}, my_sum = {my_sum}')
print(f'Сумма {n} элементов = {my_sum}')
