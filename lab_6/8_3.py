suma = 0
n = int(input("Fn, n = "))

def fib(a):
    if a == 1: return 1
    if a == 0: return 0
    return fib(a-1) + fib(a-2)

print(fib(n))