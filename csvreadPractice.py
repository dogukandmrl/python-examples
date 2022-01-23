import csv
import pandas as pd
import numpy as np

with open('NBA_season1718_salary.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       print(row[''], row['Player'], row['Tm'], row['season17_18'])
#---------------------------------------------------------------------
print(pd.read_csv("NBA_season1718_salary.csv",nrows=10))
#---------------------------------------------------------------------
print(len(pd.read_csv('NBA_season1718_salary.csv')))
#---------------------------------------------------------------------
maas= []
with open('NBA_season1718_salary.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        maas.append(float(row["season17_18"]))
print("Ortalama maas:",sum(maas)/len(maas))
#---------------------------------------------------------------------
df = pd.read_csv ('NBA_season1718_salary.csv')
print("MAX:",df['season17_18'].max())
#---------------------------------------------------------------------
print("MAX:",df['Player'].max())
