import unittest
import pytest


class TestCaseStr(unittest.TestCase):

    def test_method_1(self):
        self.assertEqual(leap_year(2000), True, msg='OK')

    def test_method_2(self):
        self.assertEqual(leap_year(2001), False, msg='OK')

    def test_method_3(self):
        self.assertEqual(simple_gen(3), [2, 3, 5], msg='OK')

    def test_method_4(self):
        self.assertEqual(simple_gen(2), [2, 3], msg='OK')


def test_method_1():
    assert leap_year(2000) == True, 'NOT OK'


def test_method_2():
    assert leap_year(2001) == False, 'NOT OK'


def test_method_3():
    assert simple_gen(3) == [2, 3, 5], 'NOT OK'


def test_method_4():
    assert simple_gen(2) == [2, 3], 'NOT OK'


def leap_year(year):
    """
    Функция - проверка на високосный год.
    >>> leap_year(2000)
    True
    >>> leap_year(2001)
    False
    """
    if year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False
    return result


def simple_gen(num):
    """
    Функция - генератор простых чисел.
    >>> simple_gen(3)
    [2, 3, 5]
    >>> simple_gen(2)
    [2, 3]
    """
    res = []
    i = 1
    data = 1
    while num != 0:
        check = 0
        while i <= data:
            if data % i == 0:
                check += 1
            i += 1
        if check == 2:
            res.append(data)
            num -= 1
        i = 1
        data += 1
    return res


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    # unittest.main()
    pytest.main()
