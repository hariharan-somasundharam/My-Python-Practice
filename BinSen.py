def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1  


arr = []
n = int(input("Enter the Range:"))
for i in range (n):
    arr.append(int(input("")))
target = int(input("Enter the Search Element:"))
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
