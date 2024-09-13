h = int(input("enter hours: "))
m = int(input("enter minutes: "))
apm = str(input("is it am or pm: "))
if apm == "am":
    m = m + (h * 60)
    print(m)
else:
    m = m + (h * 60)
    print(m + 720)