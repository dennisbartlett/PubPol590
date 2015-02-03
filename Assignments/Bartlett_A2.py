from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir = "c:/Users/Dennis Bartlett/Desktop/PubPol590/"
csv_file = "Data/small_data_w_missing_duplicated.csv"

## LOADING FILE AS-IS
df = pd.read_csv(main_dir + csv_file)

## LOADING FILE, BUT REPLACE STRING CHARACTES WITH "NaN"
missing = ["-", "NA", ".", ""]
df = pd.read_csv(main_dir + csv_file, na_values = missing)

## DROPS REPEATED ROWS AFTER 1st INSTANCE, WORKING TOP TO BOTTOM
df1 = df.drop_duplicates()

## ISOLATES ROWS WHERE CONSUMP IS "NaN"
rows = df1['consump'].isnull()
df1[rows]

## CHECK FOR DUPLICATED VALUES UNDER 'PANID' AND 'DATE'

rows1 = df1.duplicated(['panid','date'])
df1[rows1]

## DROP DUPLICATES THAT HAVE NO VALUE FOR 'CONSUMP' (all from df1[rows1])
df2 = df1.drop_duplicates(['panid','date'])

## FIND THE OVERALL MEAN OF REMAINING VALUES OF 'CONSUMP' 
df2.consump.mean()

## VALUE IS 0.91743963893521185