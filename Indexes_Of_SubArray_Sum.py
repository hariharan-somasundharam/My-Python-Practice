def subArraySum(arr, n, s): 
        
        if s == 0:
            return [-1] if 0 not in arr else [arr.index(0) + 1, arr.index(0) + 1]
        
        left = 0
        current_sum = 0

        for right in range(n):
            current_sum += arr[right]

            while current_sum > s and left <= right:
                current_sum -= arr[left]
                left += 1

            if current_sum == s:
                return [left + 1, right + 1]

        return [-1]

arr = []
n = int(input("Enter the Array Size : "))
print("Enter the Array Elements :")

for i in range (n):
     arr.append(int(input()))

s = int(input("Enter the Sum : "))
print("Array : ",arr)
print("Position Range : ",subArraySum(arr, n, s))


# Enter the Array Size : 5
# Enter the Array Elements :
# 1
# 2
# 3
# 7
# 5
# Enter the Sum : 12
# Array :  [1, 2, 3, 7, 5]
# Position Range :  [2, 4]