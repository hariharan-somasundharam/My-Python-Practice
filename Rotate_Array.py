def rotateArr(arr, d):
        d=d%len(arr)
        arr[:] = arr[d:] + arr[:d]
        return arr

n=int(input("Enter the Array Size:"))
arr=[]
print("Enter the Array Elements:")

for i in range(n):
        arr.append(int(input()))

d=int(input("Enter the Rotation Limit:"))
rotateArr(arr,d)
print("After Rotation :",arr)


# Enter the Array Size:5
# Enter the Array Elements:
# 1
# 2
# 3
# 4
# 5
# Enter the Rotation Limit:2
# After Rotation : [3, 4, 5, 1, 2]