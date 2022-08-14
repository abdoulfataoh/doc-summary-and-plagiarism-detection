# coding: utf-8

from typing import Union, List

import spacy
from spacy.lang.fr import French
from spacy.lang.en import English

from utils.enumerations import Granularity


__all__ = [
    'TextCleaner',
]


class TextCleaner():

    _nlp: Union[French, English]

    def __init__(self, spacy_lang_model: str) -> None:
        self._nlp = spacy.load(spacy_lang_model)

    def clean(
        self,
        text: str,
        remove_punctuation: bool,
        remove_stopword: bool,
        remove_digit: bool,
        remove_space: bool,
        return_word_list: bool
    ) -> List[str]:

        doc = self._nlp(text)
        cleaned_words = []
        cleaned_text = ''

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
            token_text = token_text.strip()
            token_text = token_text.lower()

            if return_word_list:
                cleaned_words.append(token_text)
            else:
                cleaned_text = cleaned_text + token_text + ' '

        return cleaned_text or cleaned_words
