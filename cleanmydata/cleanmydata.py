import ast
import re
import pandas as pd
import time
import sys
import urllib.request
import json
import requests
import spacy
from pathlib import Path
from bs4 import BeautifulSoup

from cleanmydata.language_detection import *

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")


stopwords = spacy.load('en_core_web_sm')
stopwords = stopwords.Defaults.stop_words


def clean_text(data: str, pattern: str, replace_with: str = " ") -> str:
    """Utility function to apply regex patterns to a string."""
    return re.sub(pattern, replace_with, data).strip()


def apply_column_wise(func, data, column: str):
    """Utility function to apply functions column-wise."""
    if isinstance(data, pd.DataFrame):
        data[column] = data[column].apply(func)
    elif isinstance(data, pd.Series):
        data = data.apply(func)
    return data


def remove_newlines(data, column=None):
    return apply_column_wise(lambda x: clean_text(x, r"\n", " "), data, column)


def remove_emails(data, column=None):
    return apply_column_wise(lambda x: clean_text(x, r"([A-z0-9+._-]+@[A-z0-9+._-]+\.[A-z0-9+_-]+)", ""), data, column)


def remove_urls(data, column=None):
    pattern = r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w.,@?^=%&:/~+#-])?'
    return apply_column_wise(lambda x: clean_text(x, pattern, ""), data, column)


def remove_hashtags(data, column=None):
    return apply_column_wise(lambda x: clean_text(x, r"#[A-Za-z0-9_]+", ""), data, column)


def remove_if_only_number(data, column=None):
    return apply_column_wise(lambda x: clean_text(x, r"^[0-9]+$", ""), data, column)


def remove_mentions(data, column=None):
    return apply_column_wise(lambda x: clean_text(x, r"@[A-Za-z0-9_]+", " "), data, column)


def remove_retweets(data, column=None):
    return apply_column_wise(lambda x: clean_text(x, r"\bRT\b", " "), data, column)


def remove_text_between_square_brackets(data, column=None):
    return apply_column_wise(lambda x: clean_text(x, r"[\(\[].*?[\)\]]", " "), data, column)


def remove_multiple_whitespaces(data, column=None):
    return apply_column_wise(lambda x: clean_text(x, r" +", " "), data, column)


def remove_multiple_occurrences(data, column=None):
    return apply_column_wise(lambda x: clean_text(x, r"(.)\1{2,}", r"\1"), data, column)


def remove_emojis_base(emoji_data: str) -> str:
    emoji_pattern = re.compile("["  
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
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
    return emoji_pattern.sub('', emoji_data)


def remove_emojis(data, column=None):
    return apply_column_wise(remove_emojis_base, data, column)


def remove_stopwords(data, column: str):
    """Removes stopwords from the specified column."""
    data['stopwords_removed'] = data[column].apply(lambda x: ' '.join(
        [word for word in x.split() if word.lower() not in stopwords]))
    return data


def char_count(data, column=None):
    return apply_column_wise(lambda x: len(x), data, column)


def word_count(data, column=None):
    return apply_column_wise(lambda x: len(str(x).split()), data, column)


def avg_word_len(data, column=None):
    return apply_column_wise(lambda x: sum(len(word) for word in str(x).split()) / (len(str(x).split()) or 1), data, column)


def remove_html_tags(data, column=None):
    return apply_column_wise(lambda x: BeautifulSoup(x, 'lxml').get_text().strip(), data, column)


def get_contractions():
    """Fetches and returns contractions dictionary."""
    url = "https://raw.githubusercontent.com/pranavnbapat/cleanmydata/main/cleanmydata/contraction..txt"
    contractions = urllib.request.urlopen(url).read().decode('utf-8')
    return ast.literal_eval(contractions)


def cont_to_exp(data, column=None):
    contractions = get_contractions()
    return apply_column_wise(lambda x: ' '.join([contractions.get(word, word) for word in x.split()]), data, column)


def get_exe_time(start_time: float) -> None:
    """Prints the execution time in a human-readable format."""
    end_time = time.time()
    elapsed_time = end_time - start_time

    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)

    print(f"Total execution time: {int(hours):02}:{int(minutes):02}:{seconds:.2f}")


def clean_data(lst, data, column=None, save=False, name=None):
    if not lst or not data:
        print("Please provide at least one option and ensure data is not empty and in required format.")
        return False

    if isinstance(data, pd.DataFrame):
        data = data.loc[:, ~data.columns.str.contains('^Unnamed')].dropna(subset=[column])
        if not column:
            print("Please provide a column name.")
            return False
        if save and not name:
            print("Please provide a file name for saving.")
            return False
    elif isinstance(data, str):
        data = data.strip()

    start_time = time.time()

    func_map = {
        1: remove_newlines, 2: remove_emails, 3: remove_urls, 4: remove_hashtags, 5: remove_if_only_number,
        6: remove_mentions, 7: remove_retweets, 8: remove_text_between_square_brackets, 9: remove_multiple_whitespaces,
        10: remove_multiple_occurrences, 11: remove_emojis, 12: char_count, 13: word_count, 14: avg_word_len,
        15: remove_stopwords, 16: detect_language, 17: detect_language2, 18: remove_html_tags, 19: cont_to_exp
    }

    for option in lst:
        if option in func_map:
            print(f"Running step {option}: {func_map[option].__name__}")
            data = func_map[option](data, column=column)

    print("Data cleaning done.")
    get_exe_time(start_time)

    if save:
        Path('data').mkdir(parents=True, exist_ok=True)
        if isinstance(data, pd.DataFrame):
            data.to_csv(f'data/{name}.csv', index=False, encoding='utf-8')
        else:
            with open(f'data/{name}.txt', 'w+', encoding='utf-8') as f:
                f.write(data)
        print(f"File saved: {name}.")

    return data
