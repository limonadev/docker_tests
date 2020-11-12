from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import sys
import json
import contextlib
from io import StringIO

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

#curl http://127.0.0.1:8000/code --header "Content-Type: text/plain"  --request POST --data "print('hola')"
@csrf_exempt 
def send_code(request):
    if request.method == 'POST':
        content = request.body.decode('utf-8')

        with stdoutIO() as s:
            try:
                exec(content)
            except Exception as e:
                print('PROGRAM FAILED: ')
                print(type(e))
                print(e)

        print(s.getvalue())
        return JsonResponse({'result': s.getvalue()}, safe=False)