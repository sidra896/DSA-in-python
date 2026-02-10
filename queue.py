class Queue:
    def __init__(self):
        self.queue=[]


    def isEmpty(self):
        return len(self.queue)==0
    

    def enqueue(self,data):
        self.queue.append(data)


    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            remove=self.queue.pop(0)
            print(f"The {remove} is pop out")
        

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("The front element is",self.queue[0])
        

    def display(self):
        print("The current Queue is:",self.queue)
        


obj=Queue()
n=int(input("How many you want to insert initaially?"))
for i in range(n):
    val=input(f"Enter the value {i+1} =")
    obj.enqueue(val)
obj.display()   
while True:
 print("choose your operation")
 print("1.Add the element in queue")
 print("2.delete the element in queue")
 print("3.show the front element")
 print("4.Exit from the program")
 op=input("Enter the operation(1,2,3):")
 if op=='1':
    val2=input("Enter a value =")
    obj.enqueue(val2)
    obj.display()
    
 elif op=='2':
    obj.dequeue()
    obj.display()
  
 elif op=='3':
    obj.peek()
    obj.display()

 elif op=='4':
     print("the final queue:",obj.queue)
     break
 else:
     print("Invalid choice ,please enter a valid choice")   

   

