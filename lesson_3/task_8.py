# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. 
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. 
# В конце следует вывести полученную матрицу.

ROW_SIZE = 4
COLUMN_SIZE = 5
matrix = []

# import random

# MIN_ITEM = 1
# MAX_ITEM = 20

# for i in range(ROW_SIZE):
#     sum_line = 0
#     line = [random.randint(MIN_ITEM, MAX_ITEM) for j in range(COLUMN_SIZE - 1)]
#     for num in line:
#         sum_line += num
#     line.append(sum_line)
#     matrix.append(line)
    
for i in range(ROW_SIZE):
    line = []
    sum_line = 0
    for j in range(COLUMN_SIZE - 1):
        item = int(input(f'Введите {j + 1}-ый элемент {i + 1}-ой строки '))
        sum_line += item
        line.append(item)
    line.append(sum_line)
    matrix.append(line)
    
for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print('\n')
