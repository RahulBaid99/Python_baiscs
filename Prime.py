def prime(start,end):

    for val in range(start, end + 1):

        # If num is divisible by any number
        # between 2 and val, it is not prime
        if val > 1:
            for n in range(2, val//2):
                if (val % n) == 0:
                    break
            else:
                print(val);
x=int(input("enter First Number"))
y=int(input("enter Second Number"))
prime(x,y)