def rowWithMax1s(arr):
    j = len(arr[0])-1
    maxRow =-1
    for i,row in enumerate(arr):
        while j >=0 and row[j] ==1:
            maxRow = i
            j-= 1
        
    return maxRow


n = int(input("Enter the Size of Matrix : "))
arr = []
print("Enter the Elements in Ascending Order (0's and 1's) :")
for i in range (n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    arr.append(a)

print("Matrix : ",arr)
print("Row with Index ",rowWithMax1s(arr)," has Max 1's.")


# Matrix :  [[0, 0], [1, 1]]
# Row with Index  1  has Max 1's.