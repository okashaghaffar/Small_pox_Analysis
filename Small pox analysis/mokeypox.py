# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 06:06:22 2022

@author: PC
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

smallpox_in_world=pd.read_csv("infection of small pox in whole world.csv")
print(smallpox_in_world.head())
rows,columns=smallpox_in_world.shape
#(r,c)
print("Total Rows :",rows,"\nTotal Colums: ",columns)
Total_Values=np.product(smallpox_in_world.shape)
#total cells 
print("Total Values in this dataset are : ",Total_Values)
print("THE NAMES OF COLUMNS ARE : \n",smallpox_in_world.columns)
missing_values=smallpox_in_world.isnull().sum
print(missing_values())
missing_values=missing_values().sum()
missing_percent=(missing_values/Total_Values)*100
print("missing values are ",missing_percent,"%")

print("Total missing values are : ",missing_values)
print("Rows with null data")
#print(smallpox_in_world.loc[smallpox_in_world["Code"].isnull()])
print("Since country code is not that important so we can either discard this coulumn or fill it")
smallpox_in_world.fillna(0,inplace=True)
print(smallpox_in_world)
print("Now all the missing values are filled with 0")
#print(smallpox_in_world.loc[smallpox_in_world["Code"].isnull()])
#calculating empty percentage
#print(smallpox_in_world.columns)






#print(smallpox_in_world.groupby("Year")["Reported Smallpox cases (WHO)"].sum())
#sns.barplot(x=smallpox_in_world["Year"], y=smallpox_in_world.groupby("Year")["Reported Smallpox cases (WHO)"].sum())
#sns.barplot(data=smallpox_in_world,x="Year",y="Reported Smallpox cases (WHO)")

#print(world)
plt.title("Total Recorded cases of small pox year wise")
Total_Cases=(pd.DataFrame({"Total Cases":smallpox_in_world.groupby('Year')['Reported Smallpox cases (WHO)'].sum()}).reset_index())
sns.barplot(x=Total_Cases['Year'], y=Total_Cases['Total Cases'])

plt.show()

    
