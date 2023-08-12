from string import ascii_letters
import unittest


class TestCaseStr(unittest.TestCase):

    def test_method_1(self):
        self.assertEqual(delete_from_str('hello world'),
                         'hello world', msg='OK')

    def test_method_2(self):
        self.assertEqual(delete_from_str('Hello World'),
                         'hello world', msg='OK')

    def test_method_3(self):
        self.assertEqual(delete_from_str('hello world?'),
                         'hello world', msg='OK')

    def test_method_4(self):
        self.assertEqual(delete_from_str('helloд цworld'),
                         'hello world', msg='OK')

    def test_method_5(self):
        self.assertEqual(delete_from_str('Helloд цWorld?'),
                         'hello world', msg='OK')


def delete_from_str(data: str):
    temp = []
    for char in data:
        if char in ascii_letters or char == ' ':
            temp.append(char)
    result = ''.join(temp)
    return result.lower()


if __name__ == '__main__':
    unittest.main()
