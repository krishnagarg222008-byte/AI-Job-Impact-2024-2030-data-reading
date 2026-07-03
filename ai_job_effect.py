import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#loading dataset
data=pd.read_csv("ai_job_trends_dataset.csv")

#Data cleaning
print(data.head())
print(data.shape)

print(data.isnull().sum())
print(data.duplicated().sum())

#According to output no null value nor any duplicated one

#no.of unique jobs and their names in which ai is effecting:
# number_of_unique_jobs=data['Industry'].nunique()
# unique_jobs=np.unique(data['Industry'])
# print("number of unique jobs are:",number_of_unique_jobs,"and their names are:-\n",unique_jobs)
#output:-['Education', 'Entertainment', 'Finance' ,'Healthcare' ,'IT' ,'Manufacturing','Retail','Transportation']-total 8

#top 5 industries in which Job status is increasing after AI:-
industries=data[data['Job Status']=='Increasing']['Industry'].head(10)
print(industries)

