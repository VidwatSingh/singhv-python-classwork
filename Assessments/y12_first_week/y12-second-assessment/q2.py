percentage = int(input("enter your percentage: "))
if percentage >= 90:
    print("A")
elif percentage < 90 and percentage >= 80:
    print("B")
elif percentage < 80 and percentage >= 70:
    print("C")
elif percentage < 70 and percentage >= 60:
    print("D")
else:
    print("F")
#end if