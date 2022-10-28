import re
import pandas as pd
from pathlib import Path
import time

# For stowords
import spacy
stopwords = spacy.load('en_core_web_sm')
stopwords = stopwords.Defaults.stop_words

import warnings
warnings.filterwarnings("ignore")


def remove_newlines(data, column=None):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"\n", " ", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data
        result[column] = result[column].apply(lambda x: re.sub(r"\\n", " ", str(x)).strip())

    return result


def remove_emails(data, column=None):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"([A-z0-9+._-]+@[A-z0-9+._-]+\.[A-z0-9+_-]+)", "", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data
        result[column] = result[column].apply(lambda x: re.sub(r"([A-z0-9+._-]+@[A-z0-9+._-]+\.[A-z0-9+_-]+)", "",
                                                               str(x)).strip())
        print(type(result))

    return result


def remove_urls(data, column=None):
    result = ''
    if isinstance(data, str):
        result = re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w.,@?^=%&:/~+#-])?',
                        "", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data
        result[column] = result[column].apply(lambda x: re.sub(
            r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w.,@?^=%&:/~+#-])?', '',
            str(x)).strip())

    return result


def remove_hashtags(data, column=None):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"#[A-Za-z0-9_]+", "", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data
        result[column] = result[column].apply(lambda x: re.sub(r"#[A-Za-z0-9_]+", "", str(x)).strip())

    return result


def remove_if_only_number(data, column=None):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"^[0-9]+$", " ", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data
        result[column] = result[column].apply(lambda x: re.sub(r'^[0-9]+$', '', str(x)).strip())

    return result


def remove_mentions(data, column=None):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"@[A-Za-z0-9_]+", " ", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data
        result[column] = result[column].apply(lambda x: re.sub(r"@[A-Za-z0-9_]+", " ", str(x)).strip())

    return result


def remove_retweets(data, column=None):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"\bRT\b", " ", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data
        result[column] = result[column].apply(lambda x: re.sub(r"\bRT\b", " ", str(x)).strip())

    return result


def remove_text_between_square_brackets(data, column=None):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"[\(\[].*?[\)\]]", " ", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data
        result[column] = result[column].apply(lambda x: re.sub(r"[\(\[].*?[\)\]]", '', str(x)).strip())

    return result


def remove_multiple_whitespaces(data, column=None):
    result = ''
    if isinstance(data, str):
        result = re.sub(r" +", " ", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data
        result[column] = result[column].apply(lambda x: re.sub(r" +", " ", str(x)).strip())

    return result


def remove_multiple_occurrences(data, column=None):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"(.)\1{2,}", "\\1", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data
        result[column] = result[column].apply(lambda x: re.sub(r"(.)\1{2,}", "\1", str(x)).strip())

    return result


def remove_emojis_base(emoji_data):
    emoj = re.compile("["
                      u"\U0001F600-\U0001F64F"  # emoticons
                      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                      u"\U0001F680-\U0001F6FF"  # transport & map symbols
                      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                      u"\U00002500-\U00002BEF"  # chinese char
                      u"\U00002702-\U000027B0"
                      u"\U00002702-\U000027B0"
                      u"\U000024C2-\U0001F251"
                      u"\U0001f926-\U0001f937"
                      u"\U00010000-\U0010ffff"
                      u"\u2640-\u2642"
                      u"\u2600-\u2B55"
                      u"\u200d"
                      u"\u23cf"
                      u"\u23e9"
                      u"\u231a"
                      u"\ufe0f"  # dingbats
                      u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', emoji_data)


def remove_emojis(data, column=None):
    result = ''
    if isinstance(data, str):
        result = remove_emojis_base(data)
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data
        result[column] = result[column].apply(lambda x: remove_emojis_base(x))

    return result


def drop_na(data, column=None):
    result = data
    if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = result.dropna(subset=[column])

    return result


def remove_stopwords(data, column=None):
    result = data
    if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        stopwords_list = []
        stopwords_list2 = []
        stopword_count = []
        for index, row in result.iterrows():
            for token in row[column].split():
                if token.lower() in stopwords:
                    stopwords_list.append(token)

            stopwords_list2.append(stopwords_list)
            stopword_count.append(len(stopwords_list))

        result['stopwords'] = stopwords_list2
        result['stopword_count'] = stopword_count

        return result


def char_count(data, column=None):
    result = data
    if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result['char_count'] = result[column].apply(lambda x: len(x))

    return result


def word_count(data, column=None):
    result = data
    if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result['word_count'] = result[column].apply(lambda x: len(str(x).split()))

    return result


def calculate_avg_word_len(x):
    words = x.split()
    word_len = 0
    for word in words:
        word_len += len(word)
    return word_len/len(words) if len(words) else 0


def avg_word_len(data, column=None):
    result = data
    if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result.dropna(subset=[column], inplace=True)
        result['avg_word_len'] = result[column].apply(lambda x: calculate_avg_word_len(x))

    return result


def get_exe_time(start_time):
    end_time = time.time()
    sec = end_time - start_time
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Total execution time: {0}:{1}:{2}".format(int(hours), int(mins), round(sec, 2)))
    print("\n")


def clean_data(lst, data, column=None, save=False, name=None):
    if len(lst) > 0 and data is not None and (isinstance(data, str) or isinstance(data, pd.DataFrame)
                                              or isinstance(pd.Series)):

        if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
            # Remove all Unnamed columns
            data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

            # Check for column name
            if column is None:
                print("Please provide a column name")
                return False
            # Check for file name
            if save and name is None:
                print("Please provide a file name for saving")
                return False
        # Check for file name
        elif isinstance(data, str):
            if save and name is None:
                print("Please provide a file name for saving")
                return False

        temp_data = data

        lst.sort()

        print("Starting data cleaning...")
        start_time = time.time()

        if 1 in lst:
            temp_data = remove_newlines(data=temp_data, column=column)
        if 2 in lst:
            temp_data = remove_emails(data=temp_data, column=column)
        if 3 in lst:
            temp_data = remove_urls(data=temp_data, column=column)
        if 4 in lst:
            temp_data = remove_hashtags(data=temp_data, column=column)
        if 5 in lst:
            temp_data = remove_if_only_number(data=temp_data, column=column)
        if 6 in lst:
            temp_data = remove_mentions(data=temp_data, column=column)
        if 7 in lst:
            temp_data = remove_retweets(data=temp_data, column=column)
        if 8 in lst:
            temp_data = remove_text_between_square_brackets(data=temp_data, column=column)
        if 9 in lst:
            temp_data = remove_multiple_whitespaces(data=temp_data, column=column)
        if 10 in lst:
            temp_data = remove_multiple_occurrences(data=temp_data, column=column)
        if 11 in lst:
            temp_data = remove_emojis(data=temp_data, column=column)
        if 12 in lst:
            temp_data = char_count(data=temp_data, column=column)
        if 13 in lst:
            temp_data = word_count(data=temp_data, column=column)
        if 14 in lst:
            temp_data.dropna(subset=[column], inplace=True)
            temp_data = avg_word_len(data=temp_data, column=column)
        if 15 in lst:
            temp_data.dropna(subset=[column], inplace=True)
            temp_data = remove_stopwords(data=temp_data, column=column)


        if 99 in lst:
            if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
                temp_data.dropna(subset=[column], inplace=True)

        print("Data cleaning done.")
        get_exe_time(start_time)

        # If save file is True
        if save and (isinstance(data, pd.DataFrame) or isinstance(data, pd.Series)):
            Path('data').mkdir(parents=True, exist_ok=True)
            temp_data.to_csv('data/' + name + ".csv", index=False, encoding='utf-8')
            print("File " + name + ".csv saved to data folder.")
        elif save and isinstance(data, str):
            Path('data').mkdir(parents=True, exist_ok=True)
            f = open("data/" + name + ".txt", "w+")
            f.write(temp_data)
            f.close()
            print("File " + name + ".txt saved to data folder.")

        return temp_data
    else:
        print("Please provide at least one option and make sure data is not empty and in required format.")
        return False
