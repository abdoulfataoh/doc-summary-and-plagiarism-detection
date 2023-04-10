#coding: utf-8


from sentence_transformers import SentenceTransformer

from models.interface import PlagiarismModelInterface


class DistiluseBaseMultilingualV1(PlagiarismModelInterface):
    def __init__(self) -> None:
        pass

    def get_model(self):
        model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')
        return model
