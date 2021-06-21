char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
i=0
k=[]
while i<len(char_list):
    b=0
    count=0
    a=[]
    while b<len(char_list):
        if char_list[i]==char_list[b]:
            count=count+1
        b=b+1
    a.append(char_list[i])
    a.append(count)
    if a not in k:
        k.append(a)
    i=i+1
print(k)
