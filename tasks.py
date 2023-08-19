import requests

params = {
    'limit': 150,
    'skip': 0,
}
url = 'https://dummyjson.com/todos'

response = requests.get(url=url, params=params)
result = response.json()

todos = result['todos']

print('all outstanding tasks:\n')
for task in todos:
    if task['completed'] is False:
        print(task['todo'])
