# coding: utf-8

from typing import Any

from sentence_transformers import SentenceTransformer

from .base import PlagiarismModelInterface


class AllMiniLML6V2(PlagiarismModelInterface):

    _model: SentenceTransformer

    def __init__(self, **kwargs) -> None:
        self._model = SentenceTransformer(
            'all-MiniLM-L6-v2',
            **kwargs
        )

    def train(self, **kwargs):
        raise Exception("NotImplementedError")

    def encode(self, input: Any, **kwargs) -> Any:
        return self._model.encode(input, **kwargs)

    def __str__(self) -> str:
        return 'AllMiniLML6V2'
