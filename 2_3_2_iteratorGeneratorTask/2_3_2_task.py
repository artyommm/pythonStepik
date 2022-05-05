import itertools


def primes():
    i = 1
    k = 0
    while True:
        i += 1
        # пробегаем все числа от 2 до текущего
        for j in range(2, i):
            # ищем количество делителей
            if i % j == 0:
                k = k + 1
        if k == 0:
            yield i
        else:
            k = 0

print(list(itertools.takewhile(lambda x: x <= 31, primes())))