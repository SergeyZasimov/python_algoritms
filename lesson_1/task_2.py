# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. 
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

n1 = 5; print(n1, '-',  bin(n1))
n2 = 6; print(n2, '-', bin(n2))

res_or = n1 | n2; print('ИЛИ', res_or, '-', bin(res_or))
res_and = n1 & n2; print('И', res_and, '-', bin(res_and))

res_left = n1 << 2; print('Сдвиг влево на 2 бита', res_left, '-', bin(res_left))
res_right = n1 >> 2; print('Сдвиг вправо на 2 бита', res_right, '-', bin(res_right))
