# Написать функцию генератор, создающую числа Фибоначчи до N-го.
def fib_gen(n):
    res = 1
    prev = 0
    for j in range(n):
        yield res
        n_prev = res
        res += prev
        prev = n_prev


for i in fib_gen(8):
    print(i)
