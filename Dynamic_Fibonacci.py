#bottom-up approach

def fib(n):
    if n==1 or n==2:
        return 1 
    
    memo = [None]*(n+1)
    memo[1]  = 1
    memo[2]  = 1

    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
        
    return memo[n]


x = int(input('Enter Nth Fibonacci Number u want to print : '))
print(fib(x))
    

