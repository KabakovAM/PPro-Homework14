import unittest


class TestCaseStr(unittest.TestCase):

    def test_method_1(self):
        a = Square(10, 5)
        a.square_perimeter()
        self.assertEqual(a.perimeter, 30, msg='OK')

    def test_method_2(self):
        a = Square(10, 5)
        a.square_area()
        self.assertEqual(a.area, 50, msg='OK')

    def test_method_3(self):
        a = Square(10, 5)
        a.square_perimeter()
        b = Square(30, 24)
        b.square_perimeter()
        c = a.__add__(b)
        self.assertEqual(c.perimeter, 138, msg='OK')

    def test_method_4(self):
        a = Square(10, 5)
        a.square_perimeter()
        b = Square(30, 24)
        b.square_perimeter()
        c = a.__sub__(b)
        self.assertEqual(c.perimeter, 78, msg='OK')


class Square ():
    """Класс прямоугольник"""

    def __init__(self, len_a=None, len_b=None, perimeter=None):
        """Инициализация класса"""
        if len_b == None:
            self.len_a = len_a
            self.len_b = len_a
        else:
            self.len_a = len_a
            self.len_b = len_b
        self.perimeter = perimeter

    def square_perimeter(self):
        """Расчёт периметра прямоугольника"""
        self.perimeter = 2*self.len_a + 2*self.len_b

    def square_area(self):
        """Расчёт площади прямоугольника"""
        self.area = self.len_a*self.len_b

    def __add__(self, other):
        """Сложение периметров прямоугольников"""
        return Square(perimeter=self.perimeter + other.perimeter)

    def __sub__(self, other):
        """Вычитание периметров прямоугольника"""
        return Square(perimeter=abs(self.perimeter - other.perimeter))

    def __str__(self):
        """Вывод информации в терминал для пользователя"""
        return f'Экземпляр класса Square со сторонами {self.len_a} и {self.len_b}'

    def __repr__(self):
        """Вывод информации в терминал для разработчика"""
        return f'Square({self.len_a}, {self.len_b}, {self.perimeter}, {self.area})'

    def print_perimeter(self):
        """Вывод периметра в терминал"""
        return self.perimeter


if __name__ == '__main__':
    unittest.main()