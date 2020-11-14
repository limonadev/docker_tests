import threading
import requests

url = 'http://34.69.153.204/code'

f = open('test.py', 'r')
content = ''.join(f.readlines())
f.close()

def thread_function():
    response = requests.post(url, data = content)
    print(response.text)

thread1 = threading.Thread(target=thread_function)
thread2 = threading.Thread(target=thread_function)

thread1.start()
thread2.start()

'''import requests

url = 'http://34.69.153.204/code'

f = open('test.py', 'r')
content = ''.join(f.readlines())
f.close()

r = requests.post(url, data = content)
print(r.text)'''