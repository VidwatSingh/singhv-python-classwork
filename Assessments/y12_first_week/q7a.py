array = [[0,1,2],[3,5,10],[6,7,8]]
largest_num = array[0][0]
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] > largest_num:
            largest_num = array[i][j]
print("the largest number is: ",largest_num)