# Stack
class Stack:
    def __init__(self):
        self.list=[]

    
    def push(self,value):
        self.list.append(value)

    
    def pop(self):
        if len(self.list)==0:
            print("The stack is empty")
            return
        else:
            remove=self.list.pop()

        
    def peek(self):
        if len(self.list)==0:
            print("The list is empty, nothing to peek out")
        else:
            print(f"Top element is {self.list[-1]}")

    def display(self):
        print("The Current stack:",self.list)


obj=Stack()
n=int(input("How many elements do you want to add initially in the stack?"))
for i in range(n):
    val=input(f"Enter element {i+1} =")
    obj.push(val)

obj.display()

while True:
    print("options push|pop|peek|exit")
    choice=input("Enter your option:").lower()
    if choice=="push":
        val2=input("Enter the element:")
        obj.push(val2)
        obj.display()

    elif choice=="pop":
        obj.pop()
        obj.display()

    elif choice =="exit":
        print("The final stack:",obj.list)
        break

    elif choice=="peek":
        obj.peek()
        obj.display()
    else:
        print("Invalid choice.please choice valid option")

