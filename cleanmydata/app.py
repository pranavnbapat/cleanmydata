from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cleanmydata.cleanmydata import *

# FastAPI app initialization
app = FastAPI()


# Data model for input validation
class Data(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"message": "CleanMyData API is running"}


# POST endpoints for each cleaning function
@app.post("/remove-emails/")
def clean_remove_emails(data: Data):
    try:
        cleaned_text = remove_emails(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-urls/")
def clean_remove_urls(data: Data):
    try:
        cleaned_text = remove_urls(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-newlines/")
def clean_remove_newlines(data: Data):
    try:
        cleaned_text = remove_newlines(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-hashtags/")
def clean_remove_hashtags(data: Data):
    try:
        cleaned_text = remove_hashtags(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-if-only-number/")
def clean_remove_if_only_number(data: Data):
    try:
        cleaned_text = remove_if_only_number(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-mentions/")
def clean_remove_mentions(data: Data):
    try:
        cleaned_text = remove_mentions(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-retweets/")
def clean_remove_retweets(data: Data):
    try:
        cleaned_text = remove_retweets(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-text-between-square-brackets/")
def clean_remove_text_between_square_brackets(data: Data):
    try:
        cleaned_text = remove_text_between_square_brackets(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-multiple-whitespaces/")
def clean_remove_multiple_whitespaces(data: Data):
    try:
        cleaned_text = remove_multiple_whitespaces(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-multiple-occurrences/")
def clean_remove_multiple_occurrences(data: Data):
    try:
        cleaned_text = remove_multiple_occurrences(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-emojis/")
def clean_remove_emojis(data: Data):
    try:
        cleaned_text = remove_emojis(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-html-tags/")
def clean_remove_html_tags(data: Data):
    try:
        cleaned_text = remove_html_tags(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-stopwords/")
def clean_remove_stopwords(data: Data):
    try:
        cleaned_text = remove_stopwords(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/expand-contractions/")
def clean_expand_contractions(data: Data):
    try:
        cleaned_text = cont_to_exp(data.text)
        return {"cleaned_data": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


