# 4. Определить, какое число в массиве встречается чаще всего.

import random

MIN_ITEM = 1
MAX_ITEM = 10
SIZE = 20

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

set_array = set(array)
max_count = 0

for el in set_array:
    count = 0
    for i in range(len(array)):
        if array[i] == el:
            count += 1
    if count > max_count:
        max_count = count
        num = el

print(f'Число {num} встречается {max_count} раза')
