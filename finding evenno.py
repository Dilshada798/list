a=[1,2,13,15,7,4,6,19]
b=[]
i=0
while i<len(a):
    k=a[i]
    if k%2==0:
        b.append(k)
    i=i+1
print(b)
