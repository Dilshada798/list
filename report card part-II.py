marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
i=0
sum=0
count=0
while i<len(marks):
    num=marks[i]
    a=num[0]+num[1]+num[2]+num[3]+num[4]
    b=num[0]+num[1]+num[2]+num[3]+num[4]
    c=num[0]+num[1]+num[2]+num[3]+num[4]
    count=count+1
    sum=sum+a
    k=a/len(marks[i])
    l=b/len(marks[i])
    m=c/len(marks[i])
    n=sum/len(marks[i])
    i+=1
print(k) 
print(l)
print(m)
print(n)   
print("total marks:",sum,"count:",count)
                     