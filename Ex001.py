from string import ascii_letters

def delete_from_str (data:str):
    temp = []
    for char in data:
        if char in ascii_letters or char == ' ':
            temp.append(char)
    result = ''.join(temp)
    return result.lower()

if __name__ == '__main__':
    data = 'Привет5 поT tа'
    print(delete_from_str(data))