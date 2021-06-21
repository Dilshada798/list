number = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# i=0
# # a=[]
# while i<len(number):
#     j=0
#     while j<len(number):
#         if number[i]==number[j]:
#             del(number[i])
#         j=j+1
#     i=i+1
# print(number)


i=0
j=[]
while i<len(number):
    k=number[i]
    if k not in j:
        j.append(k)
    i=i+1
print(j)
