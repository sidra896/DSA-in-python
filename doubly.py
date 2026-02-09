#Class of node 
class Node:
    def __init__(self,value):   
        self.data=value
        self.prev=None
        self.next=None

#Class Linklist
class doubly:
    def __init__(self):
       self.head=None

    def insert(self,value):
        temp=Node(value)
        if self.head is None:
            self.head=temp
            return
        t1=self.head
        while t1.next is not None:
            t1=t1.next
        t1.next=temp
        temp.prev=t1

    def display_forward(self):
        t1=self.head
        print("Forward",end=" ")
        while t1 is not None:
            print(t1.data,end="<->")
            t1=t1.next
        print("None")


    def display_backword(self):
        t1=self.head
        while t1.next is not None:
            t1=t1.next

        print("Backword",end=" ")
        while t1 is not None:
            print(t1.data,end="<->")
            t1=t1.prev
        print("None")




obj=doubly()
n=int(input("How many values you want to enter in double link list"))
for i in range(n):
    val=input(f"Enter the value {i+1} =")
    obj.insert(val)

obj.display_forward()
obj.display_backword()
