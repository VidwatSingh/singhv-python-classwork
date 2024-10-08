def multiply(x:int,y:int) -> str:
    product = x*y
    return product
#end function

#main program

e = int(input("enter first number: "))
r = int(input("enter second number: "))
ans = multiply(e,r)
print(str(ans) + " is the answer")