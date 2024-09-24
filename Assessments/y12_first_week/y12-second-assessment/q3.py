matrix = [[1,2,3],[4,5,6],[7,8,9]]
array = []
for i in range(len(matrix)):
    total = 0
    for j in range(len(matrix[i])):
        total = total + int(matrix[i][j])
    array.append(total)
    #end for loop
#end for loop
print(array)