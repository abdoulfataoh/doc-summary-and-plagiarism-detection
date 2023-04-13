# coding: utf-8

from typing import Any

from sentence_transformers import SentenceTransformer

from .base import PlagiarismModelInterface


class DistiluseBaseMultilingualV1(PlagiarismModelInterface):

    _model: SentenceTransformer

    def __init__(self, **kwargs) -> None:
        self._model = SentenceTransformer(
            'sentence-transformers/distiluse-base-multilingual-cased-v1',
            **kwargs
        )

    def train(self, **kwargs):
        raise Exception("NotImplementedError")

    def encode(self, input: Any, **kwargs) -> Any:
        return self._model.encode(input, **kwargs)

    def __str__(self) -> str:
        return 'DistiluseBaseMultilingualV1'
