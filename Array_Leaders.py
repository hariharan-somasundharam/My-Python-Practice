def leaders(n, arr):
        maxi=arr[-1]
        leaders=[]
        
        for i in arr[::-1]:
            maxi=max(maxi,i)
            if i>=maxi:
                leaders.append(i)
                
                
        return leaders[::-1]

n=int(input("Enter the Array Size : "))
arr=[]
print("Enter the Array Elements : ")

for i in range(n):
     arr.append(int(input()))

arr = leaders(n,arr)
print(arr)
