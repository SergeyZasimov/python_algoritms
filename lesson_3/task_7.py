# 7. В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 20

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

LAPS = 2

for i in range(LAPS):
    START_IND = min_ind = 0
    min_el = array[START_IND]
    for j in range(len(array)):
        if array[j] < min_el:
            min_el = array[j]
            min_ind = j
    res = array.pop(min_ind)
    print(f'Минимальный элемент {i + 1} = {res}')
