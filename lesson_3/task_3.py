# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 20

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# array = random.sample(range(MIN_ITEM, MAX_ITEM), SIZE)
print(array)

START_IND = min_ind = max_ind = 0
max_el = min_el = array[START_IND]
for i in range(len(array)):
    if array[i] < min_el:
        min_el = array[i]
        min_ind = i
    
    if array[i] > max_el:
        max_el = array[i]
        max_ind = i
        

array[min_ind], array[max_ind] = array[max_ind], array[min_ind]

print(array)
# print(f'{min_ind=} {max_ind=} {min_el=} {max_el=}')
