# coding: utf-8

from app.models.plagiarism.doc2vec import Doc2vec
from app.models.plagiarism.all_mini_lm import AllMiniLML6V2
from app.models.plagiarism.distiluse import DistiluseBaseMultilingualV1
from app.models.plagiarism.camembert import CamembertLarge

__all__ = [
    'Doc2vec',
    'AllMiniLML6V2',
    'DistiluseBaseMultilingualV1',
    'CamembertLarge',
]
