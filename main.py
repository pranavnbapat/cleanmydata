from cleanmydata.functions import *

df = pd.read_csv('data/training.1600000.processed.noemoticon.csv', encoding='ISO-8859-1', dtype='unicode')
print(df.head(10))
df = clean_data(lst=[14, 15], data=df, column='comment', save=False, name='my custome name')
print(df.head(10))
print(df.columns)
print(df.shape)

# my_data = "Pranav #Bapat pranav.g33k@gmail.com Hello"
# my_data = clean_data(lst=[2, 4, 9], data=my_data)
# print(my_data)
