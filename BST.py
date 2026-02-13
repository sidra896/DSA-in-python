class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

def insert(root,value):
        if root ==None:   #Root none tb hoo gya jb tree khali hoo 
            return Node(value)
        if root.data==value:
            return root
        if root.data>value:
            root.left=insert(root.left,value) 
        else:
            root.right=insert(root.right,value)
        return root


def search(root,value):
    if root==None:
        return False
    if root.data==value:
        return True
    if root.data>value:
        return search(root.left,value)
    else:
        return search(root.right,value)
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)


n = int(input("How many values you want to insert: "))

root = None

for i in range(n):
    value = int(input(f"Enter value {i+1} ="))
    
    root=insert(root,value)

print("InOrder Traversal:")
inOrder(root)

val=int(input("\nEnter the value you want to search="))
if search(root,val):
    print("Value found")
else:
    print("Value not found,invalid value to search")


# In OOP style
print("BST IN OOP STYLE")
class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

    def insert(self,value):
        if self.data>value:
           if self.left:
            self.left.insert(value)
           else:
              self.left=Node(value) 
        elif self.data<value:
            if self.right:
              self.right.insert(value)
            else:
               self.right=Node(value)


    def search(self,value):
        if self.data==value:
           return True
        elif self.data>value:
           if self.left:
              return self.left.search(value)
           else:
              return False
        else:
           if self.right:
              return self.right.search(value)
           else:
              return False
           

    def delete(self,value):
        if self.data>value:
            if self.left:
                self.left=self.left.delete(value)
        elif self.data<value:
            if self.right:
                self.right=self.right.delete(value)
        else:
            if not self.right:
                return self.left
            if not self.left:
                return self.right
        return self
    
    def inOrder(self):
        if self.left:
          self.left.inOrder()
        print(self.data,end=" ")
        if self.right:
            self.right.inOrder()
          


rootValue=int(input("Enter the root value="))
obj=Node(rootValue)
n = int(input("How many values you want to insert: "))
for i in range(n):
    value = int(input(f"Enter value {i+1} ="))
    obj.insert(value)

print("InOrder Traversal:")
obj.inOrder()
print("\nWhat you want to do?")
print("1.Insertion in the Tree")
print("2.Deletion in the Tree")
op=input("Choose your operation(1,2)=")
if op=='1':
 val=int(input("\nEnter the value you want to search:"))
 if obj.search(val):
   print(f"Value {val} is present in your tree.")
 else:
   print(f"Value {val} is not present in your tree.")
 print("After Insertion InOrder Traversal:")
 obj.inOrder()
if op=='2':
 val2=int(input("\nEnter the value you want to delete:"))
 if obj.search(val2):
     obj=obj.delete(val2)
     print(f"Value {val2} is deleted in your tree successfully.")
 else:
   print(f"Value {val2} is not present in tree.")

 print("After Deletion InOrder Traversal:")

 obj.inOrder()    

