elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
c=0
d=0
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
        c=sum/len(a)
    else:
        b.append(k)
        sum1=sum1+k
        d=sum1/len(b)
    i=i+1
print("even average:",c)
print("odd average:",d)
