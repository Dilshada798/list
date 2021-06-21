# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
# i=0
# count=0
# while i< len(numbers):
    
#     print(numbers)
#     i=i+1


# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 


# s=0
# for i in numbers:
#     s+=1
# print(s)


# # q.no2
# numbers=[50, 40, 23, 22,70, 56, 12, 5, 10, 7] 
# i=0
# count=0
# while i<len(numbers):
#     a=numbers[i]
#     if a>20 and a<40:
#         count=count+1
#     i=i+1
# print(count)

# qno.3
numbers = [50, 40, 23, 70, 56, 12,90, 5, 10, 7] 
i=0
max=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
print(max)



# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 
# i=1
# b=[]
# while i<=len(places):
#     b.append(places[-i])
#     i=i+1
# print(b) 




# a=[1,2,3,4,5,6,7]   
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum/7)



# # palidrome number
# a=input("enter the name")
# # a=[ 'n', 'i', 't', 'i', 'a' ] 
# b=[]
# length=len(a)
# print(length)
# i=1
# while i<=len(a):
#     b.append(a[-i])
#     i=i+1
# # print(a)
# print(b)
# if a==b:
#     print("this is a palindrome ")
# else:
#     print("not palindrome")


# odd even

# a=[]
# b=[]
# c=[]
# size=int(input("enter the size of list:"))
# i=0
# sum=0
# sum1=0
# while size>i:
#     # num=int(input("enter the number:"))
#     # a.append(size)
#     if size%2==0:
#         b.append(size)
#         sum=sum+size
#     else:
#        c.append(size)
#        sum1=sum1+size
    
#     i=i+1
# print(b,"even number")
# print(c,"odd number")
# print("sum of even number",sum)
# print("sum of odd number",sum1)




# a=[1, 0, 0, 1, 1, 0, 1, 1] 
# i=1
# sum=0
# while i<len(a):
#     sum=sum+2*i-0**a[-i]
#     i=i+1
# print(sum)








# num=[44,23,12,3,6,18,45,66,23,54,55,10,9,31]
# a=[]
# b=[]
# i=0
# sum=0
# sum1=0
# while i<len(num):
#     k=num[i]
#     if k%2==0:
#         a.append(k)
#         sum=sum+k
#     else:
#         b.append(k)
#         sum1=sum1+k
#     i=i+1
# print("sum of even",a,sum)
# print("odd number",b,sum1)

my_list=[]
i=1
while i <=10:
    my_list.append(i)
    i=i+1
print(my_list)




st=[1, 1, 2, 3, 4, 4, 5, 1]
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
                    













