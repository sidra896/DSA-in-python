class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None

class Doubly:
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


    def deleteEnd(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is None:
            self.head=None
            return
        t1=self.head
        while t1.next is not None:
            t1=t1.next
        t1.prev.next=None


    def deleteBegin(self):
        if self.head is None:
            print("The list is empty")
            return
        self.head=self.head.next
        if self.head is not None:
            self.head.prev=None

    def deleteMiddle(self):
        if self.head is None:
            print("The list is empty")
            return
        slow=self.head
        fast=self.head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next 
            fast=fast.next.next
        if prev is None:
            self.head=self.head.next
            if self.head:
             self.head.prev=None
        else:
            prev.next=slow.next
            if slow.next:
                slow.next.prev=prev

    def display_forward(self):
        t1=self.head
        print("Forward",end=" ")
        while t1 is not None:
            print(t1.data,end="<->")
            t1=t1.next
        print("None")

    def display_backward(self):
        t1=self.head
        while t1.next is not None:
            t1=t1.next

        print("Backward",end=" ")
        while t1 is not None:
            print(t1.data,end="<->")
            t1=t1.prev
        print("None")




obj=Doubly()
n=int(input("How many values you want to enter in double link list?"))
for i in range(n):
    val=input(f"Enter the value {i+1} =")
    obj.insert(val)
print("Choose your operation")
print("1.Delete the value at the End")
print("2.Delete the value at the Begin")
print("3.Delete the value at the Middle")
op=input("Enter the operation(1,2,3):")
if op=='1':
 obj.deleteEnd()
elif op=='2':
    obj.deleteBegin()
elif op=='3':
    obj.deleteMiddle()




print("\nDoubly Linked List:")
obj.display_forward()
obj.display_backward()