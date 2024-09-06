
complete = False
total = 0
count = 0
while complete == False:
    n = int(input("Enter a number greater than -1: "))
    if n >= 0:
        total += n
        count += 1
    else:
        complete == True
print("average is: ", total/count)