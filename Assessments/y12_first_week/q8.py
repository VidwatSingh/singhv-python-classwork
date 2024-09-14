s = str(input("enter your phrase: "))
nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
output = ""
for char in s:
    if char in digits:
        output += nums[int(char)]
    else:
        output += char
print("string with number replaced by their respective digits: ")
print(output)