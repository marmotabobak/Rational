def get_gcd(num1: int, num2: int) -> int:
    '''
    Функция поиска НОД по Эвклиду
    :param num1: первое число
    :param num2: второе число
    :return: НОД по алгоритму Евклида
    '''

    try:
        rest = max(num1, num2) % min(num1, num2)
    except ZeroDivisionError:
        # нужна кастомная отработка ошибки?
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

def get_gcd_recur(num1: int, num2: int) -> int:
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
            return get_gcd_recur(min(num1, num2), rest)


class Rational:
    '''
    Класс рациональных чисел
    '''

    def __init__(self, num: int, den: int):
        '''
        :param num: числитель - целое число
        :param den: знаменатель - целове число
        '''

        if den == 0:
            # добавить обработчик исключения
            raise ZeroDivisionError('Знаменатель дроби не может быть равен нулю')

        try:
            num = int(num)
            den = int(den)
        except TypeError:
            # добавить обработчик исключения
            pass
        except ValueError:
            # добавить обработчик исключения
            pass
        except ZeroDivisionError:
            # добавить обработчик исключения
            pass

        # установка знака дроби
        self.num, self.den = abs(num), abs(den)

        if num != 0:
            if num/abs(num) * den/abs(den) > 0:
                self.positive = True
            elif num/abs(num) * den/abs(den) < 0:
                self.positive = False

        # сокращение дроби
        self.shorten()

    @property
    def float(self):
        '''
        Возвращает float представление дроби
        :return: частное числителя на знаменатель, умноженное на знак дроби
        '''
        return self.sign() * self.num / self.den

    def sign(self):
        '''
        Функция определения знака дроби по признаку positive
        :return: +1 для положительной дроби, -1 для отрицательной, 0 для нулевой
        '''
        try:
            return (-1) * (-1) ** self.positive
        except AttributeError:
            return 0

    def shorten(self):
        '''
        Метод скоращения дроби
        '''
        try:
            gcd = get_gcd(self.num, self.den)
            if gcd > 1:
                self.num //= gcd
                self.den //= gcd
        except:
            # добавить обработчик исключения
            pass

    def __str__(self) -> str:
        '''
        Строковое представление объекта для отладки
        :return: Строковое значение свойства float
        '''
        return str(self.float)

    def __repr__(self) -> str:
        '''
        Строковое представление объекта
        :return: Строковое представление: +/-числитель/знаменатель
        '''
        num = self.sign() *self.num
        return f'{num}/{self.den}'

    def __add__(self, other):
        '''
        Метод сложения для дробей
        :param other: второе слагаемое
        :return: Сумма типа Rational
        '''

        if type(other) not in (Rational, int):
            raise ArithmeticError('Операции типа Rational можно проводить только с дробями типа Rational или целыми числами')

        if isinstance(other, int):
            other = Rational(other, 1)

        # вычисление числителя
        num = self.sign() * self.num * other.den + other.sign() * other.num * self.den
        # вычисление знаменателя
        den = self.den * other.den

        return Rational(num, den)

    def __radd__(self, other):
        '''
        Метод сложения для дроби с числом
        :param other: второе слагаемое
        :return: Сумма слагаемых
        '''

        return self + other

    def __sub__(self, other):
        '''
        Метод вычитания дробей
        :param other: вычитаемое
        :return: Разность типа Rational
        '''

        if type(other) not in (Rational, int):
            raise ArithmeticError('Операции типа Rational можно проводить только с дробями типа Rational или целыми числами')

        if isinstance(other, int):
            other = Rational(other, 1)

        # вычисление числителя
        num = self.sign() * self.num * other.den + (-1) * other.sign() * other.num * self.den
        # вычисление знаменателя
        den = self.den * other.den

        return Rational(num, den)

    def __rsub__(self, other):
        '''
        Метод вычитания для дроби с числом
        :param other: вычитаемое
        :return: Разность
        '''

        if type(other) not in (Rational, int):
            raise ArithmeticError('Операции типа Rational можно проводить только с дробями типа Rational или целыми числами')

        if isinstance(other, int):
            other = Rational(other, 1)

        num1 = other
        num2 = self

        return num1 - num2

    def __mul__(self, other):
        '''
        Метод умножения дробей
        :param other: второй множитель
        :return: Произведение типа Rational
        '''

        if type(other) not in (Rational, int):
            raise ArithmeticError('Операции типа Rational можно проводить только с дробями типа Rational или целыми числами')

        if isinstance(other, int):
            other = Rational(other, 1)

        # вычисление числителя
        num = self.sign() * other.sign() * self.num * other.num
        # вычисление знаменателя
        den = self.den * other.den

        return Rational(num, den)

    def __rmul__(self, other):
        '''
        Метод умножения дроби на числом
        :param other: второй множитель
        :return: Произведение множителей
        '''

        return self * other
    def __truediv__(self, other):
        '''
        Метод деление дробей
        :param other: делитель
        :return: Частное типа Rational
        '''

        if type(other) not in (Rational, int):
            raise ArithmeticError('Операции типа Rational можно проводить только с дробями типа Rational или целыми числами')

        if isinstance(other, int):
            other = Rational(other, 1)

        if other.num == 0:
            raise ZeroDivisionError('На ноль делить нельзя')

        # вычисление числителя
        num = self.sign() * other.sign() * self.num * other.den
        # вычисление знаменателя
        den = self.den * other.num

        return Rational(num, den)

    def __rtruediv__(self, other):
        '''
        Метод деление дробей
        :param other: делитель
        :return: Частное типа Rational
        '''

        if type(other) not in (Rational, int):
            raise ArithmeticError('Операции типа Rational можно проводить только с дробями типа Rational или целыми числами')

        if isinstance(other, int):
            other = Rational(other, 1)

        num1 = other
        num2 = self

        return num1 / num2


# ----- ASSERT ------
# get_gcd()
gcd_nums = ((140, 96, 4), (16, 24, 8), (15, 60, 15), (10, 15, 5), (45, 56, 1), (21, 49, 7), (2, 7, 1))
assert all(get_gcd(x, y) == z for (x, y, z) in gcd_nums), '!WARNING! Некорректная отработка get_gcd()'
assert all(get_gcd_recur(x, y) == z for (x, y, z) in gcd_nums), '!WARNING! Некорректная отработка get_gcd_recur()'
# class Rational: basics
test_fraction_1 = Rational(-3, 4)
assert test_fraction_1.num == 3 and test_fraction_1.den == 4 and not test_fraction_1.positive, '!WARNING! Некорректная отработка Rational'
test_fraction_1 = Rational(-0, 4)
assert test_fraction_1.num == 0 and test_fraction_1.den == 4, '!WARNING! Некорректная отработка Rational'
test_fraction_1 = Rational(3, 4)
assert test_fraction_1.num == 3 and test_fraction_1.den == 4 and test_fraction_1.positive, '!WARNING! Некорректная отработка Rational'
test_fraction_2 = Rational(18, 36)
assert test_fraction_2.num == 1 and test_fraction_2.den == 2 and test_fraction_2.positive, '!WARNING! Некорректная отработка сокращения дроби в shorten() в Rational'
try:
    Rational(1, 0)
except ZeroDivisionError as e:
    assert str(e) == 'Знаменатель дроби не может быть равен нулю', '!WARNING! Некорректная отработка исклюения ноля в знаменателе дроби в Rational'
# class Rational: float
assert Rational(-0, 156).float == 0, '!WARNING! Некорректная отработка float в Rational'
assert Rational(22, -745).float == -1 * 22 / 745, '!WARNING! Некорректная отработка float в Rational'
# class Rational: __repr_, __str__
assert str(Rational(-1, 25)) == str(Rational(1, -25).float), '!WARNING! Некорректная отработка __str__ в Rational'
assert repr(Rational(1, -25)) == '-1/25', '!WARNING! Некорректная отработка __repr__ в Rational'
# class Rational: __add__
assert repr(Rational(1, 3) + Rational(2, 3)) == repr(Rational(1, 1)), '!WARNING! Некорректная отработка __add__ в Rational'
assert repr(Rational(1, 3) + Rational(2, -3)) == repr(Rational(-1, 3)), '!WARNING! Некорректная отработка __add__ в Rational'
assert repr(Rational(2, 7) + Rational(3, 8)) == repr(Rational(37, 56)), '!WARNING! Некорректная отработка __add__ в Rational'
assert repr(Rational(0, 10) + Rational(-3, 8)) == repr(Rational(3, -8)), '!WARNING! Некорректная отработка __add__ в Rational'
assert str(Rational(0, 10) + Rational(-0, 8)) == str(Rational(0, -8)), '!WARNING! Некорректная отработка __add__ в Rational'
assert repr(Rational(1, 10) + 1) == repr(Rational(11, 10)), '!WARNING! Некорректная отработка __add__ с целым цислом в Rational'
try:
    repr(Rational(1, 10) + (1, 2)) == repr(Rational(11, 10))
except ArithmeticError as e:
    assert str(e) == 'Операции типа Rational можно проводить только с дробями типа Rational или целыми числами', '!WARNING! Некорректная отработка исклюячений __add__ в Rational'
assert repr(1 + Rational(1, 10)) == repr(Rational(11, 10)), '!WARNING! Некорректная отработка __radd__ с целым цислом в Rational'
assert repr(Rational(0, 1000) + Rational(1, 5555)) == repr(Rational(1, 5555)), '!WARNING! Некорректная отработка __sub__ в Rational'
assert repr(Rational(1, 3) - Rational(2, -3)) == repr(Rational(1, 1)), '!WARNING! Некорректная отработка __sub__ в Rational'
assert repr(Rational(1, 3) - Rational(2, 3)) == repr(Rational(-1, 3)), '!WARNING! Некорректная отработка __sub__ в Rational'
assert repr(Rational(-2, 7) - Rational(3, 8)) == repr(Rational(-37, 56)), '!WARNING! Некорректная отработка __sub__ в Rational'
assert repr(Rational(1, 10) - 1) == repr(Rational(-9, 10)), '!WARNING! Некорректная отработка __sub__ с целым цислом в Rational'
try:
    repr(Rational(1, 10) - (1, 2)) == repr(Rational(11, 10))
except ArithmeticError as e:
    assert str(e) == 'Операции типа Rational можно проводить только с дробями типа Rational или целыми числами', '!WARNING! Некорректная отработка исклюячений __sub__ в Rational'
assert repr(1 - Rational(1, 10)) == repr(Rational(9, 10)), '!WARNING! Некорректная отработка __rsub__ с целым цислом в Rational'
assert repr(Rational(1, 3) * Rational(2, -3)) == repr(Rational(-2, 9)), '!WARNING! Некорректная отработка __mul__ в Rational'
assert repr(Rational(1, 3) * Rational(3, 1)) == repr(Rational(1, 1)), '!WARNING! Некорректная отработка __mul__ в Rational'
assert repr(Rational(-2, 7) * Rational(3, 8)) == repr(Rational(-6, 56)), '!WARNING! Некорректная отработка __mul__ в Rational'
assert str(Rational(0, 777) * Rational(3, 8)) == str(Rational(0, 56)), '!WARNING! Некорректная отработка __smul__ в Rational'
assert repr(Rational(1, 10) * 2) == repr(Rational(1, 5)), '!WARNING! Некорректная отработка __mul__ с целым цислом в Rational'
try:
    repr(Rational(1, 10) * (1, 2)) == repr(Rational(11, 10))
except ArithmeticError as e:
    assert str(e) == 'Операции типа Rational можно проводить только с дробями типа Rational или целыми числами', '!WARNING! Некорректная отработка исклюячений __mul__ в Rational'
assert repr(0 * Rational(1, 10)) == repr(Rational(0, 10)), '!WARNING! Некорректная отработка __rmul__ с целым цислом в Rational'
assert repr(Rational(1, 3) / Rational(2, -3)) == repr(Rational(-3, 6)), '!WARNING! Некорректная отработка __truediv__ в Rational'
assert repr(Rational(1, 3) / Rational(3, 1)) == repr(Rational(1, 9)), '!WARNING! Некорректная отработка __truediv__ в Rational'
assert repr(Rational(-2, 7) / Rational(3, 8)) == repr(Rational(16, -21)), '!WARNING! Некорректная отработка __truediv__ в Rational'
assert repr(Rational(1, 10) / 2) == repr(Rational(1, 20)), '!WARNING! Некорректная отработка __truediv__ с целым цислом в Rational'
try:
    repr(Rational(1, 10) / (1, 2)) == repr(Rational(11, 10))
except ArithmeticError as e:
    assert str(e) == 'Операции типа Rational можно проводить только с дробями типа Rational или целыми числами', '!WARNING! Некорректная отработка исклюячений __truediv__ в Rational'
assert repr(1 / Rational(1, 10)) == repr(Rational(10, 1)), '!WARNING! Некорректная отработка __rtruediv__ с целым цислом в Rational'
try:
    Rational(1, 1) / Rational(0, 1)
except ZeroDivisionError as e:
    assert str(e) == 'На ноль делить нельзя', '!WARNING! Некорректная отработка исключени деления на ноль в __truediv__ в Rational'


rnum_1 = Rational(num=2, den=5)
rnum_2 = Rational(num=-3, den=7)
print(repr(rnum_1 + rnum_2), repr(rnum_1 - rnum_2), repr(rnum_1 * rnum_2), repr(rnum_1 / rnum_2))
