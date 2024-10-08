pupil = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
Group_1_array = []
Group_2_array = []

for i in range(len(pupil)):
    if pupil[i] % 2 == 0:
        Group_1_array.append(pupil[i])
    else:
        Group_2_array.append(pupil[i])
#end for loop
print(Group_1_array)
print(Group_2_array)