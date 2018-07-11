import requests
from config import *


def numb(i):
    """
    преобразует номер страницы в нужное значение start
    """
    if i > 1:
        i = i * 10 - 9
    return i

def find(search, number):
    """
    делает запрос с параметрами, получает json объект
    выводит из него название и ссылку страниц
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









