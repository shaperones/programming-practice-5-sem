"""Написать программу калькулятор, которая считывает два комплексных числа и проводит с ними
арифметические операции с обработкой вылезающих исключений: например если в процессе деления возникнет
ZeroDivisionError, программа должна продолжить работу, предложив пользователю выбрать другую операцию."""

import numbers
import numpy as np


class MyError(Exception):
    pass


class Complex:  # стандартная форма: a + bi 'standard', экспоненциальная: r*exp(fi) 'exponential'
    def __init__(self, a=0.0, b=0.0, r=0.0, f=0.0, form='standard'):
        self.a = a
        self.b = b
        self.r = r
        self.f = f
        self.form = form

    def get_form(self):
        return self.form

    def get_ab(self):  # геттер для стандартной формы
        if self.form == 'standard':
            return self.a, self.b
        else:
            return 'wrong form'

    def get_rf(self):  # геттер для экспоненциальной формы
        if self.form == 'exponential':
            return self.r, self.f
        else:
            return 'wrong form'

    def set_form(self, form):  # разрешаю использовать, чтобы задать форму при вводе числа, а не менять ее
        if (self.form == 'standard' and self.a == 0 and self.b == 0) or (
                self.form == 'exponential' and self.r == 0 and self.f == 0):
            self.form = form
        else:
            raise ValueError('incorrect form given or ur number is already in one of the forms, use ~to_form~')

    def set_ab(self, a, b):  # сеттеры для стандартной формы
        if not (isinstance(a, numbers.Number) and isinstance(b, numbers.Number)):
            raise ValueError('a & b should be numbers')
        if self.form == 'standard':
            self.a = a
            self.b = b
        else:
            raise ValueError('wrong form')

    def set_rf(self, r, f):  # сеттеры для экспоненциальной формы
        if not (isinstance(r, numbers.Number) and isinstance(f, numbers.Number)):
            raise ValueError('r & f should be numbers')
        if self.form == 'exponential':
            self.r = r
            self.f = f
        else:
            raise ValueError('wrong form')

    def to_expon_form(self):  # в экспоненциальную форму
        if self.form == 'standard':
            if self.a == 0:
                raise MyError('cannot change form: a = 0')
            else:
                self.f = np.arctan(self.b / self.a)
                self.r = (self.a ** 2 + self.b ** 2) ** 0.5
                self.a = 0
                self.b = 0
                self.form = 'exponential'
        else:
            print('number is already in exponential form')

    def to_standard_form(self):  # из экспоненциальной в стандартную
        if self.form == 'exponential':
            self.a = self.r * np.cos(self.f)
            self.b = self.r * np.sin(self.f)
            self.r = 0
            self.f = 0
            self.form = 'standard'
        else:
            print('number is already in standard form')

    def __add__(self, other):  # сложение
        if isinstance(other, Complex):
            if self.form == 'standard' and other.form == 'standard':
                return Complex(a=(self.a + other.a), b=(self.b + other.b))
            else:
                print('complex numbers should be in the standard form')
        if isinstance(other, numbers.Number):
            if self.form == 'standard':
                return Complex(a=(self.a + other), b=self.b)
            else:
                print('complex numbers should be in the standard form')

    def __radd__(self, other):  # сложение (не добавляю вариант с 2 комплексными, тк он покрывается __add__)
        if isinstance(other, numbers.Number):
            if self.form == 'standard':
                return Complex(a=(self.a + other), b=self.b)
            else:
                print('complex numbers should be in the standard form')

    def __sub__(self, other):  # вычитание
        if isinstance(other, Complex):
            if self.form == 'standard' and other.form == 'standard':
                return Complex(a=(self.a - other.a), b=(self.b - other.b))
            else:
                print('complex numbers should be in the standard form')
        if isinstance(other, numbers.Number):
            if self.form == 'standard':
                return Complex(a=(self.a - other), b=self.b)
            else:
                print('complex numbers should be in the standard form')

    def __rsub__(self, other):  # вычитание number - complex
        if isinstance(other, numbers.Number):
            if self.form == 'standard':
                return Complex(a=(other - self.a), b=(-self.b))
            else:
                print('complex numbers should be in the standard form')

    def __mul__(self, other):  # умножение
        if isinstance(other, Complex):
            if self.form == 'standard' and other.form == 'standard':
                return Complex(a=(self.a * other.a - self.b * other.b), b=(self.a * other.b + self.b * other.a))
            else:
                print('complex numbers should be in the standard form')
        if isinstance(other, numbers.Number):
            if self.form == 'standard':
                return Complex(a=(self.a * other), b=(self.b * other))
            else:
                print('complex numbers should be in the standard form')

    def __rmul__(self, other):  # умножение number * complex
        if isinstance(other, numbers.Number):
            if self.form == 'standard':
                return Complex(a=(self.a * other), b=(self.b * other))
            else:
                print('complex numbers should be in the standard form')

    def __truediv__(self, other):  # деление
        if isinstance(other, Complex):
            if self.form == 'standard' and other.form == 'standard':
                return Complex(a=((self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2)),
                               b=((self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)))
            else:
                print('numbers should be in the standard form')
        if isinstance(other, numbers.Number):
            if self.form == 'standard':
                return Complex(a=(self.a / other), b=(self.b / other))
            else:
                print('complex numbers should be in the standard form')

    def __rtruediv__(self, other):  # деление number / complex
        if isinstance(other, numbers.Number):
            if self.form == 'standard':
                return Complex(a=(self.a * other / (self.a ** 2 + self.b ** 2)),
                               b=(- self.b * other / (self.a ** 2 + self.b ** 2)))
            else:
                print('complex numbers should be in the standard form')

    def __eq__(self, other):  # сравнение
        if isinstance(other, Complex):
            if self.form == 'standard' and other.form == 'standard':
                if self.a == other.a and self.b == other.b:
                    return True
                else:
                    return False
            else:
                print('complex numbers should be in the standard form')
                return False
        if isinstance(other, numbers.Number):
            if self.form == 'standard':
                if self.b == 0 and self.a == other:
                    return True
                else:
                    return False
            else:
                print('complex numbers should be in the standard form')
                return False

    def __abs__(self):
        if self.form == 'standard':
            return (self.a ** 2 + self.b ** 2) ** 0.5
        else:
            print('complex numbers should be in the standard form')

    def __str__(self):
        if self.form == 'standard':
            return str(self.a) + " " + str(self.b)
        if self.form == 'exponential':
            return str(self.r) + " " + str(self.f)

    def __getitem__(self, item):
        if self.form == 'exponential':
            print('complex numbers should be in the standard form')
        else:
            if item == 0:
                return self.a
            if item == 1:
                return self.b
            else:
                return False

    def __setitem__(self, key, value):
        if self.form == 'exponential':
            print('complex numbers should be in the standard form')
        else:
            if key == 0:
                self.a = value
            if key == 1:
                self.b = value
            else:
                return False


class OpError(Exception):
    pass


print('\033[96m'+'Калькулятор работает с комплексными числами в стандартной форме. Справка: '
      'стандартная форма комплексного числа complex = a + bi. \n'
      'Доступные операции: *, /, +, - . '
      'Ввод чисел вида "a1 b1 a2 b2" даст числа (a1 + ib1), (a2 + ib2).\n'
      'Вывод nan означает неопределенный результат. Вы заигрались с inf :)'+'\033[0m')
while True:
    try:
        a1, b1, a2, b2 = [float(x) for x in input('Компоненты чисел через пробел:').split(' ')]
        op = input('Операция (1 символ):')[0]
        if op not in ['*', '/', '+', '-']:
            raise OpError
    except ValueError:
        print('Неверный ввод. См. пример ввода')
    except OpError:
        print('Неверно введена операция. См. доступные операции')
    except EOFError:
        print('Встречен EOF. Завершение работы')
        break
    else:
        x, y = Complex(a1, b1), Complex(a2, b2)
        if op == '+':
            print('({} + {}i) + ({} + {}i) = ({} + {}i)'.format(
                x[0], x[1], y[0], y[1], (x + y)[0], (x + y)[1]))
        if op == '-':
            print('({} + {}i) - ({} + {}i) = ({} + {}i)'.format(
                x[0], x[1], y[0], y[1], (x - y)[0], (x - y)[1]))
        if op == '*':
            print('({} + {}i) * ({} + {}i) = ({} + {}i)'.format(
                x[0], x[1], y[0], y[1], (x * y)[0], (x * y)[1]))
        if op == '/':
            try:
                print('({} + {}i) / ({} + {}i) = ({} + {}i)'.format(
                    x[0], x[1], y[0], y[1], (x / y)[0], (x / y)[1]))
            except ZeroDivisionError:
                print('Деление на ноль')
