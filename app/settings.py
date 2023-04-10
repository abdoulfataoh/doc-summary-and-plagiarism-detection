# coding: utf-8

from pathlib import Path
from enum import Enum

from environs import Env


env = Env()

# [ Path settings ]
ASSETS_FOLDER = env('ASSETS_FOLDER', r'assets')
CACHE_FOLDER = env('CACHE_FOLDER', Path(ASSETS_FOLDER, 'cache'))
DATASET_FOLDER = env('DATASET_FOLDER', Path(ASSETS_FOLDER, 'dataset'))
TRAIN_DATASET_FOLDER = env('TRAIN_DATASET_FOLDER', Path(DATASET_FOLDER, 'train'))  # noqa: E501
TEST_DATASET_FOLDER = env('TEST_DATASET_FOLDER', Path(DATASET_FOLDER, 'test'))
MODELS_FOLDER = env('MODELS_FOLDER', Path(ASSETS_FOLDER, 'models'))
EMBEDDINGS_FOLDER = env('EMBEDDINGS_FOLDER', Path(ASSETS_FOLDER, 'embeddings'))
METRICS_FOLDER = env('METRICS_FOLDER', 'metrics')

# [ Spacy settings ]
SPACY_MODEL_NAME = env('SPACY_MODEL', 'fr_core_news_sm')

# [ NLTK settings]
NLTK_LANGUAGE = env('NLTK_LANGUAGE', 'french')

# [ Granulary ]
class Granularity(Enum):
    WORD = 'WORD'
    PARAGRAPH = 'PARAGRAPH'
    SENTENCE = 'SENTENCE'
    PAGE = 'PAGE'
    DOCUMENT = 'DOCUMENT'
