class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next

class linklist:
    def __init__(self,head=None):
        self.head=head

    def insert(self,value):
        temp=Node(value)
        if self.head is None:
            self.head=temp
            return
        t1=self.head
        while t1.next is not None:
            t1=t1.next
        t1.next=temp

    def insertEnd(self,value):
        self.insert(value)

    def insertBegin(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp

    def insertMiddle(self,value):
        if self.head is None:
            self.head=Node(value)
            return
        slow=self.head
        fast=self.head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next

        temp=Node(value)
        prev.next=temp
        temp.next=slow

    def display(self):
        t1=self.head
        while t1 is not None:
            print(t1.data,end="->")
            t1=t1.next
        print(None)


obj=linklist()
n=int(input("How many values youu want to enter in linklist?"))
for i in range(n):
    val=input(f"Enter the values {i+1} =")
    obj.insert(val)


print("choose any opaeration")
print("1.insert the value at end")
print("2.insert the value at begin")
print("3.insert the value at mid or at specfic location")
op=input("Enter the operation(1,2,3)=")
if op in ['1','2','3']:
 newValue=int(input("Enter the value you want to insert:"))
if op=='1':
 obj.insertEnd(newValue)
elif op=='2':
    obj.insertBegin(newValue)
elif op=='3':
    obj.insertMiddle(newValue)
print("The linklist:")
obj.display()