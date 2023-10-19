def fibonacci(n):
    i = 0
    if n <= 1:
        return(n)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
    
n = 12
for i in range(n):
    print(fibonacci(i))