def findSmallest(arr):
        result = 1
        
        for i in arr:
            if i > result:
                break
            result += i
        
        return result

arr = []
n=int(input("Enter the Array Size : "))

for i in range (n):
     arr.append(int(input()))
print("Array : ",arr)
print("Result = ",findSmallest(arr))

# Enter the Array Size : 6
# 3
# 6
# 9
# 10
# 20
# 28
# Array :  [3, 6, 9, 10, 20, 28]
# Result =  1