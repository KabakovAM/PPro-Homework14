from string import ascii_letters

def delete_from_str(data:str):
    """
    Функция, удаляет из текста все символы кроме букв латинского алфавита и пробелов.
    >>> delete_from_str('hello world')
    'hello world'
    >>> delete_from_str('Hello World')
    'hello world'
    >>> delete_from_str('hello world?')
    'hello world'
    >>> delete_from_str('helloд цworld')
    'hello world'
    >>> delete_from_str('Helloд цWorld?')
    'hello world'
    """
    temp = []
    for char in data:
        if char in ascii_letters or char == ' ':
            temp.append(char)
    result = ''.join(temp)
    return result.lower()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)