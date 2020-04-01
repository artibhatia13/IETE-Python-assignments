def find(n, from_, to, aux):
    if n == 1:
        print ("move disc 1 from ", from_, "-->", to)
        return
    find(n-1, from_, aux, to)
    print ("move disc", n, "from ", from_, "-->", to)
    find(n-1, aux, to, from_)

x = int(input('How many discs are there in Tower Of Hanoi : '))
find(x,'A', 'C', 'B')
no = 2**x - 1
print('No Of Moves = ', no)