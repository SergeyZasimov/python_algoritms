# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
#  Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

m = 5
SIZE = 2 * m + 1

MIN_ITEM = 0
MAX_ITEM = 11

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

def median(arr, ind):

    if len(arr) == 1:
        return arr[0]

    pivot = arr[0]
    lt = []
    gt = []
    eq = []

    for el in arr:
        if el > pivot:
            gt.append(el)
        elif el < pivot:
            lt.append(el)
        else:
            eq.append(el)
    
    # print(lt, gt, eq, ind)

    if len(lt) > ind:
        return median(lt, ind)
    elif (len(lt) + len(eq)) > ind:
        return eq[0]
    else:
        return median(gt, ind - len(lt) - len(eq))

print(median(array, len(array) // 2))

# array.sort()
# print(array)
# print(array[len(array)//2])