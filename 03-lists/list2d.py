
data = [
    ["John", 4, 12, 56, 34], 
    ["Ann", 7, 23, 44, 55],
    ["Mike", 3, 78, 98, 67],
    ["Peter", 5, 12, 46, 87]
]



for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=' ')
    print()