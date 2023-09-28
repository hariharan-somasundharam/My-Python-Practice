import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def sig(x):
    return (1/1+np.exp(-x))
doc=pd.read_csv("diabetes.csv")         # Reading Document
print("The top content of the Data Set:\n",doc.head())
x=doc.iloc[:,5].values.reshape(-1,1)
y=doc.iloc[:,8].values.reshape(-1,1)
y_pred=sig(x)
plt.title("Logistic Regression For Diabetes")
plt.scatter(x,y)
plt.xlabel("BMI")
plt.ylabel("Diabetes Coefficient")
sns.regplot(x=x,y=y,data=doc,logistic=True,ci=None,color="blue")
plt.show()
