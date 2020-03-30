n = input('enter the limit')
n = int(n)
space = n

#for printing upper triangle of diamond

for i in range(0, n):
    for j in range(0,x):            #for printing spaces
        print(' ', end='')
    space-=1
    for k in range(0, i):           #for printing stars
        print('*', end=' ')
    print()

#for printing upper triangle of diamond

space = 0
for i in range(n, 0, -1):
    for j in range(0,x):
        print(' ', end='')
    space+=1
    for k in range(0, i):
        print('*', end=' ')
    print()