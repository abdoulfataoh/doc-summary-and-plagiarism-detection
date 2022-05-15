# coding: utf-8

import string
import spacy
from nltk.corpus import stopwords
import string
import re


class Tokenizer():
    def __init__(self, spacy_lang: str) -> None:
        self.nlp = spacy.load(spacy_lang)

    def get_words_tokens(self, sentences: str) -> list:
        doc = self.nlp(sentences)
        tokens = [word.text for word in doc]
        return tokens

    def get_sentences_tokens(self, sentences: str) -> list:
        doc = self.nlp(sentences)
        tokens = [sentences.text for sentences in doc.sents]
        return tokens

    @staticmethod
    def get_characters_tokens(sentences: str) -> list:
        doc = sentences
        tokens = list(doc)
        return tokens


class Cleaner():
    def __init__(self, nltk_lang) -> None:
        self.stopwords = set(stopwords.words(nltk_lang))
        self.punctuation = string.punctuation
        ...

    def remove_stopwords(self, tokens: list, tokens_type: str) -> list:
        """tokens_type: word, sentence"""
        if tokens_type == "word":
            cleaner_tokens = [token for token in tokens if token not in self.stopwords]
            return cleaner_tokens
        elif tokens_type == "sentence":
            ...
        else:
            ...
    
    def remove_punctuations(self, tokens: list):
        cleaner_tokens = [token for token in tokens if token not in self.punctuation]
        return cleaner_tokens








