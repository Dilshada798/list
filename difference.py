a = [1,2,3,4,5,6]
b= [2,3,1,0,6,7] 
c=[]
i=0
while i<len(a):
    k=a[i]
    if k not in b:
        c.append(k)
    i=i+1
print(c)



# a=[[[2,3,5]]]
# a[0][0][1]=1
# print(a)











# a=[[1,[2,3,5]]]
# # a[0][0][1]=1
# # print(a)
# a[0][0]=7
# print(a)