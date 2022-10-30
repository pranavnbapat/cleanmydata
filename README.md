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
10) Replace characters with more than two occurrences and replace with one occurrence
11) Remove emojis
12) Count characters (only for dataframe; creates a new column)
13) Count words (only for dataframe; creates a new column)
14) Calculate average word length (only for dataframe; creates a new column)
15) Count stopwords (only for dataframe; creates two new columns, stowords and stopword_count)
16) Detect language (uses <a href="https://pypi.org/project/fasttext-langdetect/">fasttext-langdetect</a>) (only for dataframe; creates two new columns, lang and lang_prob)
17) Detect language (uses <a href="https://pypi.org/project/fasttext-langdetect/">fasttext-langdetect</a>) (only for dataframe; creates just one column with langauge and probability; takes less time)
18) 


## How to install?
<code>pip install cleanmydata</code>


## Parameters
<ol>
   <li>lst (list) - List of data cleaning operations</li>
   <li>data (string or dataframe) - Data to be passed</li>
   <li>column (string) - Dataframe column on which operation to perform; only for dataframe</li>
   <li>save (boolean) - If you want to save the results in a new file</li>
   <li>name (string) - Name of the new file if save is True</li>
</ol>

## Usage
1) Import the library
   <br><code>from cleanmydata.functions import clean_data</code>
2) Call the method clean_data, and pass the parameters as you wish.
3) By default, if the dataframe is passed, it drops all NA values (dropna)

## Examples
1) To remove emails and hashtags<br>
   <code>mydata = "Hello folks. abc@example.com #hashtag"</code>
   <br>
   <code>mydata = clean_data(lst=[2, 4], data=mydata)</code>
   <br>
   <code>print(mydata)</code>
2) To count stopwords, remove mentions, and URLs, and save file from a dataframe<br>
   <code>df = pd.read_csv('data/my_csv.csv', encoding='ISO-8859-1', dtype='unicode')</code>
   <br>
   <code>df = clean_data(lst=[15, 6, 2], data=df, column='comments', save=True, name='my custome file name')</code>


## Other notes
If using stopwords, make sure you have en_core_web_sm installed. <br>
<code>python -m spacy download en_core_web_sm</code>


### More options and enhancements coming soon...