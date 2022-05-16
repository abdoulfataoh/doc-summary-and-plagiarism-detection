# coding: utf-8

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
    def __init__(self) -> None:
        self.punctuation = string.punctuation

    def remove_stopwords(
        self,
        nltk_lang: str,
        tokens: list,
        tokens_type: str
    ):
        """tokens_type: word, sentence"""
        stop_words = set(stopwords.words(nltk_lang))
        if tokens_type == "word":
            cleaner_tokens = [token for token in tokens if token not in stop_words]
            return cleaner_tokens
        elif tokens_type == "sentence":
            regex = re.compile("\w+")
            sentence = "".join(tokens)
            tokens = re.findall(regex, sentence)
            cleaner_tokens = [token for token in tokens if token not in stop_words]
            return cleaner_tokens
        else:
            ...
    
    def remove_punctuations(self, sentence: str):
        cleaner_sentence = [char for char in sentence if char not in self.punctuation]
        return "".join(cleaner_sentence).strip()
