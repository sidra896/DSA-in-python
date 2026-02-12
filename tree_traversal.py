# TREE TRAVERSAL 
class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

#PreOrder(root first ,left,right)
def preOrder(root): 
    if root!=None:
        print(root.data,end=" ")
        preOrder(root.left) 
        preOrder(root.right)  

#InOrder(left first,root,right)
def inOrder(root): 
    if root!=None:
        inOrder(root.left) 
        print(root.data,end=" ")
        inOrder(root.right)  

#PostOrder(left,right,root)
def postOrder(root): 
    if root!=None:
        postOrder(root.left) 
        postOrder(root.right)
        print(root.data,end=" ")



obj=Node("A")
obj.left=Node("B")
obj.left.left=Node("D")
obj.left.right=Node("E")
obj.left.right.right=Node("H")
obj.right=Node("C")
obj.right.left=Node("F")
obj.right.left.left=Node("I")
obj.right.right=Node("G")
obj.right.right.left=Node("j")
print("\n PreOrder:",end="")
preOrder(obj)   # Jis variable (name) ko class assign ki gayi hai, usi ko function mein pass karte hain
print("\n InOrder:",end="")
inOrder(obj) 
print("\n PostOrder:",end="")
postOrder(obj) 


print()
# In OOP Style
# TREE TRAVERSAL IN PREORDER (root node first,left node,right node)
class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

    def preOrder(self): 
        print(self.data,end=" ")
        if self.left:
         self.left.preOrder()
        if self.right:
            self.right.preOrder()  

    def inOrder(self): 
        if self.left:
            self.left.inOrder()
        print(self.data,end=" ")
        if self.right:
            self.right.inOrder()
         
    def postOrder(self): 
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.data,end=" ")
    


obj=Node("A")
obj.left=Node("B")
obj.left.left=Node("D")
obj.left.right=Node("E")
obj.left.right.right=Node("H")
obj.right=Node("C")
obj.right.left=Node("F")
obj.right.left.left=Node("I")
obj.right.right=Node("G")
obj.right.right.left=Node("j")
print("\n PreOrder:",end="")
obj.preOrder()  
print("\n InOrder:",end="")
obj.inOrder()
print("\n PostOrder:",end="")
obj.postOrder()



