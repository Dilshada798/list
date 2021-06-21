num=int(input("enter the no."))
i=1
counter=0
while i<=num:
    if num%i==0:
        print(i)
        counter=counter+1
    i=i+1
if counter==2:
    print("it is prime no.")
else:
    print("it is not prime no.")



     

