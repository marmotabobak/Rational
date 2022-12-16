from typing import Union
import functools

class LessThanZero(Exception):
    pass

# была задумка сделать кастомный обработчик исключений, но неправктично оказалось - отменяю и более не использую далее
def custom_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, *kwargs)
        except ZeroDivisionError:
            return 'ERR_1'
        except TypeError:
            return 'ERR_2'
        except ValueError:
            return 'ERR_3'
    return wrapper

def get_gcd(num1: int, num2: int) -> int:
    '''
    :param num1: первое число
    :param num2: второе число
    :return: НОД по алгоритму Евклида
    '''

    try:
        rest = max(num1, num2) % min(num1, num2)
    except ZeroDivisionError:
        raise
    else:
        if rest == 0:
            return min(num1, num2)
        a, b = min(num1, num2), rest
        while rest > 0:
            rest = a % b
            if rest > 0:
                a, b = b, rest
        return b

def get_gcd_euklide(num1: int, num2: int) -> int:
    '''
    :param num1: первое число
    :param num2: второе число
    :return: НОД по алгоритму Евклида рекурсией
    '''

    try:
        rest = max(num1, num2) % min(num1, num2)
    except ZeroDivisionError:
        raise
    else:
        if rest == 0:
            return min(num1, num2)
        else:
            return get_gcd_euklide(min(num1, num2), rest)

class Rational:
    '''
    Класс рациональных чисел
    '''

    def __init__(self, num: int, den: int):
        '''
        :param num: числитель
        :param den: знаменатель
        :param sign: знак дроби (определяется по числителю); либо 0; осознанно сделал int (не bool), чтобы проще работать с нулевым значением и знаком +/- в арифметике
        '''

        try:
            # знаменатель - натуральное число
            if den <= 0:
                # добавить обработчик исключения
                raise LessThanZero

            # установка знака дроби
            if num > 0:
                sign = 1
            elif num < 0:
                sign = -1
            else:
                sign = 0

            self.num = int(abs(num))
            self.den = int(abs(den))
            self.sign = sign

            # сокращение дроби
            self.shorten()

        except TypeError:
            # добавить обработчик исключения
            raise
        except ValueError:
            # добавить обработчик исключения
            raise

    def add(self, fraction_2):
        '''
        :param num: Прибавляемое слагаемое
        :return: Сумма
        '''

        # вычисление числителя
        self.num = self.sign * self.num * fraction_2.den + fraction_2.sign * fraction_2.num * self.den
        print('num:', fraction_2.num, end=' ')
        print('den', fraction_2.den, end=' ')
        print('sign', fraction_2.sign, end=' ')

        # определение знака (по знаку числителя)
        if self.num > 0:
            self.sign = 1
        elif self.num < 0:
            self.sign = -1
        else:
            self.sign = 0

        # удаление знака у числителя
        self.num = abs(self.num)

        # вычисление знаменателя
        self.den = self.den * fraction_2.den

        # сокращение дроби
        self.shorten()

    def substract(self, fraction_2):
        '''
        :param num: Вычисаемое
        :return: Разность
        '''

        # изменение знака вычитаемого и реализация операции сложения с ним
        fraction_2.sign *= -1
        self.add(fraction_2)

    def multiply(self, fraction_2):
        '''
        :param num: Множитель
        :return: Произведение
        '''

        # вычисление числителя
        self.num = self.sign * fraction_2.sign * self.num * fraction_2.num

        # определение знака (по знаку числителя)
        if self.num > 0:
            self.sign = 1
        elif self.num < 0:
            self.sign = -1
        else:
            self.sign = 0

        # удаление знака у числителя
        self.num = abs(self.num)

        # вычисление знаменателя
        self.num = self.den * fraction_2.den

        # сокращение дроби
        self.shorten()

    def divide(self, fraction_2):
        '''
        :param num: Делитель
        :return: Частное
        '''

        # отработать ошибку деления на ноль
        if not fraction_2.sign:
            raise ZeroDivisionError

        # умножение на обратную дробь
        self.multiply(Rational(fraction_2.den, fraction_2.num, fraction_2.sign))

    @staticmethod
    def add_rationals(cls, num1, num2):
        '''
        :param num1:
        :param num2:
        :return:
        '''
        pass

    def shorten(self):
        try:
            gcd = get_gcd(self.num, self.den)
            if gcd > 1:
                self.num //= gcd
                self.den //= gcd
        except:
            # добавить обработчик исключения
            pass

    def __unshorten__(self, mult: int):
        '''
        Функция умножения (обратно сокращению) дроби - необходимо для некоторых арифметичесих операций
        :param mult:
        :return:
        '''

        try:
            mult = int(mult)
        except:
            pass
        else:
            self.num *= mult
            self.den *= mult



# ---- ASSERT ------
# zero_division_decorator
@custom_exceptions
def zero_div_test():
    try:
        return 1/0
    except ZeroDivisionError:
        raise
assert zero_div_test() == 'ERR_1', '!WARNING! Некорректная отработка custom_exceptions()'
# get_gcd()
gcd_nums = ((140, 96, 4), (16, 24, 8), (15, 60, 15), (10, 15, 5), (45, 56, 1), (21, 49, 7), (2, 7, 1))
assert all(get_gcd(x, y) == z for (x, y, z) in gcd_nums), '!WARNING! Некорректная отработка get_gcd()'
assert all(get_gcd_euklide(x, y) == z for (x, y, z) in gcd_nums), '!WARNING! Некорректная отработка get_gcd_euklide()'
# class Rational
test_fraction_1 = Rational(-3, 4)
assert test_fraction_1.num == 3 and test_fraction_1.den == 4 and test_fraction_1.sign == -1, '!WARNING! Некорректная отработка Rational'
test_fraction_1 = Rational(-0, 4)
assert test_fraction_1.num == 0 and test_fraction_1.den == 4 and test_fraction_1.sign == 0, '!WARNING! Некорректная отработка Rational'
test_fraction_1 = Rational(3, 4)
assert test_fraction_1.num == 3 and test_fraction_1.den == 4 and test_fraction_1.sign == 1, '!WARNING! Некорректная отработка Rational'
test_fraction_2 = Rational(18, 36)
assert test_fraction_2.num == 1 and test_fraction_2.den == 2 and test_fraction_2.sign == 1, '!WARNING! Некорректная отработка сокращения дроби в shorten() в Rational'

# арифметика дробей в классе Rational
test_fraction_1.add(Rational(1, 2))
assert test_fraction_1.num == 5 and test_fraction_1.den == 4 and test_fraction_1.sign == 1,  '!WARNING! Некорректная отработка add() в Rational'
test_fraction_1.add(Rational(0, 1))
assert test_fraction_1.num == 5 and test_fraction_1.den == 4 and test_fraction_1.sign == 1,  '!WARNING! Некорректная отработка add() в Rational'
test_fraction_1.add(Rational(-1, 4))
assert test_fraction_1.num == 1 and test_fraction_1.den == 1 and test_fraction_1.sign == 1,  '!WARNING! Некорректная отработка add() в Rational'
test_fraction_1.add(Rational(-5, 4))
assert test_fraction_1.num == 1 and test_fraction_1.den == 4 and test_fraction_1.sign == -1,  '!WARNING! Некорректная отработка add() в Rational'
test_fraction_1.add(Rational(1, 4))
assert test_fraction_1.num == 0 and test_fraction_1.den == 16 and test_fraction_1.sign == 0,  '!WARNING! Некорректная отработка add() в Rational'
test_fraction_1.substract(Rational(1, 4))
assert test_fraction_1.num == 1 and test_fraction_1.den == 4 and test_fraction_1.sign == -1,  '!WARNING! Некорректная отработка add() в Rational'





