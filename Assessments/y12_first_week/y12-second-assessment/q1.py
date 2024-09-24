n = int(input("enter integer: "))
total = 0
for i in range(n + 1):
    if (i % 2) == 0:
        total = total + i
    #end if
#end for loop
print(total)