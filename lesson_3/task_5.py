# 5. В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве. 
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». 
# Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

negative_array = [num for num in array if num < 0]

START_IND = 0
max_el = negative_array[START_IND]
for el in negative_array:
    if el > max_el:
        max_el = el

print(f'Максимальный отрицательный элемент {max_el}')
