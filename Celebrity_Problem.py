def celebrity(mat,n):

    for i in range(n):
        isCeleb = True
        for j in range (n):
            if mat[i][j]!=0:
                isCeleb = False
                break
        
        if isCeleb:
            for j in range (n):
                if i!=j and mat[j][i]==0:
                    isCeleb = False
        
        if isCeleb:
            return i
    
    return -1
    

n = int(input("Enter the No.of Persons in Party: "))
mat = []
print("Enter Whether they know Others (if Knows 1 otherwise 0) :")
for i in range (n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    mat.append(a)

print("Persons Matrix : ",mat)
if celebrity(mat,n)== -1:
    print("There is No Celebrity in the Party.")
else:
    print("The Celebrity's Index is : ",celebrity(mat,n))


# Persons Matrix :  [[0, 1, 1], 
#                    [0, 0, 0],
#                    [1, 1, 1]]
# The Celebrity's Index is :  1