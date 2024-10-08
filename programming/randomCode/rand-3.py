school = ["AAAA","BBBB","CCCC","DDDD"]
medal = [4,7,1,3]

school_num = 0

AAAA = False
BBBB = False
CCCC = False
DDDD = False

a = False
b = False
c = False
d = False

for i in range(len(school)):
    name_school = input("enter the name of your school: (enter -1 for the 5th attempt to end): ")
    if name_school == "AAAA":
        medal[0] = input("enter the number of medals for your school: ")
        school_num = 1
        AAAA = True
        a = True
    elif name_school == "BBBB":
        medal[1] = input("enter the number of medals for your school: ")
        school_num = 2
        BBBB = True
        b = True
    elif name_school == "CCCC":
        medal[2] = input("enter the number of medals for your school: ")
        school_num = 3
        CCCC = True
        c = True
    elif name_school == "DDDD":
        medal[3] = input("enter the number of medals for your school: ")
        school_num = 4
        DDDD = True
        d = True
    elif name_school == "-1":
        print("School number: ", school_num)
        if a == True and AAAA == True:
            print("School name: AAAA")
            print("Number of medals", medal[0])
        elif b == True and BBBB == True:
            print("School name: BBBB")
            print("Number of medals", medal[0])
        elif b == True and CCCC == True:
            print("School name: CCCC")
            print("Number of medals", medal[0])
        elif b == True and DDDD == True:
            print("School name: DDDD")
            print("Number of medals", medal[0])
        else:
            print("NO")
    else:
        print("please enter a school")
#end for loop