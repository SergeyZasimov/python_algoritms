# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

ROW_SIZE = 3
COLUMN_SIZE = 3
matrix = []

MIN_ITEM = 1
MAX_ITEM = 20

for i in range(ROW_SIZE):
    line = [random.randint(MIN_ITEM, MAX_ITEM) for j in range(COLUMN_SIZE)]
    matrix.append(line)
    
for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print('\n')

mins = []
for j in range(COLUMN_SIZE):
    min_el = matrix[0][j]
    for i in range(ROW_SIZE):
        if matrix[i][j] < min_el:
            min_el = matrix[i][j]
#     print(f'Минимальный элемент {j + 1}-го столбца {min_el}')
    mins.append(min_el)

res = mins[0]
for num in mins:
    if num > res:
        res = num
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы {res}')
