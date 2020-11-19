# 2. Во втором массиве сохранить индексы четных элементов первого массива. 
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, 
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), 
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 20

first_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(first_array)

second_array = []
for i in range(len(first_array)):
    if first_array[i] % 2 == 0:
        second_array.append(i)
print(second_array)

# second_array_2 = [first_array.index(el) for el in first_array if el % 2 == 0]
# print(second_array_2)
