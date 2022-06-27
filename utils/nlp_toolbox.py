# coding: utf-8

from lib2to3.pgen2 import token
import re

import spacy
import nltk
from nltk.corpus import stopwords
import string
from unidecode import unidecode


def unidecoder(text):
    return (unidecode(text))


class Tokenizer():
    def __init__(self, spacy_lang: str, nltk_lang) -> None:
        self.nlp = spacy.load(spacy_lang) #spacy_lang: en_core_web_sm, fr_core_web_sm
        self.stop_words = set(stopwords.words(nltk_lang))

    def get_words_tokens(self, text: str, remove_punctuation: bool, remove_stopword: bool) -> list:
        doc = self.nlp(text)
        tokens = []
        if remove_punctuation:
            for token in doc:
                if not token.is_punct:
                    token = str(token).strip()
                    if remove_stopword:
                        if token not in self.stop_words and token != "":
                            tokens.append(token)
                    else:
                        tokens.append(token)
        else:
            for token in doc:
                token = str(token).strip()
                if remove_stopword:
                    if token not in self.stop_words and token != "":
                        tokens.append(token)
                    else:
                        continue
                else:
                    tokens.append(token)
            
        return tokens
 
