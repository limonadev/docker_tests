import sys
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

f = open('test.py', 'r')
content = ''.join(f.readlines())
f.close()

with stdoutIO() as s:
    try:
        exec(content, globals())
    except Exception as e:
        print('PROGRAM FAILED: ')
        print(type(e))
        print(e)

print(s.getvalue())
