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

     def delete(self,value):
          t1=self.head
          prev=t1
          if t1.data==value:
               self.head=t1.next
          while t1.next is not None:
               if t1.data == value:
                    prev.next=t1.next
                    break
               else:
                    prev=t1
                    t1=t1.next

          if t1.data ==value:
               prev.next=None
          
            
     def display(self):
          t1=self.head
          while t1 is not None:
               print(t1.data,end="->")
               t1=t1.next
          print("None")


obj=linklist()
n=int(input("How many values you want to enter in linklist?"))
for i in range(n):
     val=input(f"Enter the values {i+1} =")
     obj.insert(val)
newvalue=input("Enter the value you want to delete:")
if newvalue==n:
   obj.delete(newvalue)
   print("The linklist:")
   obj.display()
else:
     print("Invalid value")
