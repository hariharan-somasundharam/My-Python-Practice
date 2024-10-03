def Quick_Sort(start, end, arr):
    if(start < end):
        pos=Partition(start, end, arr)
        Quick_Sort(start, pos-1, arr)
        Quick_Sort(pos+1, end, arr)


def Partition(start, end , arr):
    i=start
    j=end-1
    pivot=arr[end]

    while i<j:
        while i < end and arr[i] < pivot:
            i+=1
        while j > start and arr[j]>= pivot:
            j-=1
        
        if i < j:
            Swap(i, j, arr)

    if arr[i] > pivot:
        Swap(i, end, arr)
    
    return i


def Swap(a, b, arr):
    if a!=b:
        temp = arr[a]
        arr[a]=arr[b]
        arr[b]=temp
arr=[]
n=int(input("Enter the Array Size:"))
print("Enter the Elements:")
for i in range (n):
    arr.append(int(input()))
print("Before Sorting :",arr)
Quick_Sort(0,len(arr)-1, arr)
print("After Sorting: ",arr)
