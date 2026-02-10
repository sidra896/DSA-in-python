class Priority:
    def __init__(self):
        self.queue=[]  # ak list bana loo 


    def isEmpty(self):
        return len(self.queue)==0
    
    def enqueue(self,prio,data):
        self.queue.append((prio,data))
        self.queue.sort()
        print(f"{data} is inserted with priority {prio}")


    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty")

        else:
            item=self.queue.pop(0)
            print(f"{item[1]} with priority {item[0]} is removed ")


    def peek(self):
        if self.isEmpty():
            print("The Queue is empty")
        else:
            print(f"The front element is {self.queue[0][1]} with priority {self.queue[0][0]}")

    def display(self):
        print("The current queue is :",self.queue)


obj=Priority()
n=int(input("How many you want to insert initaially?"))
for i in range(n):
    val=input(f"Enter the value {i+1} =")
    pr=int(input(f"Enter priority for {val}:"))
    obj.enqueue(pr,val)
obj.display()   
while True:
 print("choose your operation")
 print("1.Add the element in queue")
 print("2.delete the element in queue")
 print("3.show the front element")
 print("4.Exit from the program")
 op=input("Enter the operation(1,2,3,4):")
 if op=='1':
    val2=input("Enter a value =")
    pr2=int(input(f"Enter priority for {val2}:"))
    obj.enqueue(pr2,val2)
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