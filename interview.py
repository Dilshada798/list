# fruits=["papaya","orange","apple","papaya","apple","orange","grape fruit"]
# b=[]
# i=0
# while i<len(fruits):
#         j=0
#         count=0
#         k=[]
#         while j<len(fruits):
#                 if fruits[i]==fruits[j]:
#                     count=count+1
#            j=j+1
#         k.append(fruits[i])
#         k.append(count)
#         if k not in b:
#                 b.append(k)
#         i=i+1
# print(b)

        








# a=["srushti","dilshada","priyanka"]
# for  i in a:
#     count=0
#     for j in i:
#         count=count+1
#     if count%2==0:
#         print(i,"even","count:",count)
#     else:
#         print(i,"odd","count:",count)





# name=["snowball","chewy","bubbles","gruff"]
# animals=["cat","dog","fish","goat"]
# age=[1,2,3,4]
# i=0
# c=[]
# b = " "
# while i<len(name):
#     k=(name[0]+b+"the"+b+animals[0]+b+"is"+b+str(age[0]))
#     n=(name[1]+b+"the"+b+animals[1]+b+"is"+b+str(age[1]))
#     l=(name[2]+b+"the"+b+animals[2]+b+"is"+b+str(age[2]))
#     r=(name[3]+b+"the"+b+animals[3]+b+"is"+b+str(age[3]))
     
#     i=i+1
# print(k)
# print(n)
# print(l)
# print(r)

# a="my name is swati"
# b=a.split(" ")
# i=0
# while i<len(b):
#     print(b[i][0].upper(),end="")
#     j=1
#     while j<len(b[i]):
#         k=b[i][j]
#         print(k,end="")
#         j+=1
#     print()
#     i+=1

# a="ankita pisal"
# s=""
# b=[]
# for i in a:
#     if i==" ":
#         b.append(s)
#         # s=" "
#     else:
#         s+=i
# if s:
#     b.append(s)
# print(b)

# num=int(input("enter the no."))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num=num//10
# print("rev num=",rev//10*10)

a=[ 10,20,33,45,56]
max=a[0]
min=a[0]
i=0
while i<len(a):
    if max<a[i]:
        max=a[i]
    if min>a[i]:
        min=a[i]
    i=i+1
print(max)
print(min)


   
  