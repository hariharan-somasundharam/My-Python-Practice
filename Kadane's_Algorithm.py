def maxSubArraySum(arr):
        maxi = arr[0]
        cur = 0
        
        for i in arr:
            if cur < 0:
                cur = 0
            cur +=i
            maxi = max(maxi,cur)
        
        return maxi

arr = []
n = int(input("Enter the Array Size :"))
print("Enter the Array Elements :")

for i in range(n):
     arr.append(int(input()))

print("Maximum Sum of Sub Array : ",maxSubArraySum(arr))

# Enter the Array Size :5
# Enter the Array Elements :
# 1
# 2
# 3
# -2
# 5
# Maximum Sum of Sub Array :  9