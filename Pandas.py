import pandas as pd
roll_no=[]
name=[]
DM=[]
OOPs=[]
DS=[]
FDS=[]
avg=[]
result=[]
n=int(input("Enter the No.of students:"))
for i in range (n):
    r=int(input("Enter the Roll.No:"))
    roll_no.append(r)
    nm=str(input("Enter the Student's name:"))
    name.append(nm)
    mt=int(input("Enter the DM mark:"))
    DM.append(mt)
    java=int(input("Enter the OOPs mark:"))
    OOPs.append(java)
    ds=int(input("Enter the DS mark:"))
    DS.append(ds)
    fds=int(input("Enter the FDS mark:"))
    FDS.append(fds)
    average=(mt+java+ds+fds)/4
    avg.append(average)
    if(mt<50 or java<50 or ds<50 or fds<50):
        result.append("FAIL")
    else:
        result.append("PASS")
data={"Roll_No":roll_no,"Maths":DM,"OOPs":OOPs,"DataStruct":DS,"DataSci":FDS,"Average":avg,"FinalResult":result}
df=pd.DataFrame(data,index=name)
print("   ")
print(df)
