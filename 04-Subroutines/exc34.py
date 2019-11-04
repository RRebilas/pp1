def fib(n):
    a, b = 0, 1
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1


for i in range(1, 21):
    print(fib(i))
