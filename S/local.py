import requests
from pprint import pprint
r = requests.get('http://127.0.0.1:5000/users')
print(r.status_code, r.headers, type(r.text), r.json())

r = requests.delete('http://127.0.0.1:5000/users', json={
    "user_id": 19,
    })