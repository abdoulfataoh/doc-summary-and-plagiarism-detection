# coding: utf-8

import logging
from pathlib import Path
from enum import Enum

from environs import Env

logging.basicConfig(level=logging.WARNING)

env = Env()
env.read_env()

TEST = env.bool('TEST', False)

# [ PATH SETTINGS ]
ASSETS_FOLDER = env('ASSETS_FOLDER', Path('assets'))
CACHE_FOLDER = env('CACHE_FOLDER', Path(ASSETS_FOLDER, 'cache'))
DATASET_FOLDER = env('DATASET_FOLDER', Path(ASSETS_FOLDER, 'dataset'))
TRAIN_DATASET_FOLDER = env('TRAIN_DATASET_FOLDER', Path(DATASET_FOLDER, 'train'))  # noqa: E501
TEST_DATASET_FOLDER = env('TEST_DATASET_FOLDER', Path(DATASET_FOLDER, 'test'))
MODELS_FOLDER = env('MODELS_FOLDER', Path(ASSETS_FOLDER, 'models'))
EMBEDDINGS_FOLDER = env('EMBEDDINGS_FOLDER', Path(ASSETS_FOLDER, 'embeddings'))
METRICS_FOLDER = env('METRICS_FOLDER', Path('metrics'))
WORKDIR = env('WORKDIR', Path('static'))

# [ SPACY SETTINGS ]
SPACY_MODEL_NAME = env('SPACY_MODEL', 'fr_core_news_sm')

# [ NLTK SETTINGS ]
NLTK_LANGUAGE = env('NLTK_LANGUAGE', 'french')

# [ OPENAI ]
OPENAI_API_KEY = env('OPENAI_API_TOKEN', '')


# [ Granulary ]
class Granularity(Enum):
    WORD = 'WORD'
    PARAGRAPH = 'PARAGRAPH'
    SENTENCE = 'SENTENCE'
    PAGE = 'PAGE'
    DOCUMENT = 'DOCUMENT'
