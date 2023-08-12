from string import ascii_letters
import pytest

def delete_from_str(data: str):
    temp = []
    for char in data:
        if char in ascii_letters or char == ' ':
            temp.append(char)
    result = ''.join(temp)
    return result.lower()

def test_method_1():
    assert delete_from_str('hello world') == 'hello world', 'NOT OK'

def test_method_2():
    assert delete_from_str('Hello World') == 'hello world', 'NOT OK'

def test_method_3():
    assert delete_from_str('hello world?') == 'hello world', 'NOT OK'

def test_method_4():
    assert delete_from_str('helloд цworld') == 'hello world', 'NOT OK'

def test_method_5():
    assert delete_from_str('Helloд цWorld?') == 'hello world', 'NOT OK'

if __name__ == '__main__':
    pytest.main()
