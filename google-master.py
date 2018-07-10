import requests
from config import *
import json
search = str(input())


#https://www.googleapis.com/customsearch/v1?key=INSERT_YOUR_API_KEY&cx=017576662512468239146:omuauf_lfve&q=lectures

URL = 'https://www.googleapis.com/customsearch/v1'
payload = {'key': API, 'cx': cx, 'q': search}
r =requests.get(URL, params=payload)
r = r.json()

for names in r['items'][0:5]:
    print(names['title'], names['link'])

print ('Do you want to go to a next page? y/n')
var = input()
if var == 'y':
    for names in r['items'][6:10]:
        print(names['title'], names['link'])
else:
    print('Goodbye!')



