import pandas as pd                 # Importing Pandas package
        # Reading a Data Set File
h=pd.read_csv("iris.csv")
print("\n Top rows\n",h.head())     # Printing The Top rows of Data Set File
m=int(input("How many samples do you need?:"))      #Getting Sample Input From User
print(h.sample(m))
print("\n Coloumn one\n",h.columns,"\n Order of the sheet:",h.shape)
        #Slicing The Data Set Values
on=int(input("Enter the start value to slice:"))
to=int(input("Enter the stop value:"))
print("Sliced data set:\n",h[on:to])
        # Displaying Specific Row
r=int(input("Enter the row to be displayed:"))
print(h.iloc[r])
        # Displaying Specific Column
c=input("Enter the column to be displayed:")
print(h[[c]])
        # Counting The Values Of Specific Column
c_count=input("Enter the column name to count the values:")
print(h[c_count].value_counts())
        # Obtaining Mean,Median,Sum,Maximum And Minimum Values Of The Specific Column
d=input("Enter the column name to find Mean,Median,Minimum,Maximum and Sum:")
print("Mean:",h[d].mean(),"\nMedian:",h[d].median(),"\nSum:",h[d].sum(),"\nMinimum:",h[d].min(),"\nMaximum:",h[d].max())
        # Renaming A Specific Column
g=input("Enter the column name to be replaced:")
f=input("Enter the new name:")
p={g:f}
h.rename(columns=p,inplace=True)
print("The final Dataset is:\n",h)
