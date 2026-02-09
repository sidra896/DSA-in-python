# DOUBLY LINKED LIST

class Node:
    def __init__(self, info):
        self.data = info
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        temp = Node(value)

        # Agar list khali ho
        if self.head is None:
            self.head = temp
            return

        t1 = self.head
        while t1.next is not None:
            t1 = t1.next

        t1.next = temp
        temp.prev = t1
    def insertEnd(self,value):
        self.insert(value)

    def insertBegin(self,value):
        temp=Node(value)
        if self.head is not None:
            self.head.prev=temp
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
        temp.prev=prev
        temp.next=slow
        slow.prev=temp

    def display_forward(self):
        t1 = self.head
        print("Forward:", end=" ")
        while t1 is not None:
            print(t1.data, end=" <-> ")
            t1 = t1.next
        print("None")

    def display_backward(self):
        t1 = self.head
        # Last node tak jao
        while t1.next is not None:
            t1 = t1.next

        print("Backward:", end=" ")
        while t1 is not None:
            print(t1.data, end=" <-> ")
            t1 = t1.prev
        print("None")


# Object
obj = DoublyLinkedList()
n = int(input("Enter how many values: "))

for i in range(n):
    val = input(f"Enter value {i+1}: ")
    obj.insert(val)

newvalue=input("Enter the value you want to insert:")
print("Choose our operation")
print("1.Insert at the End")
print("2.Insert at the Begin")
print("3.Insert at the Middle")
op=input("Enter the opaertaion:")
if op=='1':
 obj.insertEnd(newvalue)
elif op=='2':
 obj.insertBegin(newvalue)
elif op=='3':
 obj.insertMiddle(newvalue)
else:
    print("Invalid choice")

print("\nDoubly Linked List:")
obj.display_forward()
obj.display_backward()
