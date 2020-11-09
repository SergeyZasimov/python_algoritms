# 6. В одномерном массиве найти сумму элементов, 
# находящихся между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 20

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] 
# сумма между первым вхождением min max (?)
# если один из этих элементов входит внутрь вычисляемого диапазона он не исключается (?)
# исключаются только границы диапазона


# array = random.sample(range(MIN_ITEM, MAX_ITEM), SIZE) # нет повторяющихся элементов
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
        
my_sum = 0
if min_ind < max_ind:
    for ind in range(min_ind + 1, max_ind):
        my_sum += array[ind]
else:
    for ind in range(max_ind + 1, min_ind):
        my_sum += array[ind]

        
# print(f'{min_ind=} {max_ind=} {min_el=} {max_el=}')
print(f'Сумма между минимальным элементом и максимальным элементом {my_sum}')
