# coding: utf-8

from typing import Any

import openai

from app.models.summarize import SummarizeModelInterface


class OpenAi(SummarizeModelInterface):
    _api_key: str
    _openai: Any
    _model_name: str
    _temperature: float
    _frequency_penalty: float
    _presence_penalty: float

    def __init__(
            self,
            api_key: str,
            model_name: str,
            temperature: float = 0.7,
            frequency_penalty: float = 0.0,
            presence_penalty: float = 0.0,
    ):
        self._api_key = api_key
        self._model_name = model_name
        self._openai = openai
        self._openai.api_key = api_key
        self._temperature = temperature
        self._frequency_penalty = frequency_penalty
        self._presence_penalty = presence_penalty

    def summarization_task(
            self,
            input: str,
            max_tokens: int,
            top_p: float = 1.0,
    ) -> str:
        ask = 'Resume moi ce texte:\n{input}'
        response = self._openai.Completion.create(
            model=self._model_name,
            prompt=ask,
            temperature=self._temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=self._frequency_penalty,
            presence_penalty=self._presence_penalty,
        )

        text: str = response['choices'][0]['text']
        text = text.strip()

        return text
