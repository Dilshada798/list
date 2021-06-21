# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]

# print type(magic_square)
# print type(magic_square[0])
# print type(magic_square[1])

# print sum(magic_square[0])
# print sum(magic_square[1])
# print sum(magic_square[2]) 

magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
sum=0
while i<len(magic_square):
    column=0
    while column<len(magic_square):
        sum=sum+magic_square[i][column]
        column=column+1
    j=0
    sum1=0
    while j<len(magic_square):
        row=0   
        while row<len(magic_square):
            sum1=sum1+magic_square[i][row]
            row=row+1
        j=j+1
        k=0
        sum2=0
        while k<len(magic_square):
            dignal=0
            while dignal<len(magic_square):
                sum2=sum2+magic_square[i][dignal]
                dignal=dignal+1
            k=k+1
    i=i+1
print(sum)
print(sum1)
print(sum2)
if sum==sum1==sum2:
    print("its magic square")
else:
    print("it's not a magic square")

