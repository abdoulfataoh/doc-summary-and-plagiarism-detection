# coding: utf-8

from typing import Any

import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM

from app.models.summarize.base import SummarizeModelInterface


class BarthezOrange(SummarizeModelInterface):

    _tokenizer: Any
    _model: Any

    def __init__(self):
        self._tokenizer = AutoTokenizer.from_pretrained('moussaKam/barthez')
        self._model = AutoModelForSeq2SeqLM.from_pretrained(
            'moussaKam/barthez-orangesum-abstract'
        )

    def summarization_task(self, input: str, max_tokens: int, **kwargs):
        input_ids = torch.tensor(
            [self._tokenizer.encode(input, add_special_tokens=True)]
        )
        self._model.eval()
        predict = self._model.generate(input_ids, max_length=max_tokens)[0]
        summary = self._tokenizer.decode(predict, skip_special_tokens=True)
        return summary
