nums = []
Rnums = []
total = 0
for i in range(6):
    nums.append(int(input("Enter 6 numbers: ")))
Rnums.append(str(nums[5]) + ", " + str(nums[4]) + ", " + str(nums[3]) + ", " + str(nums[2]) + ", " + str(nums[1]) + ", " + str(nums[0]))
print(Rnums)

for i in range(len(nums)):
    total = total + nums[i]
print(total)

for i in range(len(nums)):
    avg = total / 6
print(avg)