def fib_rec(n):
    pass
    if n <= 1:
        return n
    return fib_rec(n - 1) +  fib_rec(n - 2)

def fib_iter(n):
    pass
    if n <= 1:
        return n
    a = 0
    b = 1
    c = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c


print("ENTER THE VALUE OF N: ")
n = int(input())

rec = list()
ite = list()

for i in range(n + 1):
    rec.append(fib_rec(i))
    ite.append(fib_iter(i))

print(rec)
print(ite)
