# coding: utf-8

from typing import Any

from sentence_transformers import SentenceTransformer

from .base import PlagiarismModelInterface


class CamembertLarge(PlagiarismModelInterface):

    _model: SentenceTransformer

    def __init__(self, **kwargs) -> None:
        self._model = SentenceTransformer(
            'camembert/camembert-large',
            **kwargs
        )

    def train(self, **kwargs):
        raise Exception("NotImplementedError")

    def encode(self, input: Any, **kwargs) -> Any:
        return self._model.encode(input, **kwargs)

    def __str__(self) -> str:
        return 'CamembertLarge'
