import csv
import pandas

filepath = "D:\\Work\\NetApp OneDrive\\OneDrive - NetApp Inc\\294915 - ARCH-Identify the unused objects in the system\\BCO.csv"

df = pandas.read_csv(filepath)
#print(df[['Name']])
for line in df['Name']:
    txt = line.replace(".bco"," ")
    print(txt)