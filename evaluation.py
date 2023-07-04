# coding: utf-8

from typing import Any
import json
from pathlib import Path
import sys

import evaluate


class EvaluateSummary():
    _rouge: Any
    _predictions: list
    _references: list

    def __init__(self, summary_dict_path: Path) -> None:
        self._rouge = evaluate.load('rouge')
        self._predictions = []
        self._references = []

        with open(summary_dict_path, 'r') as f:
            data = json.load(f)
            for d in data:
                self._predictions.append(d['text'])
                self._references.append(d['summary'])

    def compute(self):
        results = self._rouge.compute(
            predictions=self._predictions,
            references=self._references
        )
        return results


if __name__ == '__main__':
    summary_dict_path = sys.argv[1]
    eval_summary = EvaluateSummary(
        summary_dict_path=summary_dict_path
    )
    r = eval_summary.compute()
    print(r)
