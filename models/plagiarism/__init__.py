# coding: utf-8

from models.plagiarism.doc2vec import Doc2vec
from models.plagiarism.all_mini_lm import AllMiniLML6V2
from models.plagiarism.distiluse import DistiluseBaseMultilingualV1
from models.plagiarism.camembert import CamembertLarge


__all__ = [
    'doc2vec',
    'all_mini_lm',
    'camembert_large',
    'distiluse',
]


doc2vec = Doc2vec()
all_mini_lm = AllMiniLML6V2()
camembert_large = CamembertLarge()
distiluse = DistiluseBaseMultilingualV1()