import requests
from config import *


def numb(i):"""

    :param i: введенный номер страницы
    :return: преобразованный номер страницы 
    """
    if i > 1:
        i = i * 10 - 9
    return i

def find(search, number):"""

    :param search: введеный текст пользователя, 
    :param number: введенное число страницы, преобразованное функцией numb()
    :return: название страницы и её ссылка
    """
    payload = {'key': API, 'cx': cx, 'q': search, 'start': number}
    r = requests.get('https://www.googleapis.com/customsearch/v1', payload).json()
    for names in r['items']:
        print(names['title'], names['link'])

print('Type the search')
search = str(input())

print('Type the number')
find(search, numb(int(input())))
print("choose another page or quit")
i = input()
while i != 'quit':
    """
    цикл для перехода к другим страницам
    """
    find(search, numb(int(i)))
    print("choose another page or quit")
    i = input()









