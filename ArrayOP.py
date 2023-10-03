import numpy as np
h=list(map(int,input("Enter the Elements:").split()))
print("Choice\n1.Insert\n2.Delete\n3.Sort\n4.Search\n5.Exit")
ch=int(input("Enter Your Choice:"))
while(ch!=5):
    if(ch==1):
        val=int(input("Enter the Element:"))
        idx=int(input("Enter the Index:"))
        h=np.insert(h,idx,val)
        print("Array After Insertion:",h)
    elif(ch==2):
        idx_1=int(input("Enter the  Index:"))
        print("Deleted Element:",h[idx_1])
        h=np.delete(h,idx_1)
        print("Array After Deletion:",h)
    elif(ch==3):
        h=np.sort(h)
        print("Sorted Array:",h)
    elif(ch==4):
        val_1=int(input("Enter the Search Element:"))
        m=np.where(h==val_1)
        print(m)
    else:
        print("OOPs!\nEntered Invalid Choice!!")
    ch=int(input("Enter Your Choice:"))
        
