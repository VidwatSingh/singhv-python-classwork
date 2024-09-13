total = 0
count = 0
TF = False
while TF == False:
    n = int(input("enter a number, not -1, unless you want to stop and take the average: "))
    if n >=0:
        TF = False
        total += n
        count += 1
    else:
        TF = True
print("The average is: ", total/count)