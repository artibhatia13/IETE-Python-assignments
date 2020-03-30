a = 0 
b = 1 
c = 0
n = input('how many numbers do you want to print : ')
print('1')
for i in range(0, int(n)):
    c=a+b
    print(c, end=' ')
    a=b
    b=c


