# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib

def uniq_substring(data):
    length = len(data)
    uniq_hash = []
    exceptions_hash = (
        hashlib.sha256(''.encode('utf-8')).hexdigest(),
        hashlib.sha256(data.encode('utf-8')).hexdigest(),
    )

    for i in range(length):
        for j in range(length + 1):
            substring = data[i:j]
            hash_substring = hashlib.sha256(substring.encode('utf-8')).hexdigest()
            if (hash_substring in uniq_hash) or (hash_substring in exceptions_hash):
                continue
            else:
                uniq_hash.append(hash_substring)

    return len(uniq_hash)

def test_uniq_substring():
    assert uniq_substring('papa') == 6, 'papa'
    assert uniq_substring('sova') == 9, 'sova'
    assert uniq_substring('abcd') == 9, 'abcd'
    assert uniq_substring('a c') == 5, 'a c'
    print('Test OK')

test_uniq_substring()