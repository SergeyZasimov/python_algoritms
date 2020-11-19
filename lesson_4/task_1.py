# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, 
#   для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

import timeit, cProfile

'''
1. В диапазоне натуральных чисел от 2 до 99 определить, 
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

def func1(N):
    MIN_ITEM = 2
    MAX_ITEM = N

    LEFT = 2
    RIGHT = 9

    res = [0] * (RIGHT + 1 - LEFT)

    for i in range(MIN_ITEM, MAX_ITEM + 1):
        for j in range(LEFT, RIGHT + 1):
            if i % j == 0:
                res[j - LEFT] += 1

    return res

print(timeit.timeit('func1(100)', number=100, globals=globals()))		# 0.009399220001796493
print(timeit.timeit('func1(1000)', number=100, globals=globals()))		# 0.07789418700122042
print(timeit.timeit('func1(10000)', number=100, globals=globals()))		# 0.8345993000002636
print(timeit.timeit('func1(100000)', number=100, globals=globals()))	# 9.30621157600035
print(timeit.timeit('func1(1000000)', number=100, globals=globals()))	# 95.88406337800188
cProfile.run('func1(1000000)')

#	4 function calls in 0.914 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.914    0.914 <string>:1(<module>)
#        1    0.914    0.914    0.914    0.914 task_1.py:15(func1)
#        1    0.000    0.000    0.914    0.914 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('***')
def func2(N):
    MIN_ITEM = 2
    MAX_ITEM = N

    LEFT = 2
    RIGHT = 9

    res = []

    for j in range(LEFT, RIGHT + 1):
        count = 0
        for i in range(MIN_ITEM, MAX_ITEM + 1):
            if i % j == 0:
                count += 1
        res.append(count)

    return res


print(timeit.timeit('func2(100)', number=100, globals=globals()))		# 0.006028223000612343
print(timeit.timeit('func2(1000)', number=100, globals=globals()))		# 0.05718641199928243
print(timeit.timeit('func2(10000)', number=100, globals=globals()))		# 0.614911992000998
print(timeit.timeit('func2(100000)', number=100, globals=globals()))	# 6.222983768999256
print(timeit.timeit('func2(1000000)', number=100, globals=globals()))	# 61.51436230699983
cProfile.run('func2(1000000)')

#	12 function calls in 0.594 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.594    0.594 <string>:1(<module>)
#        1    0.594    0.594    0.594    0.594 task_1.py:39(func2)
#        1    0.000    0.000    0.594    0.594 {built-in method builtins.exec}
#        8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('***')
def func3(N):
    
    MIN_ITEM = 2
    MAX_ITEM = N

    LEFT = 2
    RIGHT = 9
    
    res = {}
    
    for i in range(MIN_ITEM, MAX_ITEM + 1):
        for j in range(LEFT, RIGHT + 1):
            if i % j == 0:
                res.setdefault(j, 0)
                res[j] += 1
    return list(res.values())

print(timeit.timeit('func3(100)', number=100, globals=globals()))		# 0.009491914002865087
print(timeit.timeit('func3(1000)', number=100, globals=globals()))		# 0.09398012100064079
print(timeit.timeit('func3(10000)', number=100, globals=globals()))		# 0.9627868919997127
print(timeit.timeit('func3(100000)', number=100, globals=globals()))	# 10.175979251998797
print(timeit.timeit('func3(1000000)', number=100, globals=globals()))	# 105.4606879109997
cProfile.run('func3(1000000)')

#         1828972 function calls in 1.444 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.444    1.444 <string>:1(<module>)
#        1    1.242    1.242    1.444    1.444 task_1.py:65(func3)
#        1    0.000    0.000    1.444    1.444 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  1828967    0.201    0.000    0.201    0.000 {method 'setdefault' of 'dict' objects}
#        1    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}


#def test_func(func):
#    N = 99
#    res = [49, 33, 24, 19, 16, 14, 12, 11]
#    assert res == func(N)
#    print('test - OK')
#
#test_func(func1)
#test_func(func2)
#test_func(func3)

# Вывод: все три функции имеют сложность O(n^2) из-за использования двух циклов. Второй алгоритм выполняется быстрее всего.
# Работу третьей функции замедляет метод setdefault.
