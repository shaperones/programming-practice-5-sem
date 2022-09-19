#1) Создайте класс для хранения комплексных чисел с инициализатором.
#2) Обеспечьте его необходимыми геттерами и сеттерами.
#3) Реализуйте методы, позволяющие переводить комплексное число в экспоненциальную форму и обратно.
#4) Добавьте функции, позволяющие складывать, вычитать, умножать и делить два комплексных числа,
#   результатом работы которых будет новое комплексное число.
import numpy as np


class Complex:  # стандартная форма: a + bi 'standard', экспоненциальная: r*exp(fi) 'exponential'
    def __init__(self, a=0, b=0, r=0, f=0, form='standard'):
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
            return 'lol wrong form'

    def get_rf(self):  # геттер для экспоненциальной формы
        if self.form == 'exponential':
            return self.r, self.f
        else:
            return 'lol wrong form'

    def set_form(self, form):  # разрешаю использовать, чтобы задать форму при вводе числа, а не менять ее
        if (self.form == 'standard' and self.a == 0 and self.b == 0) or (
                self.form == 'exponential' and self.r == 0 and self.f == 0):
            self.form = form
        else:
            print('ur number is already in one of the forms, use ~to_form~')

    def set_ab(self, a, b):  # сеттеры для стандартной формы
        if self.form == 'standard':
            self.a = a
            self.b = b
        else:
            print('lol wrong form')

    def set_rf(self, r, f):  # сеттеры для экспоненциальной формы
        if self.form == 'exponential':
            self.r = r
            self.f = f
        else:
            print('lol wrong form')

    def to_expon_form(self):  # в экспоненциальную форму
        if self.form == 'standard':
            self.r = (self.a ** 2 + self.b ** 2) ** 0.5
            self.f = np.arctan(self.b / self.a)
            self.a = 0
            self.b = 0
            self.form = 'exponential'

    def to_standard_form(self):  # из экспоненциальной в стандартную
        if self.form == 'exponential':
            self.a = self.r * np.cos(self.f)
            self.b = self.r * np.sin(self.f)
            self.r = 0
            self.f = 0
            self.form = 'standard'

    def add(self, other):  # сложение
        if self.form == 'standard' and other.form == 'standard':
            return Complex(a=(self.a + other.a), b=(self.b + other.b))
        else:
            print('numbers should be in the standard form')

    def subtract(self, other):  # вычитание
        if self.form == 'standard' and other.form == 'standard':
            return Complex(a=(self.a - other.a), b=(self.b - other.b))
        else:
            print('numbers should be in the standard form')

    def multiply(self, other):  # умножение
        if self.form == 'standard' and other.form == 'standard':
            return Complex(a=(self.a * other.a - self.b * other.b), b=(self.a * other.b + self.b * other.a))
        else:
            print('numbers should be in the standard form')

    def divide(self, other):  # деление
        if self.form == 'standard' and other.form == 'standard':
            return Complex(a=((self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2)),
                       b=((self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)))
        else:
            print('numbers should be in the standard form')


# тесты

number = Complex()
number1 = Complex()
number2 = Complex()
print(number.get_ab())
number.set_form('exponential')
print(number.get_form(), number.get_rf())
number.set_rf(1, -1)
number1.set_ab(2, 1)
number2.set_ab(2, -3)
print(number.get_form(), number.get_rf())
print(number1.get_form(), number1.get_ab())
print(number2.get_form(), number2.get_ab())
sum = number1.add(number2)
dif = number1.subtract(number2)
mul = number1.multiply(number2)
div = number1.divide(number2)
print(sum.get_ab(), dif.get_ab(), mul.get_ab(), div.get_ab())


