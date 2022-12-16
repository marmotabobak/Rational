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
        return self.sign() * self.num / self.den

    def sign(self):
        '''
        Функция определения знака дроби по признаку positive
        :return: +1 для положительной дроби, -1 для отрицаиельной, 0 для нулевой
        '''
        try:
            return (-1) * (-1) ** self.positive
        except AttributeError:
            return 0

    def shorten(self):
        try:
            gcd = get_gcd(self.num, self.den)
            if gcd > 1:
                self.num //= gcd
                self.den //= gcd
        except:
            # добавить обработчик исключения
            pass


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
# class Rational: float
assert Rational(-0, 156).float == 0, '!WARNING! Некорректная отработка float в Rational'
assert Rational(22, -745).float == -1 * 22 / 745, '!WARNING! Некорректная отработка float в Rational'

