# 1. В диапазоне натуральных чисел от 2 до 99 определить, 
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM = 99

LEFT = 2
RIGHT = 9

res = [0] * (RIGHT + 1 - LEFT)

for i in range(MIN_ITEM, MAX_ITEM + 1):
    for j in range(LEFT, RIGHT + 1):
        if i % j == 0:
            res[j - LEFT] += 1

for el in res:
    print(f'{res.index(el) + LEFT} = {el}')
