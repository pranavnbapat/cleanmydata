import pandas as pd

from cleanmydata.functions import *

# df = pd.read_csv('data/training.1600000.processed.noemoticon.csv', encoding='ISO-8859-1', dtype='unicode')
# print(df.head(10))
# print(df.columns)
# print(df.shape)
# df = clean_data(lst={2, 99}, data=df, column='comment', save=False, name='my custome name')
# print(df.head(10))
# print(df.columns)
# print(df.shape)


my_data = "pranav.g33k@gmail.com Pranav #Hello Bapat"
print(my_data)
my_data = clean_data(lst={1, 2}, data=my_data, column='comment')
print(my_data)
