def g(x):
    return pow(x, 2)
def f(x):
    return pow(2,x)

def calcHalf(a,b):
    return a + abs(a - b)/2.0

def calcbisect(a,b):
    links = a
    rechts = b
    half = 0
    while abs(links - rechts) > 1.0E-13:
        half = calcHalf(links, rechts)
        if f(links) < g(links) and f(half) > g(half):
            rechts = half
        else:
            links = half
    return half

print(calcbisect(-1,0))