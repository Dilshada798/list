elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
a=[]
b=[]
i=0
sum=0
sum1=0
while i<len(elements):
    k=elements[i]
    if k%2==0:
        a.append(k)
        sum=sum+k
    else:
        b.append(k)
        sum1=sum1+k
    i=i+1
print("sum of even",a,sum)
print("odd number",b,sum1)





elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
a=[]
b=[]
i=0
sum=0
sum1=0
avg=0
while i<len(elements):
    k=elements[i]
    if k%2==0:
        a.append(k)
        sum=sum+k
        avg=sum/avg
    # average=sum/len(elements)
    else:
        b.append(k)
        sum1=sum1+k
        avg=sum/avg
        # average=sum//len(elements)
    i=i+1
print("sum of even",a,sum,"average",average)
print("odd number",b,sum1,"average")
