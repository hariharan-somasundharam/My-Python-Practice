import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([[1,2,3,4,5],[6,7,8,9,0]])
c=np.array([[1,2,3],[4,5,6],[7,8,9]])

        #Determining Dimension Of Numpy Arrays

print("Dimension of a:",a.ndim)
print("Dimension of b:",b.ndim)
print("Dimension of c:",c.ndim)

        #Determining DataType Of Numpy Arrays

print("DataType of a:",a.dtype)
print("DataType of b:",b.dtype)
print("DataType of c:",c.dtype)

        #Determining Rows&Coloumns Of Numpy Arrays

print("Shape of a:",a.shape)
print("Shape of b:",b.shape)
print("Shape of c:",c.shape)

        #Slicing Of Numpy Arrays

print("Slicing of a:",a[1:4])   # obj_name[strt.idx:end.idx]
print("Slicing of b:",b[1,1:4:2])     # obj_name[row.idx,strt.idx:end.idx]
print("Slicing of c:",c[2,0:2])     #obj_name[row.idx,strt.idx:end.idx]

        #Copying Numpy Arrays

d=c.copy()
print("Copied Array d:",d)

        #Viewing Numpy Arrays
e=b.view()
print("Viewing Array b:",e)

        #Changing Numpy Array's DataType

f=np.array([1.1,2.2,3.3,4.4,5.5,6.6])
print("Changed DataType of f:",f.astype('i'),f.dtype)

        #Reshaping Numpy Arrays

print("Reshaped Array f(2,3):",f.reshape(2,3))
print("Reshaped Array f(3,2):",f.reshape(3,2))

        #Iterating Numpy Arrays

print("Iterated Array a:")
for x in np.nditer(a):
    print(x)
        #Concatenating Numpy Arrays
    
g=np.array([11,12,13,14,15])
print("Concatenation of a&g:",np.concatenate((a,g)))
