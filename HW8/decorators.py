""" 1) Написать декоратор, разворачивающий порядок переданных в функцию аргументов
    независимо от их количества (например декорированная __foo(4, 5)__ должна быть
    эквивалентна вызову недекорированной __foo(5, 4)__)
    2) Написать декоратор, печатающий аргументы, переданные функции, после её выполнения.
    3) Написать декоратор, пробующий запустить переданную функцию, и возвращающий
    строку "error" в случае возникновения исключения."""


from functools import wraps


def reverse_args(func):
    @wraps(func)  # чтобы обращать декорирование __wrapped__
    def wrapper(*args):
        args = args[::-1]
        res = func(*args)
        return res
    return wrapper


def print_args(func):
    @wraps(func)  # чтобы обращать декорирование __wrapped__
    def wrapper(*args):
        func(*args)
        print('given args: ', *args)
    return wrapper


def catch_exceptions(func):
    @wraps(func)  # чтобы обращать декорирование __wrapped__
    def wrapper(*args):
        try:
            func(*args)
        except Exception:
            print('error')
    return wrapper


if __name__ == '__main__':
    @reverse_args
    def foo(*args):
        print(*args)

    foo(1, 2, 3, 5)
    foo.__wrapped__(1, 2, 3, 5)

    @print_args
    @catch_exceptions
    def foo1(*args):
        print(sum(args))

    foo1(1, 2, 3, 5)
    foo1.__wrapped__(1, 2, 3, 5)
    foo1('nya', 1, 'a')
