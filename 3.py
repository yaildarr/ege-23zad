def IsNotPrime(n):
    d=2
    k=2
    if n==2:
        return 1
    while d*d<=n:
        if n%d==0:
            return 1
        d+=1
    return 0

def f(x, y):
    if x > y or IsNotPrime(x)==0:
        return 0
    if x == y:
        return 1
    else:
        return (f(x+1,y) + f(x+5, y) + f(x*2,y))
print(f(9,14)*f(14,35))
