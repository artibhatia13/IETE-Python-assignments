def find_factorial(x):
    fac=1
    for i in range(1, x+1):
        fac *= i
    return fac

def find_nCr(n, r):
    nCr = find_factorial(n) / (find_factorial(n-r)*find_factorial(r))
    return nCr

n = input('enter no of rows to be printed : ')
n = int(n)

for i in range(1, n+1):
    for k in range(0, i):
        nCr = find_nCr(i, k)
        print(int(nCr), end=' ')
    print()
    


