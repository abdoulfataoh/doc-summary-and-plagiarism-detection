#coding: utf-8


from pathlib import Path

class Config():
    DATASET_PATH = Path(r"data/pdf/")
    DATASET_TMP_PATH = Path(r"data/tmp/")
    SAVE_MODELS_PATH = Path(r"data/models")
    SPACY_MODEL = "fr_core_news_sm"

