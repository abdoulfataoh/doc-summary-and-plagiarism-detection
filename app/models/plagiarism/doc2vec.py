# coding: utf-8

from gensim.models.doc2vec import Doc2Vec


class Doc2vec:
    def __init__(self) -> None:
        ...
    
    def get_model(self, **kwargs):
        return Doc2Vec(**kwargs)
