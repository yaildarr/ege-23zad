def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x+1, y) + f(x+4, y) + f(x*3, y)
print(f(2,46))