def f(x, y):
    if x > y or x == 46:
        return 0
    if x == y:
        return 1
    else:
        return (f(x+3,y) + f(x+5, y) + f(x*2,y))
print(f(1,24)*f(24,60))
