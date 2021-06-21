numbers = [50, 40, 23, 70, 56, 12,90, 5, 10, 7] 
i=0
max=0
number = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
i=0
k=number[0]
a=[]
while i<len(number):
    num=number[i]
    if num>k:
        k=num
    i=i+1
number.remove(k)
j=0
m=number[0]
s=[]
while j<len(number):
    n=number[j]
    if n>m:
        m=n
    j=j+1
a.append(m)
print(a)