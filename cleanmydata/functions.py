import re
import pandas as pd


def remove_emails(data):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"([A-z0-9+._-]+@[A-z0-9+._-]+\.[A-z0-9+_-]+)", "", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data.apply(lambda x: re.sub(r"([A-z0-9+._-]+@[A-z0-9+._-]+\.[A-z0-9+_-]+)", "", str(x)).strip())

    return result


def remove_urls(data):
    result = ''
    if isinstance(data, str):
        result = re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w.,@?^=%&:/~+#-])?', "", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data.apply(lambda x: re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w.,@?^=%&:/~+#-])?', "", str(x)).strip())

    return result


def remove_hashtags(data):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"#[A-Za-z0-9_]+", "", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data.apply(lambda x: re.sub(r"#[A-Za-z0-9_]+", "", str(x)).strip())

    return result


def remove_newlines(data):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"\n", " ", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data.apply(lambda x: re.sub(r"\\n", " ", str(x)).strip())

    return result


def remove_text_between_square_brackets(data):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"[\(\[].*?[\)\]]", " ", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data.apply(lambda x: re.sub(r"[\(\[].*?[\)\]]", " ", str(x)).strip())

    return result


def remove_if_only_number(data):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"^[0-9]+$", " ", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data.apply(lambda x: re.sub(r"^[0-9]+$", " ", str(x)).strip())

    return result


def remove_mentions(data):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"@[A-Za-z0-9_]+", " ", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data.apply(lambda x: re.sub(r"@[A-Za-z0-9_]+", " ", str(x)).strip())

    return result


def remove_retweets(data):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"\bRT\b", " ", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data.apply(lambda x: re.sub(r"\bRT\b", " ", str(x)).strip())

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


def remove_emojis(data):
    result = ''
    if isinstance(data, str):
        result = remove_emojis_base(data)
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data.apply(lambda x: remove_emojis_base(x))

    return result


def remove_multiple_whitespaces(data):
    result = ''
    if isinstance(data, str):
        result = re.sub(r" +", " ", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data.apply(lambda x: re.sub(r" +", " ", str(x)).strip())

    return result


def drop_na(data):
    result = ''
    if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data.apply(lambda x: re.sub(r" +", " ", str(x)).strip())

    return result


def remove_multiple_occurrences(data):
    result = ''
    if isinstance(data, str):
        result = re.sub(r"(.)\1{2,}", "\1", str(data)).strip()
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        result = data.apply(lambda x: re.sub(r"(.)\1{2,}", "\1", str(x)).strip())

    return result


def clean_data(l, data):
    l.sort()
    if 1 in l:
        data = remove_newlines(data)
    if 2 in l:
        data = remove_emails(data)
    if 3 in l:
        data = remove_urls(data)
    if 4 in l:
        data = remove_hashtags(data)
    if 5 in l:
        data = remove_if_only_number(data)
    if 6 in l:
        data = remove_mentions(data)
    if 7 in l:
        data = remove_retweets(data)
    if 8 in l:
        data = remove_text_between_square_brackets(data)
    if 9 in l:
        data = remove_multiple_whitespaces(data)
    if 10 in l:
        data = remove_multiple_occurrences(data)
    return data
