
#attempt = int(input("enter 1 or 2: "))
#def getPword(attempt):
#    one = False
#    if attempt == 1:
#        password = input("enter password: ")
#        if len(password) > 6 and len(password) < 8:
#            one = True
#    while one == True:
#        password2 = input("re-enter password: ")
#        if len(password2) == len(password):
#            print("change was succsessful")
#        else:
#            print("Error - passwords don't match")
#
#
#z = getPword(attempt)
#print(z)


#n = int(input("enter a number between 1 and 3: "))
#names = []

#def addName(names):
#    appendNames = input("enter a name: ")
#    appeneded_Names = names.append(appendNames)
#    return appeneded_Names

#def display_menu(n):
#    if n == 1:
#        addedNames = addName(names)
#        return addedNames
#    elif n == 2:
#        z = addName(names)
#        print(z)
#    elif n == 3:
#        print("proram terminating")
#    else:
#        print("enter a number bwteen 1 and 3")



#choice = display_menu(n)
#print(choice)












#arrayNames = ["john", "james", "dylan", "Stacy", "Abagail"]
#names = arrayNames.append(input("enter a pupils name: "))
#findNames = str(input("enter the pupils name you want to find: "))
#found = False
#for i in range(len(arrayNames)):
#    if arrayNames[i] == findNames:
#        found = True
#    else:
#        found = False
#end for loop
#if found == True:
#    print("name found at index: ", i)
#else:
#    print("name not found")













#outletSales1 = [10,12,15,10]
#outletSales2 = [5,8,3,6]
#outletSales3 = [10,12,15,10]
#total1 = 0
#total2 = 0
#total3 = 0
#for i in range(len(outletSales1)):
#    total1 = total1 + outletSales1[i]
#print("total for quater 1: ", total1)
##end for loop
#for j in range(len(outletSales2)):
#    total2 = total2 + outletSales2[j]
#print("total for quater 2: ", total2)
##end for loop
#for z in range(len(outletSales3)):
#    total3 = total3 + outletSales3[z]
#print("total for quater 3: ", total3)
##end for loop
















#ROWS = 6
#COLUMNS = 4
#
#grid = [["x" for _ in range(COLUMNS)] for _ in range(ROWS)]
#
#char_row = 0
#char_col = 0
#
#def display_grid(grid, char_row, char_col):
#    print("Grid:")
#    for row in range(ROWS):
#        for col in range(COLUMNS):
#            if row == char_row and col == char_col:
#                print("O", end=" ")
#            else:
#                print(grid[row][col], end=" ")
#        print()
#
#display_grid(grid, char_row, char_col)
#
#while True:
#    new_row = int(input("Enter row (1-6): "))
#    new_col = int(input("Enter column (1-4): "))
#    if new_row < 1 or new_row > ROWS or new_col < 1 or new_col > COLUMNS:
#        print("Invalid input. Please enter valid row and column values.")
#        continue
#    char_row = new_row - 1  
#    char_col = new_col - 1
#    display_grid(grid, char_row, char_col)













def populate_empty_park():
    for i in range(10):
        park_row = []
        for j in range(6):
            park_row.append("empty")
        park.append(park_row)

def enter_grid_reference():
    row = False
    column = False

    while row == False:
        grid_ref_row = input("enter the row number where it has been parked: ")
        try:
            grid_ref_row = int(grid_ref_row)
            row = True
            if grid_ref_row < 1 or grid_ref_row > 10:
                row = False
                print("you must enter a number between 1 and 10.")
        except:
            print("you must enter a number.")

    
    while column == False:
        grid_ref_col = input("enter the column number where it has been parked: ")
        try:
            grid_ref_col = int(grid_ref_col)
            row = True
            if grid_ref_col < 1 or grid_ref_col > 6:
                column = False
                print("you must enter a number between 1 and 6.")
        except:
            print("you must enter a number.")

    grid_ref_row -= 1
    grid_ref_col -= 1

    #if park[grid_ref_row][grid_ref_col] == "empty"
    # continue





park = []
populate_empty_park()

while True:
    registration = input("enter the registration number: ")
    enter_grid_reference(registration)