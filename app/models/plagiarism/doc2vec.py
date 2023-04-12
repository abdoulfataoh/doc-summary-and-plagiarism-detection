# coding: utf-8

from typing import Any

from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from .base import PlagiarismModelInterface


class Doc2vec(PlagiarismModelInterface):

    _model: Doc2Vec

    def __init__(self, **kwargs) -> None:
        self._model = Doc2Vec(**kwargs)
        if kwargs.get('existing_model') is not None:
            self._model = Doc2Vec.load(kwargs.get('existing_model'))

    def train(self, **kwargs):
        docs = kwargs['documents']
        vector_size = kwargs['vector_size']
        window = kwargs['window']
        min_count = kwargs['min_count']
        workers = kwargs['workers']
        tagged_docs = [TaggedDocument(doc, [i]) for i, doc in enumerate(docs)]

        # from gensim.test.utils import common_texts
        # from gensim.models.doc2vec import Doc2Vec, TaggedDocument

        # documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]
        # model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)

        self._model = Doc2Vec(
            documents=tagged_docs,
            vector_size=vector_size,
            window=window,
            min_count=min_count,
            workers=workers,
        )

    def encode(self, input: Any, **kwargs) -> Any:
        return self._model.infer_vector(input, **kwargs)

    def __str__(self) -> str:
        return 'Doc2vec'
