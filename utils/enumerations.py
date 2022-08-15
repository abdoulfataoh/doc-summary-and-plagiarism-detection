# coding: utf-8

from enum import Enum


__all__ = [
    'Granularity',
]


class Granularity(Enum):
    WORD = 'WORD'
    PARAGRAPH = 'PARAGRAPH'
    SENTENCE = 'SENTENCE'
    PAGE = 'PAGE'
    DOCUMENT = 'DOCUMENT'
