# # # #Array in DSA
# # # import array

# # # def insert_end(ds, val):
# # #     ds.append(val)

# # # def insert_begin(ds, val):
# # #     ds.insert(0, val)

# # # def insert_mid(ds, val):
# # #     ds.insert(len(ds)//2, val)

# # # def delete_value(ds, val):
# # #     if val in ds:
# # #         ds.remove(val)

# # # def delete_end(ds):
# # #     if ds:
# # #         ds.pop()

# # # def delete_begin(ds):
# # #     if ds:
# # #         ds.pop(0)

# # # def delete_mid(ds):
# # #     if ds:
# # #         ds.pop(len(ds)//2)


# # # # ---- Step 1: Data Type ----
# # # print("1 = Numbers")
# # # print("2 = Names")

# # # mode = input("Enter mode (1/2): ")

# # # if mode == '1':
# # #     dtype = input("Enter type (i for int, f for float): ")
# # #     ds = array.array(dtype)
# # #     n = int(input("How many values? "))
# # #     for i in range(n):
# # #         v = float(input(f"Value {i+1}: ")) if dtype=='f' else int(input(f"Value {i+1}: "))
# # #         ds.append(v)

# # # elif mode == '2':
# # #     ds = []
# # #     n = int(input("How many names? "))
# # #     for i in range(n):
# # #         ds.append(input(f"Name {i+1}: "))

# # # else:
# # #     print("Wrong choice")
# # #     exit()

# # # # ---- Step 2: Operation (only once) ----
# # # print("\nChoose ONE operation:")
# # # print("1 Insert End")
# # # print("2 Insert Beginning")
# # # print("3 Insert Middle")
# # # print("4 Delete Value")
# # # print("5 Delete End")
# # # print("6 Delete Beginning")
# # # print("7 Delete Middle")

# # # op = input("Enter operation: ")

# # # if op == '1':
# # #     v = input("Enter value to insert: ")
# # #     v = float(v) if isinstance(ds, array.array) and ds.typecode=='f' else int(v) if isinstance(ds, array.array) else v
# # #     insert_end(ds, v)

# # # elif op == '2':
# # #     v = input("Enter value to insert: ")
# # #     v = float(v) if isinstance(ds, array.array) and ds.typecode=='f' else int(v) if isinstance(ds, array.array) else v
# # #     insert_begin(ds, v)

# # # elif op == '3':
# # #     v = input("Enter value to insert: ")
# # #     v = float(v) if isinstance(ds, array.array) and ds.typecode=='f' else int(v) if isinstance(ds, array.array) else v
# # #     insert_mid(ds, v)

# # # elif op == '4':
# # #     v = input("Enter value to delete: ")
# # #     v = float(v) if isinstance(ds, array.array) and ds.typecode=='f' else int(v) if isinstance(ds, array.array) else v
# # #     delete_value(ds, v)

# # # elif op == '5':
# # #     delete_end(ds)

# # # elif op == '6':
# # #     delete_begin(ds)

# # # elif op == '7':
# # #     delete_mid(ds)

# # # else:
# # #     print("Invalid operation")

# # # print("\nFinal Result:", ds)



# # import array
# # #All the function of insert and delete 
# # def insert_end(arr,val):
# #     arr.append(val)

# # def insert_begin(arr,val):
# #    arr.insert(0,val)

# # def insert_mid(arr,val):
# #    arr.insert(len(arr)//2,val)

# # def delete_value(arr,val):
# #    if val in arr:
# #       arr.remove(val)
# #    else:
# #     print(f"Value {val} not found in array/list!")

# # def delete_end(arr):
# #    if arr:
# #       arr.pop()

# # def delete_begin(arr):
# #    if arr:
# #       arr.pop(0)

# # def delete_mid(arr):
# #    if arr:
# #       arr.pop(len(arr)//2,)
   
# # #Datatype and values in array
# # print("Choose the type of the value you want to enter:")
# # print("1.integer")
# # print("2.float")
# # print("3.text / name")
# # choice=input("Enter the choice (1,2,3)=")
# # n=int(input("How many value you want to enter?"))


# # if choice=='1':
# #     arr=array.array('i')
# #     for i in range(n):
# #      val = int(input(f"Enter integer value {i+1}= "))
# #      arr.append(val)
# #     print("Integer Array",arr)

# # elif choice=='2':
# #     arr=array.array('f')
# #     for i in range(n):
# #      val = float(input(f"Enter float value {i+1}="))
# #      arr.append(val)
# #     print("Float Array",arr)

# # elif choice=='3':
# #     arr=[]
# #     for i in range(n):
# #      val = input(f"Enter name/text {i+1}= ")
# #      arr.append(val)
# #     print("Name list",arr)

# # else:
# #     print("Invalid choice")
# #     exit()

# # #Insert yeh delete karna hai
# # print("What do you want to do")
# # print("1.Insert a value")
# # print("2.Delete a value")
# # op_choice=input("Enter choice(1,2)=")
# # if op_choice=='1':
# #  if choice=='1':
# #    new_value=int(input("Enter a value to insert:"))
# #  elif choice=='2':
# #    new_value=float(input("Enter a value to insert:"))
# #  else:
# #    new_value=input("Enter a value to insert:")
# # elif op_choice=='2':
# #   if choice=='1':
# #    new_value=int(input("Enter a value to delete:"))
# #   elif choice=='2':
# #    new_value=float(input("Enter a value to delete:"))
# #   else:
# #    new_value=input("Enter a value to delete:")



# # print("1.insert at end")
# # print("2.insert at begin")
# # print("3.insert at middle")
# # print("4.delete the value")
# # print("5.Delete at end")
# # print("6.delete at begin ")
# # print("7.delete at mid")
# # pos_choice=input("enter the choice (1,2,3,4,5,6)")

# # if pos_choice=='1':
# #  insert_end(arr,new_value)
# #  print("\nThe array after the insertion is= ",arr)
# # elif pos_choice=='2':
# #    insert_begin(arr,new_value)
# #    print("the array after insertion is:",arr)
# # elif pos_choice=='3':
# #    insert_mid(arr,new_value)
# #    print("The array after the insertion is",arr)
# # elif pos_choice=='4':
# #    delete_value(arr,val)
# #    print("the array after deletion",arr)
# # elif pos_choice=='5':
# #    delete_end(arr)
# #    print("the array after deletion",arr)
# # elif pos_choice=='5':
# #    delete_begin(arr)
# #    print("the array after deletion",arr)
# # elif pos_choice=='6':
# #    delete_mid(arr)
# #    print("the array after deletion",arr) 



# # Simple 2D Array with type selection

# # Functions for row operations
# def insert_row_end(arr, row):
#     arr.append(row)

# def insert_row_begin(arr, row):
#     arr.insert(0, row)

# def insert_row_mid(arr, row):
#     arr.insert(len(arr)//2, row)

# def delete_row(arr, index):
#     if 0 <= index < len(arr):
#         arr.pop(index)
#     else:
#         print(f"Row index {index} not valid!")

# # ---- User chooses type ----
# print("Choose the type of 2D array:")
# print("1. Integer")
# print("2. Float")
# print("3. Text/String")
# choice = input("Enter choice (1-3): ")

# # ---- Input rows and columns ----
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# arr2D = []

# for i in range(rows):
#     row = []
#     print(f"Enter values for row {i+1}:")
#     for j in range(cols):
#         val = input(f"Value at column {j+1}: ")
#         if choice == '1':
#             val = int(val)
#         elif choice == '2':
#             val = float(val)
#         # else string, no conversion
#         row.append(val)
#     arr2D.append(row)

# print("\n2D Array:")
# for r in arr2D:
#     print(r)

# # ---- Choose operation ----
# print("\nChoose operation:")
# print("1.Insert row at end")
# print("2.Insert row at begin")
# print("3.Insert row at middle")
# print("4.Delete a row by index")
# op = input("Enter operation (1-4): ")

# if op in ['1','2','3']:
#     new_row = []
#     print("Enter values for new row:")
#     for j in range(cols):
#         val = input(f"Value at column {j+1}: ")
#         if choice == '1':
#             val = int(val)
#         elif choice == '2':
#             val = float(val)
#         new_row.append(val)
#     if op=='1':
#         insert_row_end(arr2D, new_row)
#     elif op=='2':
#         insert_row_begin(arr2D, new_row)
#     elif op=='3':
#         insert_row_mid(arr2D, new_row)
# elif op=='4':
#     idx = int(input("Enter row index to delete (0-based): "))
#     delete_row(arr2D, idx)
# else:
#     print("Invalid operation!")

# # ---- Print final 2D array ----
# print("\n2D Array after operation:")
# for r in arr2D:
#     print(r)

# import array
# arr=array.array('i')
# n=int(input("How many values you want to enter in array:"))
# for i in range(n):
#     val=int(input(f"Enter integer value {i+1}="))
#     arr.append(val)
# print("The integer array",arr)


# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# matrix = []

# print("Enter the elements row wise:")

# for i in range(rows):
#     row = []
#     for j in range(cols):
#         val = int(input(f"Enter element [{i}][{j}]: "))
#         row.append(val)
#     matrix.append(row)

# print("\nYour 2D Array (Matrix):")
# for row in matrix:
#     print(row)



def insert_end(matrix,row_num,val):
    matrix[row_num].append(val)

def insert_begin(matrix,row_num,val):
    matrix[row_num].insert(0,val)

def insert_mid(matrix,row_num,val):
    matrix[row_num].insert(len(matrix[row_num])//2,val)

def delete_value(matrix,row_num,val):
    if val in matrix[row_num]:
        matrix[row_num].remove(val)
    else:
        print("value not found")

def delete_end(matrix,row_num):
    if matrix[row_num]:
        matrix[row_num].pop()

def delete_begin(matrix,row_num):
    if matrix[row_num]:
        matrix[row_num].pop(0)

def delete_mid(matrix,row_num):
    if matrix[row_num]:
        matrix[row_num].pop(len(matrix[row_num])//2)

def display_matrix(matrix):
    print("current 2D Array")
    for row in matrix:
        print(row)


row=int(input("Enter the number of rows"))
column=int(input("Enter teh number of columns"))
matrix=[]
print("enter the value one by one")
for i in range(row):
    row=[]
    for j in range(column):
        val=int(input(f"enter the value for row {i},column {j}="))
        row.append(val)
    matrix.append(row)
display_matrix(matrix)

while True:
    print("Choose an operation")
    print("1.insert at end")
    print("2.Insert at begin")
    print("3.Insert at mid")
    print("4.Delete the value")
    print("5.Delete at end")
    print("6.delete at begin")
    print("7.Delete at mid")
    print("8.Display array")
    print("9.Exist program")
    op=input("Enter the operation(1-9)")
    if op=='9':
     print("Existing program")
     break
    

    if op in ['1','2','3','4','5','6','7']:
     sel_num= int(input(f"Enter row number : "))
    
    if op in ['1','2','3','4']:
        new_value = int(input("Enter value: "))

    if op == '1':
      insert_end(matrix, sel_num, new_value)
    elif op == '2':
      insert_begin(matrix, sel_num, new_value)
    elif op == '3':
      insert_mid(matrix, sel_num, new_value)
    elif op == '4':
       delete_value(matrix, sel_num, new_value)
    elif op == '5':
       delete_end(matrix, sel_num)
    elif op == '6':
      delete_begin(matrix, sel_num)
    elif op == '7':
       delete_mid(matrix, sel_num)
    elif op == '8':
      display_matrix(matrix)
    else:
      print("Invalid option! Please try again.")
    
display_matrix(matrix)