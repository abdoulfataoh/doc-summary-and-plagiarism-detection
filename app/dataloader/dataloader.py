# coding: utf-8

import logging
from pathlib import Path
from typing import List, Callable, Any

from app.dataloader.pdf import Pdf
from app.settings import Granularity as G

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataLoader:

    _filespath: Path
    _pdf: Pdf
    _cleaner: Any
    _files: List[Path]

    def __init__(
        self,
        filespath: Path,
        pdf: Pdf,
        cleaner: Callable,
    ) -> None:

        self._filespath = filespath
        self._pdf = pdf
        self._cleaner = cleaner

        if self._filespath.is_dir():
            self._files = list(self._filespath.rglob('*.pdf'))
        elif self._filespath.is_file():
            self._files.append(self._filespath)
        else:
            raise FileNotFoundError("Unable to found pdf file at {filespath}")

    def load_data(
        self,
        granularity: G,
        del_punctuation: bool,
        del_stopword: bool,
        del_digit: bool,
        del_space: bool,
    ) -> List[dict]:

        dataset = []
        for pdf_path in self._files:
            logger.info(f"load {pdf_path} data ...")
            data = self._pdf.extract_text(pdf_path, granularity)
            for d in data:
                d['clean_text'] = self._cleaner(
                    text=d['text'],
                    del_punctuation=True,
                    del_stopword=True,
                    del_digit=True,
                    del_space=True,
                )
            dataset.extend(data)
        return dataset

    @property
    def text_cleaner(self) -> Callable:
        return self._cleaner

    @text_cleaner.setter
    def text_cleaner(self, cleaner: Callable) -> bool:
        self._cleaner = cleaner
        return True

    @text_cleaner.deleter
    def text_cleaner(self) -> None:
        raise Exception("deleting text_cleaner is not allowed")
