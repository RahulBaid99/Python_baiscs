def fibo(n):
    if n == 1 or n == 0:
        return 1
    else:

            n= n-1 + n-2
            return n;
x=int(input('Enter the nth number of fibo series'))
print(fibo(x))
