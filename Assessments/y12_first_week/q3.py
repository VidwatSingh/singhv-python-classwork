msm = int(input("how many minutes scince midnight: "))
h = int(msm/60)
m = msm - (h*60)
if h <= 9 and m >= 10:
    print("0" + str(h) + ":" + str(m))
elif h <= 9 and m == 0:
    print("0" + str(h) + ":" + "00")
elif h <= 9 and m < 10:
    print("0" + str(h) + ":" + "0" + str(m))
elif h > 9 and m >= 10:
    print(str(h) + ":" + str(m))
elif h > 9 and m == 0:
    print(str(h) + ":" + "00")
else:
    print(str(h) + ":" + "0" + str(m))