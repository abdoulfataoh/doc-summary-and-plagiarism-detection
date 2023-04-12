# coding: utf-8

from typing import Any

from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from .base import PlagiarismModelInterface


class Doc2vec(PlagiarismModelInterface):

    _model: Doc2Vec

    def __init__(self, **kwargs) -> None:
        self._model = Doc2Vec()
        if kwargs.get('load_from') is not None:
            self._model = Doc2Vec.load(kwargs.get('load_from'))

    def train(self, **kwargs):
        docs = kwargs['documents']
        vector_size = kwargs['vector_size']
        window = kwargs['window']
        min_count = kwargs['min_count']
        workers = kwargs['workers']
        tagged_docs = [TaggedDocument(doc, [i]) for i, doc in enumerate(docs)]

        self._model = Doc2Vec(
            documents=tagged_docs,
            vector_size=vector_size,
            window=window,
            min_count=min_count,
            workers=workers,
        )

    def encode(self, input: Any, **kwargs) -> Any:
        if type(input) == str:
            input = input.split()
        return self._model.infer_vector(input, **kwargs)
        

    def __str__(self) -> str:
        return 'Doc2vec'
