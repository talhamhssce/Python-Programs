def add(a, b = 5):
    return a + b

print(add(5))
print(add(5,10))

def f(a, L=[]):
    L.append(a)
    return L

def findSquares(L = [], Q = []):
    for i in range(1, 11):
        L.append(i**2)
        Q.append(i**3)
    return L, Q    


