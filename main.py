import pandas as pd
import numpy as np
df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
#head() functions displays first 5 rows of the dataframe by default.
print(df.head())
#info() function displays the complete informtion about the dataframe: total number of columns,name-data type of each column, memory usage
print(df.info())
#shape displays the number of rows and columns in the dataframe
print(df.shape)
#columns prints the names of the columns
print(df.columns)
#to change the daya type of any column astype is used
df['Daily Steps'] = df['Daily Steps'].astype("int64")
#The describe method shows basic statistical characteristics of each numerical feature (int64 and float64 types): 
#number of non-missing values, mean, standard deviation, range, median, 0.25 and 0.75 quartiles.
print(df.describe())
#to include statistics of non-numerical features, we need to include the data types in the descrive function
print(df.describe(include=['object','bool']))
#value_counts function shows the total in each value of the feature for type object and type boolean
print(df['Occupation'].value_counts())
#to show as the fracion use normalize()
print(df['Gender'].value_counts(normalize=True))
print(df.sort_values(by="Occupation",ascending=True).head())
#sorting dataframe by multiple columns
print(df.sort_values(by=["Occupation","BMI Category"],ascending=[True,False]).head())
print(df[df["Occupation"] == "Accountant"]['Heart Rate'].mean())
print(df[(df['Occupation'] == "Teacher") & (df["Gender"] == "Female")]["Blood Pressure"])
# Mean of the male users sleep time
print(round(df[df['Gender'] == 'Male']['Sleep Duration'].mean(),2))
# Mean of the Female users sleep time
print(round(df[df['Gender'] == 'Female']['Sleep Duration'].mean(),2))
#Maximum Daily steps for Doctors who have BMI category - normal
print(df[(df['Occupation'] == 'Doctor') & (df['BMI Category'] == 'Normal')]['Daily Steps'].max())
#locating rows with the index 0 to 5 (both inclusive) and columns labeled as Gender till Sleep Duration
print(df.loc[0:5,"Gender":"Sleep Duration"])
#Using iloc to access using numbers, 5 & 3 is no included
print(df.iloc[0:5,0:3]) 
#to get the first line of the data
print(df[:1])
#to get the last line of the data
print(df[-1:])
#use of lambda function with apply
print(df[df['Occupation'].apply(lambda val:val[0] == 'S')].head(10))
#The map method can be used to replace values in a column by passing a dictionary 
#of the form {old_value: new_value} as its argument
d = {"Male" : "M", "Female" : "F"}
df["Gender"] = df["Gender"].map(d)
print(df.head())
#using groupby for gender sleep duration
print(df.groupby(["Gender"])["Sleep Duration"].agg([np.mean,np.max,np.min]))
