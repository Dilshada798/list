# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# i=0
# num=mainStr.split()
# while i<len(num):
#     if "over" in num:
#         num.remove("over")
#     i=i+1
# print(num)




mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
num=mainStr.split()
subStr = "over"
replacementStr = "on" 
i=0
# j=[]
while i<len(num):
    if "over"in num:
        num.remove("over")
        if "on"not in num:
            num.insert(5,"on")
    i=i+1
print(num)
    
        
    