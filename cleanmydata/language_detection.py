import pandas as pd
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from concurrent.futures import ThreadPoolExecutor

# Set seed for reproducibility
DetectorFactory.seed = 0


def detect_language(text):
    try:
        return detect(text)
    except LangDetectException:
        return 'unknown'


def detect_language_dataframe(data, column=None, num_workers=4):
    if column is None or column not in data.columns:
        raise ValueError("A valid column name must be provided.")

    # Drop rows where the column is NaN or empty
    data = data.dropna(subset=[column])

    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        languages = list(executor.map(detect_language, data[column].tolist()))

    # Add the detected languages to a new column
    data['language'] = languages

    return data


# Example usage:
if __name__ == "__main__":
    # Sample DataFrame
    df = pd.DataFrame({
        'text': [
            'Hello world!',
            'Bonjour tout le monde!',
            'Hola mundo!',
            None,  # This will be handled gracefully
            'Hallo Welt!',
            'Ciao mondo!',
            ''  # Empty string will return 'unknown'
        ]
    })

    # Detect language in the 'text' column and print the result
    df_with_languages = detect_language_in_dataframe(df, column='text', num_workers=4)
    print(df_with_languages)
