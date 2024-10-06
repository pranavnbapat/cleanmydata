import ast
import re
import time
import urllib.request
import spacy
from pathlib import Path
from bs4 import BeautifulSoup

from cleanmydata.language_detection import *

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")


stopwords = spacy.load('en_core_web_sm')
stopwords = stopwords.Defaults.stop_words


# Utility function to apply regex patterns to a string
def clean_text(data: str, pattern: str, replace_with: str = " ") -> str:
    return re.sub(pattern, replace_with, data).strip()


# Text cleaning functions for single strings
def remove_newlines(data: str) -> str:
    return clean_text(data, r"\n", " ")


def remove_emails(data: str) -> str:
    return clean_text(data, r"([A-z0-9+._-]+@[A-z0-9+._-]+\.[A-z0-9+_-]+)", "")


def remove_urls(data: str) -> str:
    pattern = r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w.,@?^=%&:/~+#-])?'
    return clean_text(data, pattern, "")


def remove_hashtags(data: str) -> str:
    return clean_text(data, r"#[A-Za-z0-9_]+", "")


def remove_if_only_number(data: str) -> str:
    return clean_text(data, r"^[0-9]+$", "")


def remove_mentions(data: str) -> str:
    return clean_text(data, r"@[A-Za-z0-9_]+", " ")


def remove_retweets(data: str) -> str:
    return clean_text(data, r"\bRT\b", " ")


def remove_text_between_square_brackets(data: str) -> str:
    return clean_text(data, r"[\(\[].*?[\)\]]", " ")


def remove_multiple_whitespaces(data: str) -> str:
    return clean_text(data, r" +", " ")


def remove_multiple_occurrences(data: str) -> str:
    return clean_text(data, r"(.)\1{2,}", r"\1")


# Function to remove emojis
def remove_emojis(emoji_data: str) -> str:
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


# Function to remove HTML tags
def remove_html_tags(data: str) -> str:
    return BeautifulSoup(data, 'lxml').get_text().strip()


# Function to remove stopwords
def remove_stopwords(data: str) -> str:
    return ' '.join([word for word in data.split() if word.lower() not in stopwords])


# Function to get contraction list and expand contractions
def get_contractions():
    url = "https://raw.githubusercontent.com/pranavnbapat/cleanmydata/main/cleanmydata/contraction.txt"
    contractions = urllib.request.urlopen(url).read().decode('utf-8')
    return ast.literal_eval(contractions)


def cont_to_exp(data: str) -> str:
    contractions = get_contractions()
    return ' '.join([contractions.get(word, word) for word in data.split()])


# Character and word count functions
def char_count(data: str) -> int:
    return len(data)


def word_count(data: str) -> int:
    return len(data.split())


def avg_word_len(data: str) -> float:
    words = data.split()
    return sum(len(word) for word in words) / len(words) if words else 0


# Time tracking function
def get_exe_time(start_time: float) -> None:
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
        15: remove_stopwords, 16: detect_language, 17: remove_html_tags, 18: cont_to_exp
    }

    for option in lst:
        if option in func_map:
            print(f"Running step {option}: {func_map[option].__name__}")
            data = func_map[option](data)

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
