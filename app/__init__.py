# coding: utf-8

import spacy

from app import settings
from app.settings import Granularity as G
from app.dataloader import Pdf
from app.dataloader import DataLoader
# from app.processors import clean_with_spacy
from app.processors import clean_with_re


__all__ = [
    'dataLoader',
    'pdf',
    'cleaner',
]

pdf = Pdf()
cleaner = clean_with_re

if settings.TEST == True:
    dataloader = DataLoader(
        filespath=settings.TEST_DATASET_FOLDER,
        pdf=pdf,
        cleaner=cleaner,
    )
else:
    dataloader = DataLoader(
        filespath=settings.TEST_DATASET_FOLDER,
        pdf=pdf,
        cleaner=cleaner,
    )




