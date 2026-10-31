def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
print("每次重新调用next(fib(n))")
print(next(fib(6)))
print(next(fib(6)))
print(next(fib(6)))

fb=fib(6)
print("为fb=fib(n)属性赋值，再调用next")
print(next(fb))
print(next(fb))
print(next(fb))

print("遍历fib(n)")
for n in fib(6):
    print(n)

print("获取fib的返回值")
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

