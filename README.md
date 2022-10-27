## cleanmydata

This library contains all the essential functions for data cleaning.

It takes a list of data cleaning parameters and either a string or pandas dataframe as input

Functions:
1) Remove new lines
2) Remove emails
3) Remove URLs 
4) Remove hashtags (#hashtag)
5) Remove the string if it contains only numbers
6) Remove mentions (@user)
7) Remove retweets (RT...)
8) Remove text between the square brackets [ ]
9) Remove multiple whitespaces and replace with one whitespace 
10) Remove multiple occurrences

Coming soon...
<br>(Must be a dataframe and provide a column name)
11) Drop NA values
12) Remove stopwords (creates new columns with stopword count, stopwords, count without stopwords)
13) Count characters (creates a new column)
14) Count words (creates a new column)
15) Calculate average word length (creates a new column)


## How to install?
<code>pip install cleanmydata</code>


## Usage
1) Import the library
   <br><code>from cleanmydata.functions import clean_data</code>
2) Call the method clean_data, and pass the data and the number indicating the cleaning operations as a list.
   <br>E.g., to remove emails and hashtags from the data, 
   <br>
   <code>
   mydata = "Hello folks. abc@example.com #hashtag"
   <br>print(mydata)
   <br>mydata = dc.clean_data([2, 4], mydata)
   <br>print(mydata)
   </code>