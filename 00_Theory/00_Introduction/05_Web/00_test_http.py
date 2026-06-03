import requests as r
try:
    #response = r.get('https://httpbin.dev/delay/10', timeout = 3)
    response = r.get('https://jsonplaceholder.typicode.com/todos/1')

    print(response.json())
except r.exceptions.ReadTimeout:
    print('catturato errore')
