matrix = [[3,5,1],[9,2,8],[4,7,6]]
array = []
for i in range(len(matrix)):
    largestNum = matrix[i][0]
    for j in range(len(matrix[i])):
        if matrix[i][j] > largestNum:
            largestNum = matrix[i][j]
        #end if
    array.append(largestNum)
    #end for loop
#end for loop
print(array)