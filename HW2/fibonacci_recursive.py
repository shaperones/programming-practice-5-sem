number = int(input())  # нумерация последовательности с нуля!


def fibonacci_recursive(number):
    n = 1
    if number > 1:
        n = fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)
    return n


print(fibonacci_recursive(number))
