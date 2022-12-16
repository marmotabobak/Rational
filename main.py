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

# ----- ASSERT ------
# get_gcd()
gcd_nums = ((140, 96, 4), (16, 24, 8), (15, 60, 15), (10, 15, 5), (45, 56, 1), (21, 49, 7), (2, 7, 1))
assert all(get_gcd(x, y) == z for (x, y, z) in gcd_nums), '!WARNING! Некорректная отработка get_gcd()'
assert all(get_gcd_recur(x, y) == z for (x, y, z) in gcd_nums), '!WARNING! Некорректная отработка get_gcd_recur()'


