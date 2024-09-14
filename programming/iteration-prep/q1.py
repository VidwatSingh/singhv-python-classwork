largestLetter = "a"
smallestLetter = "z"
for i in range(5):
    letter = str(input("enter a letter: "))
    if letter < smallestLetter:
        smallestLetter = letter
    elif letter > largestLetter and letter > smallestLetter:
        largestLetter = letter
#end for loop
print(largestLetter)
print(smallestLetter)