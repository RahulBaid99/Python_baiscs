def Fibonacci(n):
    if n<1:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 1
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        n= (n-1)+(n-2)
x=int(input('Enter the nth number of fibo series'))
print (Fibonacci(x))
