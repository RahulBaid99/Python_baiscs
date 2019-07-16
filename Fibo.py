def seq(length):
    if(length <= 1):
        return length
    else:
        return (seq(length-1) + seq(length-2))

x = int(input("Enter number of terms:"))
#We count 1 as 1st position
if x<=0:
    print("Enter valid number")
else:
    print("nth number in sequence")
# This is x-1 as to find the number at xth position otherwise it will print number at x+1 position
    print(seq(x-1))
print("Fibonacci sequence")
for i in range(x):
    print(seq(i))