number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=4
y=[]
while i<len(n):
    a=0
    while a<len(n):
        if n[i]+n[a]==number:
            j=([n[i],n[a]])
            y.append(j)
        a=a+1
    i=i+1
print(y)

# num=int(input("enter the no."))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num=num//10
# print("rev num=",rev//10*10 )

