def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  


my_list=[]
n=int(input("Enter the Range:"))

for i in range (n):
    
    my_list.append(int(input()))
target_element = int(input("Enter the search element:"))

result = linear_search(my_list, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the list")
