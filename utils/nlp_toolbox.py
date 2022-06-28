# coding: utf-8


from pickle import TRUE
import spacy
import string
from unidecode import unidecode


def unidecoder(text):
    return (unidecode(text))


class Tokenizer():
    def __init__(self, spacy_lang: str) -> None:
        self.nlp = spacy.load(spacy_lang) #spacy_lang: en_core_web_sm, fr_core_web_sm

    def get_words_tokens(
        self,
        text: str,
        remove_punctuation: bool,
        remove_stopword: bool,
        remove_digit: bool,
        remove_space: bool
    ):
        doc = self.nlp(text)
        tokens = []
        for token in doc:
            if remove_punctuation:
                if token.is_punct:
                    continue
            if remove_stopword:
                if token.is_stop:
                    continue
            if remove_digit:
                if token.is_digit:
                    continue
            if remove_space:
                if token.is_space:
                    continue
            token_text = token.text
            tokens.append(token_text.strip().lower())
    
        return tokens



