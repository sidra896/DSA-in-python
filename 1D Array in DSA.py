import array

def insert_end(arr,val):
    arr.append(val)
def insert_begin(arr,val):
    arr.insert(0,val)
def insert_mid(arr,val):
    arr.insert(len(arr)//2,val)

def delete_value(arr,val):
    if val in arr:
        arr.remove(val)
    else:
        print(f"the enter {val} is not fount array\list")
def delete_end(arr):
    if arr:
     arr.pop()
def delete_begin(arr):
    if arr:
        arr.pop(0)
def delete_mid(arr):
    if arr:
        arr.pop(len(arr)//2)


print("Enter the type of values you want to enter")
print("1.integer")
print("2.float")
print("3.Name/text")
choice=input("Enter the choice(1,2,3)=")
n=int(input("How many valuese you want to enter?"))
if choice=='1':
    arr=array.array('i')
    for i in range(n):
        val=int(input(f"enter integer value {i+1}="))
        arr.append(val)
    print("The integer array",arr)

elif choice=='2':
    arr=array.array('f')
    for i in range(n):
        val=float(input(f"enter the float value {i+1}="))
        arr.append(val)
    print("The Float array",arr)
elif choice=='3':
    arr=[]
    for i in range(n):
        val=input(f"enter the name {i+1}=")
        arr.append(val)
    print("The name list",arr)
else:
    print("Invalid choice")
    exit()
print("Choice your operation")
print("1.Insert at end")
print("2.insert at begin")
print("3.Insert at mid")
print("4.Delete the value")
print("5.Delete at end")
print("6.delete at begin")
print("7.Delete at mid")
op=input("Enter the operation(1,2,3,4,5,6,7)=")
if op in ['1','2','3',]:
 if choice=='1':
    new_value=int(input("enter the integer value to insert:"))

 elif choice=='2':
    new_value=float(input("enter the float value to insert:"))
 else:
    new_value=input("enter the  name to insert:")
elif op=='4':
    if choice=='1':
     new_value=int(input("enter the integer value to delete:"))

    elif choice=='2':
     new_value=float(input("enter the float value to delete:"))
    else:
     new_value=input("enter the  name to delete:")


if op=='1':
  insert_end(arr,new_value)
  print("The array after the insertion",arr)
elif op=='2':
  insert_begin(arr,new_value)
  print("The array after the insertion",arr)
elif op=='3':
  insert_mid(arr,new_value)
  print("The array after insertion",arr)
elif op=='4':
  delete_value(arr,new_value)
  print("The array after deletion",arr)
elif op=='5':
  delete_end(arr)
  print("The array after deletion",arr)
elif op=='6':
  delete_begin(arr)
  print("The array after deletion",arr)
elif op=='7':
  delete_mid(arr)
  print("The array after the deletion",arr)



