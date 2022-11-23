"""1) Считать матрицы (заполненные целыми числами) из файлов
__matrix_1.csv__ и __matrix_2.csv__. Написать функцию, выполняющую
печатающую матрицу - результат перемножения первой на вторую,
задекорировать ее своим временным декоратором (Я вам
запрещаю использовать готовые библиотеки
типа `numpy` или `pandas`).
2) Написать функцию, выполняющую аналогичные
вычисления, но с использованием библиотеки
`multiprocessing`, причем функция должна принимать
аргументом число вспомогательных подпроцессов.
3) Построить график (можно использовать __excel__) функции
__f(n) = T<sub>1</sub> / T<sub>n</sub>__,
где __T<sub>n</sub>__ - время работы функции
перемножения матриц с использованием __n__ подпроцессов."""

import multiprocessing as mp
import time


def read_csv(path):
    csv_to_list = []
    with open(path) as my_data:
        for line in my_data:
            row_list = []
            for val in line.split(';'):
                val = int(val.strip())
                row_list.append(val)
            csv_to_list.append(row_list)
    return csv_to_list


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
        return res
    return wrapper


def empty_mat(cols_b, rows_a):
    return [[0 for row in range(cols_b)] for col in range(rows_a)]


def mult(el_a, el_b):
    return el_a * el_b


@time_decorator
def matmul(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])
    if cols_a != rows_b:
        print('wrong sizes')
    else:
        res = empty_mat(cols_b, rows_a)
        # fill zeros
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    res[i][j] += mult(a[i][k], b[k][j])
        # print in a matrix way
        tmp = list(map(str, res))
        s = '\n'.join([' '.join((l1, l2)) for l1, l2 in zip(tmp[::2], tmp[1::2])])
        print(s)


@time_decorator
def pro_matmul(a, b, n):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])
    if cols_a != rows_b:
        print('wrong sizes')
    else:
        res = empty_mat(cols_b, rows_a)
        # fill zeros
        with mp.Pool(n) as p:
            for i in range(rows_a):
                for j in range(cols_b):
                    for elem_mul in p.starmap(mult, zip(a[i], [row[j] for row in b])):
                        res[i][j] += elem_mul
        # print in a matrix way
        tmp = list(map(str, res))
        s = '\n'.join([' '.join((l1, l2)) for l1, l2 in zip(tmp[::2], tmp[1::2])])
        print(s)


if __name__ == "__main__":
    m1 = read_csv('./matrix_1.csv')
    m2 = read_csv('./matrix_2.csv')
    matmul(m1, m2)
    print('start pro')
    for n in (range(1, mp.cpu_count() + 1)):  # я понимаю, что верхний предел больше, чем нужно, но интересно же
        pro_matmul(m1, m2, n)

    #import matplotlib.pyplot as plt
    #plt.figure(figsize=(10, 7))
    #plt.plot([1, 2, 3, 4], [71.01935291290283, 12.017442226409912, 17.79146695137024, 14.336626052856445])
    #plt.xlabel('processes')
    #plt.ylabel('time, s')
    #plt.show()



