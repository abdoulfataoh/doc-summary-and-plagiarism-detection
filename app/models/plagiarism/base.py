# coding: utf-8

from abc import ABC, abstractmethod


__all__ = [
    'PlagiarismModelInterface',
]


class PlagiarismModelInterface(ABC):
    """
    Tremplate for Plagiarism detection models
    """

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def train(self, **kwargs):
        ...

    @abstractmethod
    def encode(self, input, **kwargs):
        ...
