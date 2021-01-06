# 1. Подсчитать, сколько было выделено памяти под переменные
#    в ранее разработанных программах в рамках первых трех уроков. 
#    Проанализировать результат и определить программы с наиболее эффективным 
#    использованием памяти.


# 4. Определить, какое число в массиве встречается чаще всего.

import sys
import random

MIN_ITEM = 1
MAX_ITEM = 10
SIZE = 20

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)

def func_1(array):
    set_array = set(array)
    frequency = 0

    for el in set_array:
        count = 0
        for i in range(len(array)):
            if array[i] == el:
                count += 1
        if count > frequency:
            frequency = count
            num = el
            
    return locals()

def func_2(array):
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]

    return locals()

def func_3(array):
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    return locals()

functions = (func_1, func_2, func_3)

for func in functions:
    vars_ = func(array)
    print(func.__name__)
    # print(f"{vars_['num']=}, {vars_['frequency']=}")
    total = 0
    for key in vars_:
        print(f'{key:<10} => {type(vars_[key])} => {sys.getsizeof(vars_[key])}')
        total += sys.getsizeof(vars_[key])
    print(f'total => {total}')
    print('\n')

# func_1
# array      => <class 'list'> => 256
# set_array  => <class 'set'> => 728
# max_count  => <class 'int'> => 28
# el         => <class 'int'> => 28
# count      => <class 'int'> => 28
# i          => <class 'int'> => 28
# num        => <class 'int'> => 28
# total => 1124

#  func_2
# array      => <class 'list'> => 256
# num        => <class 'int'> => 28
# frequency  => <class 'int'> => 28
# i          => <class 'int'> => 28
# spam       => <class 'int'> => 28
# j          => <class 'int'> => 28
# total => 396

#  func_3
# array      => <class 'list'> => 256
# counter    => <class 'dict'> => 360
# frequency  => <class 'int'> => 28
# num        => <class 'int'> => 28
# item       => <class 'int'> => 28
# total => 700

# Python 3.8.5 64-bit

# Наименьшее количество памяти занимают переменные второго варианта решения.
# Первый и третий варианты занимают больше памяти из-за использования множества(set)
# и словаря(dict).