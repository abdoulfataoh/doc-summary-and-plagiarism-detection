#coding: utf-8

from pathlib import Path

class Config():
    DATASET_PATH = Path(r"dataset/pdf/")
    TRAIN_DATASET_PATH = Path(r"assets/datasets")
    TRAIN_MODELS_PATH = Path(r"assets/models")
    EMBEDDINGS_PATH = Path(r"assets/embeddings")
    OTHERS_DATA_PATH = Path(r"assets/others")
    SPACY_MODEL = "fr_core_news_sm"
    WORKERS = 2
