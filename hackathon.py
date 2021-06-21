# num=int(input("enter the no."))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num=num//10
# print("rev num=",rev//10*10 )



# num=int(input("enter the number"))
# i=1
# while i<=num:
#     j=1
#     while j<=num-i:
#         print(" ",end="")
#         j=j+1
#     k=1
#     while k<i:
#         print(k,end="")
#         k=k+1
#     b=i
#     while b>0:
#         print(b,end="" )
#         b=b-1
#     print()
    # i=i+1



# i=1
# while i<=50:
#     # num=int(input("enter the no."))
#     if i%3==0 and i%5==0:
#         print("fizz buzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print("number")
#     print(i)
#     i=i+1





# row=int(input("enter the no. of row"))
# column=int(input("enter the no. of column"))
# i=1
# while i<=row:
#     j=1
#     while j<=column:
#         if i%2!=0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#         j=j+1
#     i=i+1
#     print()
    



# num=int(input("enter the number"))
# i=1
# while i<=num:
#     if i%9==0:
#         print("weired")
#     elif i%2==0 and num<=5:
#         print(" not weired")
#     elif i%6==0 and i%20==0:
#         print(" weired")
#     else:
#         print("not weired")
#     print(i)
#     i+=1



# i=0
# a=65
# while i<=97:
#     print(chr(a),end="")
#     a=a+1
#     print()
#     i=i+1



# num=int(input(" enter the no."))
# i=0
# while i<1:
#     print((num*num)+(num-1)*(num-1))
#     i=i+1



# num=int(input("enter the no."))
# i=0
# sum=0
# count=int(input("enter the no."))
# while i<count:
#     s=num*(10**i)
#     sum=sum+s
#     print(s,"",end="")
#     i=i+1
# print("series",sum)