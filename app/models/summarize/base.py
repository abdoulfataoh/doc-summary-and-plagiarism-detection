# coding: utf-8

from abc import ABC, abstractmethod


class SummarizeModelInterface(ABC):
    """
    Tremplate for Summarization models
    """

    def __init__(self, **kwargs) -> None:
        pass

    @abstractmethod
    def summarization_task(
            self,
            input: str,
            max_tokens: int,
            **kwargs
    ):
        pass
