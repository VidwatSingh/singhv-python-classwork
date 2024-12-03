class myStringStack:
    def __init__(self, size) -> None:
        self.sp = 1
        self.max = size
        self.data = ["" for _ in range(size)]
    #end constructor

    def pop(self) -> None: #not returning anything, so it is a procedure
        temp = self.data[self.sp]
        if not self.isEmpty():
            self.sp -= 1
        else:
            print("stack is empty")
            return ""
        #end if
        return temp
            
    #end public procedure

    def push(self, item) -> None:
        if not self.isFull():
            self.sp += 1
            self.data[self.sp] = item
        else:
            print("stack is full")
    #end public procedure

    def isFull(self) -> bool: #returns a boolean value
        return self.sp + 1 == self.max
    #end public procedure
    
    def isEmpty(self) -> bool:
        return self.sp == -1
    #end public procedure

    def peek(self) -> str: #returns a string value
        if not self.isEmpty():
            return self.data[self.sp]
        else:
            print("Stack is empty")
            return ""
    #end public procedure
    def __repr__(self) -> str:
        return ":".join(self.data)
#end class

my_stack = myStringStack(3)

my_stack.push(input("enter what you want to input: "))
print(my_stack)
my_stack.push(input("enter what you want to input: "))
print(my_stack)
my_stack.push(input("enter what you want to input: "))
print(my_stack)

my_stack.pop()

print(my_stack)