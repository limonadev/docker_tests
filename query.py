import requests

url = 'http://127.0.0.1:8000/code'

f = open('test.py', 'r')
content = ''.join(f.readlines())
f.close()

r = requests.post(url, data = content)
print(r.text)