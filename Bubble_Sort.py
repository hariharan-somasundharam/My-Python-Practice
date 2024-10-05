def bubbleSort(arr, n):
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
            
        if not swapped:
            break
        
    return arr

arr=[]
n=int(input("Enter the Array Size:"))
print("Enter the Array Elements:")
for i in range (n):
    arr.append(int(input()))
print("Before Sorting :",arr)
print("After Sorting :",bubbleSort(arr,n))
