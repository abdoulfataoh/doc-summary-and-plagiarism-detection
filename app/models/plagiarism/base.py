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
    def get_model(self):
        ...
