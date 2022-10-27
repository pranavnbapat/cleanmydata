import pandas as pd
import re
from cleanmydata.functions import clean_data

mydata = "Here we    go @Pranav #Bapat ...^\n\n This is the"

print(mydata)

mydata = clean_data([4, 6, 10, 1], mydata)

print(mydata)