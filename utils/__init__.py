# coding: utf-8

from utils.pdf import Pdf
from utils.nlp import TextCleaner
from utils.data_loader import DataLoader
from utils.config import Config
from utils.enumerations import Granularity


__all__ = [
    'DataLoader',
    'pdf',
    'text_cleaner',
    'Config',
    'Granularity',
]


pdf = Pdf()
text_cleaner = TextCleaner(Config.SPACY_MODEL)
