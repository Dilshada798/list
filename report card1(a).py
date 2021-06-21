marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
] 
i=0
sum=0
while i<len(marks):
    a=0
    h=0
    sum=0
    while a<len(marks[i]):
        h=h+(marks[i][a])
        a=a+1
    sum=sum+h
    k=sum/len(marks[i])

    i=i+1
    print(sum,k)