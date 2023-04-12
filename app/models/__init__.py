# coding: utf-8

from models.plagiarism.doc2vec import Doc2vec
from models.plagiarism.all_mini_lm import AllMiniLML6V2
from models.plagiarism.distiluse import DistiluseBaseMultilingualV1
from models.plagiarism.camembert import CamembertLarge

__all__ = [
    'Doc2vec',
    'AllMiniLML6V2',
    'DistiluseBaseMultilingualV1',
    'CamembertLarge',
]