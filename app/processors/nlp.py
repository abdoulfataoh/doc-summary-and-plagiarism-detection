# coding: utf-8

import re
import string

import spacy
from spacy.language import Language
from nltk.corpus import stopwords

from app import settings


spacy_model = spacy.load(settings.SPACY_MODEL_NAME)


def clean_with_spacy(
    text: str,
    del_punctuation: bool,
    del_stopword: bool,
    del_digit: bool,
    del_space: bool,
) -> str:

    nlp: Language = spacy_model
    doc = nlp(text)
    tokens = []

    for token in doc:
        if del_punctuation:
            if token.is_punct:
                continue
        if del_stopword:
            if token.is_stop:
                continue
        if del_digit:
            if token.is_digit:
                continue
        if del_space:
            if token.is_space:
                continue

        tokens.append(token.text.strip().lower())

    return ' '.join(tokens)


def clean_with_re(
    text: str,
    del_punctuation: bool,
    del_stopword: bool,
    del_digit: bool,
    del_space: bool,
) -> str:
    tokens = []
    regex = re.compile('\w+')  # noqa: W605
    doc = re.findall(regex, text)
    for token in doc:
        if del_punctuation:
            if token in string.punctuation:
                continue
        if del_stopword:
            if token in stopwords.words(settings.NLTK_LANGUAGE):
                continue
        if del_digit:
            if token.isdigit():
                continue
        if del_space:
            if token.strip() == '':
                continue

        tokens.append(token.strip().lower())
    print(tokens)
    return ' '.join(tokens)
