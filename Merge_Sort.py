def Merge_Sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        Merge_Sort(left_arr)
        Merge_Sort(right_arr)
        i=0
        j=0
        k=0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1


arr=[]
n=int(input("Enter the Array Size:"))
print("Enter the Array Elements:")
for i in range (n):
    arr.append(int(input()))
print("Before Sorting :",arr)

Merge_Sort(arr)

print("After Sorting :",arr)
