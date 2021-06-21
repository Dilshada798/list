num=int(input("enter number"))
j=1
while num>0:
    j=j*num
    num=num-1
    print("factorial",j)


# i=1
# while i<=100:
#     if i%2==0:
#         print(i,"even")
#     else:
#         print(i,"odd") 
#     i=i+1       



i=5
while i>=1:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print() 
    i=i-1


# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1 
  
#do
# i=1
# while i<=10:
#     a=1
#     while a<=10-i:
#         print(" ",end="")
#         a=a+1
#     k=1
#     while k<=i:
#         print("*",end=" ")
#         k=k+1
#     print() 
#     i=i+20


#diamond
# i=1
# j=4
# while i<=5:
#     print(" "*j+i*" *"+j*" ")
#     i=i+1
#     j-=1
# a=1
# b=4
# while b>0:
#     print(" "*a+b*" *"+a*" ") 
#     b=b-1
#     a=a+1   



# num=int(input("enter num:"))
# yn=num
# sum=0
# while num:
#     i=1
#     f=1
#     y=num%10
#     while i<=y:
#         f=f*i
#         i=i+1
#     sum=sum+f
#     num=num//10
# if sum==yn:
#     print(sum,"strong num")
# else:
#     print(sum,"not a strong num") 
  




# num=int(input("enter the number"))
# sum=0
# i=1
# while i<num:
#     if num%i==0:
#         sum=sum+i
#     i=i+1    
# if num==sum:
#     print(num,"perfect number")  
# else:
#     print(num,"not a perfect nummber") 

# # 
#    

# num=int(input("enter the number"))
# num1=int(input())
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num=num//10
# print(rev)
# print()



