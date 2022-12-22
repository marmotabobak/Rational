import yaml
from sys import argv

class CriticalApplicationError(Exception):
    pass

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
            raise
        except ValueError:
            # добавить обработчик исключения
            raise
        except ZeroDivisionError:
            # добавить обработчик исключения
            raise

        # установка знака дроби
        self.num, self.den = abs(num), abs(den)

        if num != 0:
            if num/abs(num) * den/abs(den) > 0:
                self.positive = True
            elif num/abs(num) * den/abs(den) < 0:
                self.positive = False
            else:
                pass
        else:
            self.positive = True

        # сокращение дроби
        #self.shorten()

    @property
    def float(self):
        '''
        Возвращает float представление дроби
        :return: частное числителя на знаменатель, умноженное на знак дроби
        '''
        return self.sign() * self.num / self.den

    @staticmethod
    def get_gcd_recur(num1: int, num2: int) -> int:
        '''
        Метод поиска НОД по Эвклиду рекурсией
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
                return Rational.get_gcd_recur(min(num1, num2), rest)

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
        if self.num == 0:
            self. positive = True
            self.den = 1
            return self
        try:
            gcd = Rational.get_gcd_recur(self.num, self.den)
            if gcd > 1:
                self.num //= gcd
                self.den //= gcd
        except Exception as e:
            # добавить обработчик исключения
            raise
        return self

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

    @classmethod
    def __int_to_rational(cls, other):
        '''
        Метод приведения int к Rational
        :param other:
        :return:
        '''
        if type(other) not in (Rational, int):
            raise TypeError('Операции типа Rational можно проводить только с дробями типа Rational или целыми числами')

        return Rational(other, 1) if isinstance(other, int) else other

    def __add__(self, other):
        '''
        Метод сложения для дробей
        :param other: второе слагаемое
        :return: Сумма типа Rational
        '''

        other = self.__int_to_rational(other)

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

        other = self.__int_to_rational(other)

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

        other = self.__int_to_rational(other)

        num1 = other
        num2 = self

        return num1 - num2

    def __mul__(self, other):
        '''
        Метод умножения дробей
        :param other: второй множитель
        :return: Произведение типа Rational
        '''

        other = self.__int_to_rational(other)

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

        other = self.__int_to_rational(other)

        if other.num == 0:
            raise ZeroDivisionError('На ноль делить нельзя')

        # вычисление числителя
        num = self.sign() * other.sign() * self.num * other.den
        # вычисление знаменателя
        den = self.den * other.num

        return Rational(num, den)

    def __rtruediv__(self, other):
        '''
        Метод деление на дробь Rational
        :param other: частное
        :return: Частное от деления
        '''

        other = self.__int_to_rational(other)

        num1 = other
        num2 = self

        return num1 / num2

    def __eq__(self, other):

        other = self.__int_to_rational(other)

        return (self.num, self.den, self.positive) == (other.num, other.den, other.positive)

    def __gt__(self, other):

        other = self.__int_to_rational(other)

        if self.sign() > other.sign():
            return True
        elif self.sign() < other.sign():
            return False
        else:
            if self.positive:
                return self.num * other.den > other.num * self.den
            else:
                return self.num * other.den < other.num * self.den

    def __ge__(self, other):

        other = self.__int_to_rational(other)

        if self.sign() > other.sign():
            return True
        elif self.sign() < other.sign():
            return False
        else:
            if self.positive:
                return self.num * other.den >= other.num * self.den
            else:
                return self.num * other.den <= other.num * self.den

    def __setattr__(self, key, value):

        # Проверка на ноль в знаменателе
        if key == 'den' and value == 0:
            raise ZeroDivisionError('Знаменатель не может быть равен 0')

        # Если устанавливается ноль в числителе либо уже установлен, то установить 0/1
        if (key == 'num' and value == 0) or (key != 'num' and self.num == 0):
            object.__setattr__(self, 'num', 0)
            object.__setattr__(self, 'den', 1)
            object.__setattr__(self, 'positive', True)
        # иначе, если это операция по установке знака, то установить знак
        elif key == 'positive':
            object.__setattr__(self, key, value)
        # иначе, если это операция по  изменению числителя или знаменателя, то сократить и изменить
        elif ('num' in self.__dict__ and key == 'den') or (key == 'num' and 'den' in self.__dict__):
            num = self.num if 'num' in self.__dict__ else value
            den = self.den if 'den' in self.__dict__ else value
            try:
                gcd = Rational.get_gcd_recur(num, den)
                if gcd > 1:
                    num //= gcd
                    den //= gcd
                object.__setattr__(self, 'num', num)
                object.__setattr__(self, 'den', den)
            except Exception as e:
                # добавить обработчик исключения
                raise
        # иначе установить параметр - на момент комментария, единственный возможный кейс в данном случае - первоначальная инициализация с установкой int без установленного den
        else:
            object.__setattr__(self, key, value)

        #self.shorten()

if (len(argv) < 2):
    raise CriticalApplicationError('! CRTITICAL ! Должно быть передано имя файла последним аргументом.')
else:
    try:
        file_name = argv[-1]
    except Exception as e:
        # обработать необходимые ошибки
        raise

try:
    with open(file_name) as file:
        json_data = yaml.safe_load(file)
except FileNotFoundError as e:
    raise CriticalApplicationError('! CRITICAL ! Файл не найден. Сервис остановлен.') from None
except Exception as e:
    # отработать необходимые исключения
    raise

try:
    json_data
except Exception as e:
    raise CriticalApplicationError('! CRITICAL ! Ошибка в процессе парсинга файла. Сервис остановлен.')

for item in json_data:
    try:
        a = item['a']
        b = item['b'] if 'b' in item else a
        oper = item['operation']
    except KeyError as e:
        print(f'! WARNING ! Проверьте структуру файла с данными - отсутствуют необходимый ключ: {e}. Элемент пропущен: {item}')
        continue

    try:
        if '/' in a:
            a_num, a_den = (int(x) for x in a.split('/'))
        else:
            a_num = int(a)
            a_den = 1
        if '/' in b:
            b_num, b_den= (int(x) for x in b.split('/'))
        else:
            b_num = int(b)
            b_den = 1
    except ValueError as e:
        print(f'! WARNING ! Некорректный формат данных (должен быть Rational или int): {e} Элемент пропущен: {item}')
        continue
    except Exception as e:
        raise

    print(f'{a} {oper} {b} =', eval(f'repr(Rational({a_num}, {a_den}) {oper} Rational({b_num}, {b_den}))'))

# ----- ASSERT ------
# get_gcd()
gcd_nums = ((140, 96, 4), (16, 24, 8), (15, 60, 15), (10, 15, 5), (45, 56, 1), (21, 49, 7), (2, 7, 1))
assert all(get_gcd(x, y) == z for (x, y, z) in gcd_nums), '!WARNING! Некорректная отработка get_gcd()'
assert all(Rational.get_gcd_recur(x, y) == z for (x, y, z) in gcd_nums), '!WARNING! Некорректная отработка get_gcd_recur()'
# class Rational: basics
test_fraction_1 = Rational(-3, 4)
assert test_fraction_1.num == 3 and test_fraction_1.den == 4 and not test_fraction_1.positive, '!WARNING! Некорректная отработка Rational'
test_fraction_1 = Rational(-0, 4)
assert test_fraction_1.num == 0 and test_fraction_1.den == 1, '!WARNING! Некорректная отработка Rational'
test_fraction_1 = Rational(3, 4)
assert test_fraction_1.num == 3 and test_fraction_1.den == 4 and test_fraction_1.positive, '!WARNING! Некорректная отработка Rational'
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
# class Rational: dunders
assert str(Rational(1, 3) + Rational(2, 3)) == str(Rational(1, 1)), '!WARNING! Некорректная отработка __add__ в Rational'
assert str(Rational(1, 3) + Rational(2, -3)) == str(Rational(-1, 3)), '!WARNING! Некорректная отработка __add__ в Rational'
assert str(Rational(2, 7) + Rational(3, 8)) == str(Rational(37, 56)), '!WARNING! Некорректная отработка __add__ в Rational'
assert str(Rational(0, 10) + Rational(-3, 8)) == str(Rational(3, -8)), '!WARNING! Некорректная отработка __add__ в Rational'
assert str(Rational(0, 10) + Rational(-0, 8)) == str(Rational(0, -8)), '!WARNING! Некорректная отработка __add__ в Rational'
assert repr(Rational(1, 10) + 1) == repr(Rational(11, 10)), '!WARNING! Некорректная отработка __add__ с целым цислом в Rational'
try:
    repr(Rational(1, 10) + (1, 2)) == repr(Rational(11, 10))
except TypeError as e:
    assert str(e) == 'Операции типа Rational можно проводить только с дробями типа Rational или целыми числами', '!WARNING! Некорректная отработка исклюячений __add__ в Rational'
assert repr(1 + Rational(1, 10)) == repr(Rational(11, 10)), '!WARNING! Некорректная отработка __radd__ с целым цислом в Rational'
assert str(Rational(0, 1000) + Rational(1, 5555)) == str(Rational(1, 5555)), '!WARNING! Некорректная отработка __sub__ в Rational'
assert str(Rational(1, 3) - Rational(2, -3)) == str(Rational(1, 1)), '!WARNING! Некорректная отработка __sub__ в Rational'
assert str(Rational(1, 3) - Rational(2, 3)) == str(Rational(-1, 3)), '!WARNING! Некорректная отработка __sub__ в Rational'
assert str(Rational(-2, 7) - Rational(3, 8)) == str(Rational(-37, 56)), '!WARNING! Некорректная отработка __sub__ в Rational'
assert str(Rational(1, 10) - 1) == str(Rational(-9, 10)), '!WARNING! Некорректная отработка __sub__ с целым цислом в Rational'
try:
    repr(Rational(1, 10) - (1, 2)) == repr(Rational(11, 10))
except TypeError as e:
    assert str(e) == 'Операции типа Rational можно проводить только с дробями типа Rational или целыми числами', '!WARNING! Некорректная отработка исклюячений __sub__ в Rational'
assert repr(1 - Rational(1, 10)) == repr(Rational(9, 10)), '!WARNING! Некорректная отработка __rsub__ с целым цислом в Rational'
assert repr(Rational(1, 3) * Rational(2, -3)) == repr(Rational(-2, 9)), '!WARNING! Некорректная отработка __mul__ в Rational'
assert str(Rational(1, 3) * Rational(3, 1)) == str(Rational(1, 1)), '!WARNING! Некорректная отработка __mul__ в Rational'
assert str(Rational(-2, 7) * Rational(3, 8)) == str(Rational(-6, 56)), '!WARNING! Некорректная отработка __mul__ в Rational'
assert str(Rational(0, 777) * Rational(3, 8)) == str(Rational(0, 56)), '!WARNING! Некорректная отработка __smul__ в Rational'
assert str(Rational(1, 10) * 2) == str(Rational(1, 5)), '!WARNING! Некорректная отработка __mul__ с целым цислом в Rational'
try:
    repr(Rational(1, 10) * (1, 2)) == repr(Rational(11, 10))
except TypeError as e:
    assert str(e) == 'Операции типа Rational можно проводить только с дробями типа Rational или целыми числами', '!WARNING! Некорректная отработка исклюячений __mul__ в Rational'
assert repr(0 * Rational(1, 10)) == repr(Rational(0, 10)), '!WARNING! Некорректная отработка __rmul__ с целым цислом в Rational'
assert repr(Rational(1, 3) / Rational(2, -3)) == repr(Rational(-3, 6)), '!WARNING! Некорректная отработка __truediv__ в Rational'
assert repr(Rational(1, 3) / Rational(3, 1)) == repr(Rational(1, 9)), '!WARNING! Некорректная отработка __truediv__ в Rational'
assert repr(Rational(-2, 7) / Rational(3, 8)) == repr(Rational(16, -21)), '!WARNING! Некорректная отработка __truediv__ в Rational'
assert repr(Rational(1, 10) / 2) == repr(Rational(1, 20)), '!WARNING! Некорректная отработка __truediv__ с целым цислом в Rational'
try:
    repr(Rational(1, 10) / (1, 2)) == repr(Rational(11, 10))
except TypeError as e:
    assert str(e) == 'Операции типа Rational можно проводить только с дробями типа Rational или целыми числами', '!WARNING! Некорректная отработка исклюячений __truediv__ в Rational'
assert repr(1 / Rational(1, 10)) == repr(Rational(10, 1)), '!WARNING! Некорректная отработка __rtruediv__ с целым цислом в Rational'
try:
    Rational(1, 1) / Rational(0, 1)
except ZeroDivisionError as e:
    assert str(e) == 'На ноль делить нельзя', '!WARNING! Некорректная отработка исключени деления на ноль в __truediv__ в Rational'
assert Rational(-1, 2) == Rational(4, -8), '!WARNING! Некорректная отработка __eq__ в Rational'
assert Rational(-2, 2) == -1, '!WARNING! Некорректная отработка __eq__ в Rational'
assert Rational(0, 2) == Rational(0, -100), '!WARNING! Некорректная отработка __eq__ в Rational'
assert Rational(1, 2) != Rational(-1, 2), '!WARNING! Некорректная отработка __eq__ в Rational'
assert Rational(1, 2) > Rational(1, 4), '!WARNING! Некорректная отработка __gt__ в Rational'
assert Rational(-1, 2) < Rational(1, -4), '!WARNING! Некорректная отработка __gt__ в Rational'
assert Rational(-1, 2) < Rational(0, 1), '!WARNING! Некорректная отработка __gt__ в Rational'
assert Rational(1, 2) >= Rational(0, 1), '!WARNING! Некорректная отработка __ge__ в Rational'
assert Rational(1, -2) <= Rational(0, 1), '!WARNING! Некорректная отработка __ge__ в Rational'
assert Rational(-1, 2) >= Rational(-10, 3), '!WARNING! Некорректная отработка __ge__ в Rational'
assert Rational(-1, 2) <= Rational(1, -2), '!WARNING! Некорректная отработка __ge__ в Rational'
assert Rational(-1, -2) >= Rational(2, 4), '!WARNING! Некорректная отработка __ge__ в Rational'
test_fraction_2 = Rational(18, 36)
assert test_fraction_2.num == 1 and test_fraction_2.den == 2 and test_fraction_2.positive, '!WARNING! Некорректная отработка сокращения дроби в __setattr__ в Rational'
try:
    test_fraction_2 = Rational(18, 0)
except ZeroDivisionError as e:
    assert str(e) == 'Знаменатель дроби не может быть равен нулю', '!WARNING! Некорректная отработка исключения нулевого знаменателя в Rational'
