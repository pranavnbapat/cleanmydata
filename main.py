from cleanmydata.functions import *

df = pd.read_csv('data/training.1600000.processed.noemoticon.csv', encoding='ISO-8859-1', dtype='unicode')
df = clean_data(lst={2, 3, 4, 5, 6, 7, 16}, data=df, column='comment')
print(df.head())
print(df.columns)
print(df.shape)

