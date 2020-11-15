def fib(n):
    if n == 1 or n == 0:
        return n
    return fib(n-1) + fib(n-2)

print(fib(3))
print(fib(5))

for i in range(10):
    print(i)