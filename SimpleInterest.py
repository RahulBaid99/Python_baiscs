def si(pr,ra,ti):

    simpl=float((pr*ra*ti)/100)
    print (simpl);

#here the input type should be in  type float as interest can be in decimal
p=float(input("Enter the principal amount"))
r=float(input("Enter the rate "))
t=float(input("Enter the Time in years"))
si(p,r,t)
