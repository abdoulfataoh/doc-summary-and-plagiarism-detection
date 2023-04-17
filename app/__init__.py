# coding: utf-8

from app import settings
from app.dataloader import Pdf
from app.dataloader import DataLoader
# from app.processors import clean_with_spacy
from app.processors import clean_with_re


settings.WORKDIR.mkdir(parents=True, exist_ok=True)
settings.ASSETS_FOLDER.mkdir(parents=True, exist_ok=True)
settings.CACHE_FOLDER.mkdir(parents=True, exist_ok=True)
settings.METRICS_FOLDER.mkdir(parents=True, exist_ok=True)
settings.MODELS_FOLDER.mkdir(parents=True, exist_ok=True)
settings.DATASET_FOLDER.mkdir(parents=True, exist_ok=True)
settings.PLAGIARISM_DATASET_FOLDER.mkdir(parents=True, exist_ok=True)
settings.SUMMARIZE_DATASET_FOLDER.mkdir(parents=True, exist_ok=True)
settings.PLAGIARISM_TRAIN_DATASET_FOLDER.mkdir(parents=True, exist_ok=True)
settings.PLAGIARISM_TEST_DATASET_FOLDER.mkdir(parents=True, exist_ok=True)

__all__ = [
    'dataLoader',
    'Pdf',
    'cleaner',
]

cleaner = clean_with_re

if settings.TEST is True:
    dataloader = DataLoader(
        filespath=settings.PLAGIARISM_TEST_DATASET_FOLDER,
        cleaner=cleaner,
    )
else:
    dataloader = DataLoader(
        filespath=settings.PLAGIARISM_TRAIN_DATASET_FOLDER,
        cleaner=cleaner,
    )
