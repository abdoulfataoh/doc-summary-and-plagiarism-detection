# coding: utf-8

import logging
from pathlib import Path
from typing import List, Callable, Any, Union

from rich.progress import track

from app.dataloader.pdf import Pdf
from app.settings import Granularity as G

logger = logging.getLogger(__name__)


class DataLoader:

    _filespath: Path
    _cleaner: Any
    _files: List[Path]

    def __init__(
        self,
        filespath: Path,
        cleaner: Union[Callable, None] = None,
    ) -> None:
        self._files = []
        self._filespath = filespath
        self._cleaner = cleaner

        if self._filespath.is_dir():
            self._files = list(self._filespath.rglob('*.pdf'))
        elif self._filespath.is_file():
            self._files.append(self._filespath)
        else:
            raise FileNotFoundError("Unable to found pdf file at {filespath}")

    def load_data_from_pdf(
        self,
        granularity: G = G.PARAGRAPH,
        del_punctuation: bool = False,
        del_stopword: bool = False,
        del_digit: bool = False,
        del_space: bool = False,
    ) -> List[dict]:

        dataset = []

        for pdf_path in track(
            self._files,
            description="pdf text extractor"
        ):
            logger.info(f"load {pdf_path} data ...")
            data = Pdf.extract_text(pdf_path, granularity)
            if self._cleaner is None:
                dataset.extend(data)
            else:
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

    def load_data_from_json(
        self,
        del_punctuation: bool = False,
        del_stopword: bool = False,
        del_digit: bool = False,
        del_space: bool = False,
        json_parser: Callable = lambda x: x,
    ) -> List[dict]:
        raise Exception("NotImplementedException")

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
