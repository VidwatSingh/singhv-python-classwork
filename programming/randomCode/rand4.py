def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    #end if
#end function

def fibonacci2(n):
    fibNumbers = [0, 1]  # List of the first two Fibonacci numbers
    # Now append the sum of the two previous numbers to the list
    for i in range(2, n + 1):
        fibNumbers.append(fibNumbers[i - 1] + fibNumbers[i - 2])
    return fibNumbers[n]
    #end for loop
#end function

while True:
    try:
        n = int(input("Enter the place of the fibonnacci number you want to find, between 3 and 30: "))
        if 3 <= n <= 30:
            break
        else:
            print("enter a number between 3 and 30")
    except ValueError:
        print("invalid input, enter a number")
print("Recursive method: ")