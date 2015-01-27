from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir = "c:/Users/Dennis Bartlett/Desktop/PubPol590/"
txt_file = "Assignments/File1_small.txt"

df = pd.read_table(main_dir + txt_file, sep = " ")

rowslice = df[60:100]
colslice = df[df.kwh > 30]
