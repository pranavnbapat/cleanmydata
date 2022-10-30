import pandas as pd
from ftlangdetect import detect

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")


def detect_language(data, column=None):
    result = ''
    try:
        if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
            result = data
            result['language'] = result[column].apply(lambda x: detect(text=x, low_memory=False)['lang'])
            result['lang_prob'] = result[column].apply(lambda x: detect(text=x, low_memory=False)['score'])
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")

    return result


def map_detect_language(data):
    return detect(text=data, low_memory=False)


def detect_language2(data, column=None):
    result = ''
    try:
        if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
            result = data
            temp_list = result[column].to_list()
            # Detects the language using map function and converts it to the list
            lang_res = list(map(map_detect_language, temp_list))
            result['language'] = lang_res
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")

    return result
