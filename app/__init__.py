# coding: utf-8

from app import settings
from app.settings import Granularity as G
from app.dataloader import Pdf
from app.dataloader import DataLoader
# from app.processors import clean_with_spacy
from app.processors import clean_with_re


settings.ASSETS_FOLDER.mkdir(parents=True, exist_ok=True)
settings.CACHE_FOLDER.mkdir(parents=True, exist_ok=True)
settings.DATASET_FOLDER.mkdir(parents=True, exist_ok=True)
settings.TRAIN_DATASET_FOLDER.mkdir(parents=True, exist_ok=True)
settings.TEST_DATASET_FOLDER.mkdir(parents=True, exist_ok=True)
settings.MODELS_FOLDER.mkdir(parents=True, exist_ok=True)
settings.EMBEDDINGS_FOLDER.mkdir(parents=True, exist_ok=True)
settings.METRICS_FOLDER.mkdir(parents=True, exist_ok=True)

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
