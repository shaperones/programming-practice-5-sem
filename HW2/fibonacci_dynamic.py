number = int(input())  # нумерация последовательности с нуля!
memory = [1, 1] + [0] * (number - 1)  # чтобы хранить числа


def fibonacci_dynamic(n):
    if memory[n] != 0:  # если уже вычисляли
        return memory[n]
    else:
        memory[n] = fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)  # если еще нет
    return memory[n]


print(fibonacci_dynamic(number))
