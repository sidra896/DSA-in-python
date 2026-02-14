# # Linear serach 
# #Idea: Array ka har element check karna jab tak target mil na jaye.
# #Time Complexity: O(n)
# def search_linear(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#     return -1
# n=int(input("how many values in Array="))
# arr=[]
# for i in range(n):
#     val=int(input(f"Enter the value {i+1} ="))
#     arr.append(val)
# val2=int(input("Enter the value to search:"))
# result=search_linear(arr,val2)
# if result!=-1:
#     print(f"Element {val2} is found at {result}")
# else:
#     print(f"Element {val2} is not found")


## Binary search
# def search_binary(arr,target):
#     low=0
#     high=len(arr)-1

#     while low<=high:
#         mid=(low+high)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1

#     return -1
# n=int(input("How many values in Array?"))
# arr=[]
# for i in range(n):
#     val=int(input(f"Enter the value {i+1} ="))
#     arr.append(val)
# arr.sort()
# print("The sorted Array:")
# val2=int(input("Enter the value you want to search:"))
# result=search_binary(arr,val2)
# if result!=-1:
#     print(f"Element {val2} is found at the index {result}")
# else:
#     print(f"Element {val2} is not found")


# #Bubble Sort
# def bubbleSort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-1-i):# J->0,j->n-1-0(i)
#            if arr[j]>arr[j+1]:# compare kar rahe hai hum
#               arr[j],arr[j+1]=arr[j+1],arr[j]#Swap ka code a,b=b,a 
# #Input
# n=int(input("How many values in array?"))
# arr=[]
# for i in range(n):
#     val=int(input(f"Enter the value {i+1} ="))
#     arr.append(val)
# print("The Original array:",arr)

# #Function call
# bubbleSort(arr)   
# print("The Sorted array:",arr)


##Selection Sort
# def selectSort(arr):
#     n=len(arr)
#     for i in range(n):
#         min=i
#         for j in range(i,n-1):#(i,n)bi likh sakhte hain
#             if arr[min]>arr[j]:
#                 min=j
#         arr[i],arr[min]=arr[min],arr[i]


# n=int(input("How many values in array?"))
# arr=[]
# for i in range(n):
#     val=int(input(f"Enter the value {i+1} ="))
#     arr.append(val)

# print("The Original array:",arr)

# #Function call
# selectSort(arr)
# print("The sorted array:",arr)




# #Selection Sort
# def insertionSort(arr):
#     n=len(arr)
#     for i in range(1,n):
#         key=arr[i]
#         j=i-1
#         while j>=0 and key<arr[j]:
#             arr[j+1]=arr[j]
#             j=j-1
#         arr[j+1]=key
    


# #Input
# n=int(input("How many values in array?"))
# arr=[]
# for i in range(n):
#     val=int(input(f"Enter the value {i+1} ="))
#     arr.append(val)

# print("The Original array:",arr)

# #Function call
# insertionSort(arr)
# print("The sorted array:",arr)

# #Quick Sort
# def quickSort(arr,left,right):
#     if(left<right):
#         p=partition(arr,left,right)
#         quickSort(arr,left,p-1)
#         quickSort(arr,p+1,right)
# def partition(arr,left,right):
#     pivot=arr[left]
#     i=left+1
#     j=right

#     while True:
#         while(i<=j and arr[i]<=pivot):
#             i=i+1
#         while(i<=j and arr[j]>pivot):
#             j=j-1
#         if(i<j):
#             arr[i],arr[j]=arr[j],arr[i]
#         else:
#             break
#     arr[left],arr[j]=arr[j],arr[left]
#     return j

# #Input
# n=int(input("How many values in array?"))
# arr=[]
# for i in range(n):
#     val=int(input(f"Enter the value {i+1} ="))
#     arr.append(val)

# print("The Original array:",arr)

# #Function call
# quickSort(arr,0,len(arr)-1)
# print("The sorted array:",arr)



# #Selection Sort
# def mergeSort(arr):
#     if len(arr)<=1:
#      return arr
    
#     mid=len(arr)//2
#     left=mergeSort(arr[:mid])
#     right=mergeSort(arr[mid:])

#     return sorted(left+right)



# n=int(input("How many values in array?"))
# arr=[]
# for i in range(n):
#     val=int(input(f"Enter the value {i+1} ="))
#     arr.append(val)

# print("The Original array:",arr)

# #Function call
# arr=mergeSort(arr)
# print("The sorted array:",arr)




# 🔹 Interactive Sorting & Searching Menu

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    arr.sort()  # Binary search requires sorted array
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def quick_sort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quick_sort(arr, left, p-1)
        quick_sort(arr, p+1, right)

def partition(arr, left, right):
    pivot = arr[left]
    i = left + 1
    j = right
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[left], arr[j] = arr[j], arr[left]
    return j

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return sorted(left + right)


# 🔹 Main Program
n = int(input("How many values in the array? "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter value {i+1} = ")))

print("\nOriginal Array:", arr)

print("\nChoose an option:")
print("1 - Linear Search")
print("2 - Binary Search")
print("3 - Bubble Sort")
print("4 - Selection Sort")
print("5 - Insertion Sort")
print("6 - Quick Sort")
print("7 - Merge Sort")

choice = int(input("Enter your choice: "))

if choice == 1:
    target = int(input("Enter value to search: "))
    idx = linear_search(arr, target)
    if idx != -1:
        print(f"Element {target} found at index {idx}")
    else:
        print(f"Element {target} not found")
elif choice == 2:
    target = int(input("Enter value to search: "))
    idx = binary_search(arr, target)
    if idx != -1:
        print(f"Element {target} found at index {idx} (array sorted first)")
    else:
        print(f"Element {target} not found")
elif choice == 3:
    bubble_sort(arr)
    print("Sorted Array:", arr)
elif choice == 4:
    selection_sort(arr)
    print("Sorted Array:", arr)
elif choice == 5:
    insertion_sort(arr)
    print("Sorted Array:", arr)
elif choice == 6:
    quick_sort(arr, 0, len(arr)-1)
    print("Sorted Array:", arr)
elif choice == 7:
    arr = merge_sort(arr)
    print("Sorted Array:", arr)
else:
    print("Invalid choice!")
