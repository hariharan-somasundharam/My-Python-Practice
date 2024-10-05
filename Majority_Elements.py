# Boyer-Moore Algorithm

def majorityElement(arr):
    res,count = 0,0
        
    for i in arr:
        if count == 0:
            res = i
        count += (1 if i == res else -1)
        
    if arr.count(res) > len(arr) // 2:
        return res
    else:
        return -1


arr = []
n = int(input("Enter the Array Size : "))
print("Enter the Array Elements : ")

for i in range (n):
    arr.append(int(input()))

print("Array : ",arr)
print("Majority Element : ",majorityElement(arr))
