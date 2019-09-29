def func():
    for i in range(2):
        yield i

g = func()
while True:
    try:
        print(g.__next__())
    except:
        break


















