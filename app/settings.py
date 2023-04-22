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
WORKDIR = env('WORKDIR', Path('static'))
ASSETS_FOLDER = env.path('ASSETS_FOLDER', 'assets')
CACHE_FOLDER = ASSETS_FOLDER / env.path('CACHE_FOLDER', 'cache')
METRICS_FOLDER = ASSETS_FOLDER / env.path('METRICS_FOLDER', 'metrics')
MODELS_FOLDER = ASSETS_FOLDER / env.path('MODELS_FOLDER', 'models')
DATASET_FOLDER = ASSETS_FOLDER / env.path('DATASET_FOLDER', 'dataset')

PLAGIARISM_DATASET_FOLDER = DATASET_FOLDER / \
    env.path('PLAGIARISM_DATASET_FOLDER', 'plagiarism')
SUMMARIZE_DATASET_FOLDER = DATASET_FOLDER / \
    env.path('SUMMARIZE_DATASET_FOLDER', 'summarize')

PLAGIARISM_TRAIN_DATASET_FOLDER = PLAGIARISM_DATASET_FOLDER / \
    env('PLAGIARISM_TRAIN_DATASET_FOLDER', 'train')
PLAGIARISM_TEST_DATASET_FOLDER = PLAGIARISM_DATASET_FOLDER / \
    env('PLAGIARISM_TEST_DATASET_FOLDER', 'test')

SUMMARY_SECTION_MIN_WORDS = env.int('SUMMARY_SECTION_MIN_WORDS', 50)


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
