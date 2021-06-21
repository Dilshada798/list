# num=int(input("enter the number"))
# sum=0
# i=1
# while i<num:
#     if num%i==0:
#         sum=sum+i
#     i=i+1    
# if num==sum:
#     print(num,"perfect number",i)    
# else:
#     print(num,"not a perfect nummber",i) 
# a="dilshada"
# a+=" pooja"
# print(a)
# # a=5
# while a<10:
#     j=1
#     while j<a:
#         print(a)
#         j=j+1
#     a=a+1
# print(a)

from typing import NewType


char_list=[1, 1, 2, 3, 4, 4, 5, 1]
i=0
newList=[]
while i<len(char_list):
    b=1
    count=0
    a=[]
    while b<len(char_list):
        if char_list[i]==char_list[b]:
            count=count+1
        b=b+1
    a.append(count)
    a.append(char_list[i])
    if a not in newList:
        newList.append(a)
    i=i+1
print(newList)
 