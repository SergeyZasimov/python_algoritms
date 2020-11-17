# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
# При этом каждое число представляется как коллекция, элементы которой — цифры числа. 
# Например, пользователь ввёл A2 и C4F. 
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
from functools import reduce

def add(num1, num2):
    
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    num2.extendleft(['0' for _ in range(len(num1) - len(num2))])

    res = deque([])
    remain = 0
    for i in range(-1, -(len(num1) + 1), -1):
        sum_ = (hex_.index(num1[i]) + hex_.index(num2[i])) - len(hex_) + remain
        if sum_ > 0:
            remain = 1
        else: remain = 0
        res.appendleft(hex_[sum_])
    if remain == 1:
        res.appendleft(hex_[remain])
    return res

def mul(num1, num2):
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    adds = deque([])
    for j in range(-1, -(len(num2) + 1), -1):
        remain = 0
        temps = deque([])
        for i in range(-1, -(len(num1) + 1), -1):
            tmp = hex_.index(num1[i]) * hex_.index(num2[j]) + remain
            remain = tmp // 16
            temps.appendleft(hex_[tmp % 16])
        temps.appendleft(hex_[remain])
        temps.extend(['0' for _ in range(-j - 1)])
        adds.append(temps)

    res = reduce(add, adds)
    return  res

hex_ = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# num1 = deque(['A', '2'])
# num2 = deque(['C', '4', 'F'])

while True:
    sign = input('Введите знак операции [+, *, 0-выход] ')
    if sign == '0': break

    num1 = deque(list(input('Введите первое число ').upper()))
    num2 = deque(list(input('Введите второе число ').upper()))


    signs = {
        '+': [add, "Сумма %s"],
        '*': [mul, "Произведение %s"],
    }

    result = signs[sign][0](num1, num2)
    print(signs[sign][1] %''.join(result))
