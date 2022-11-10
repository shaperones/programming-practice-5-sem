"""4) Написать программу, сравнивающую скорость работы функции вычисления чисел
Фибоначчи, написанной через циклы и через рекурсию, с использованием __@lru_cache(maxsize=None)__
и без"""
import time
from functools import lru_cache


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
        return res
    return wrapper


@lru_cache(maxsize=None)
@time_decorator
def fib_cycle(n):
    fib1 = 1
    fib2 = 1
    if n == 0 or n == 1:
        return 1
    for _ in range(1, n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


@lru_cache(maxsize=None)  # декоратор времени здесь бесполезен, тк рекурсия
def fib_recursion(n):
    if n == 0 or n == 1:
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)


if __name__ == '__main__':
    n = int(input('номер: '))

    start_time_2 = time.time()
    fib_recursion.__wrapped__(n)
    rec_time_2 = time.time() - start_time_2
    print('recursive time without lru: ', rec_time_2)

    start_time = time.time()
    fib_recursion(n)
    rec_time = time.time() - start_time
    print('recursive time with lru: ', rec_time)

    print('cyclic time without lru:', end=' ')
    fib_cycle.__wrapped__(n)

    print('cyclic time with lru:', end=' ')
    fib_cycle(n)


