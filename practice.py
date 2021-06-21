# a=[1,2,3,4,5,6,7,8,9]
# num=int(input("enter the no."))
# j=[]
# i=-1
# while i<len(a):
#     j.append([a])
#     if a[i]==num:
#         break
#     i=i-1
# print(j)



# list1=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# i=0
# num=int(input("enter the no."))
# while i<len(list1):
#    if num>=i:
#         b.append(list1[-i])
#    else:
#        b.append(list1[i])
#        i=i+1
# print(b)


# def a(name):
#      k=""
#      i=1
     
#      while i<=len(name):
#           k=k+name[-i]
#           i=i+1
#      print(k)
# a("dilshada aijaz")




# a=[1,2,3,[4,5],6,7,[8,9],1,2,3,[4,5]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==type(a):
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j+=1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)

# # list1=[10,20,30,40]
# list2


# 1.Write a Python program to create a list reflecting the modified run-length encoding from 
# a given list of integers or a given list of characters. 
# Original list:
# list1=[1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String:
# aabcddddadnss
# List reflecting the modified run-length encoding from the said string:
#[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]
lst=[1, 1, 2, 3, 4, 4, 5, 1]
i=0
while i<len(list1):
     count=0
     j=0
     a=[]
     while j<len(list1):
          if list1[i]==list1[j]:
               count=count+1
               j=j+1
     a.append(count)
     a.append(list1[i])
     i=i+1
print(list1)
                    

