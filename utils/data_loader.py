# coding: utf-8

import logging
from pathlib import Path
from typing import List, Union, Dict

from utils.pdf import Pdf
from utils.nlp import TextCleaner
from utils.enumerations import Granularity
from utils.entities import Document, Page, Paragraph

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataLoader:

    _files_path: str
    _pdf: Pdf
    _text_cleaner: TextCleaner
    _listed_files: List[str]

    def __init__(
        self,
        files_path: str,
        pdf: Pdf,
        text_cleaner: TextCleaner
    ) -> None:

        self._files_path = files_path
        self._pdf = pdf
        self._text_cleaner = text_cleaner
        self._listed_files = self._listing_pdf_files(files_path)

        if not self._listed_files:
            raise Exception("No pdf file detected")
            logger.warning(f"Unable de find pdf file from {files_path}")

    def load_data(
        self,
        granularity: Granularity
    ) -> List[Dict[str, Union[Document, Page, Paragraph]]]:

        dataset = []
        for pdf_path in self._listed_files:
            log_msg = f"load {pdf_path} data ..."
            data = self._pdf.extract_text(pdf_path, granularity)
            dataset.extend(data)
            logger.info(log_msg)

        return dataset

    def clean_data(
        self,
        dataset: List[Union[Document, Page, Paragraph]],
        spacy_lang_model: str,
        remove_punctuation: bool,
        remove_stopword: bool,
        remove_digit: bool,
        remove_space: bool,
        return_word_list: bool
    ) -> List[Union[Document, Page, Paragraph]]:

        for data in dataset:
            log_msg = f"clean {data.file_name} ..."
            logger.info(log_msg)
            text = data.text
            clean_text = self._text_cleaner.clean(
                text=text,
                remove_punctuation=remove_punctuation,
                remove_stopword=remove_stopword,
                remove_digit=remove_digit,
                remove_space=remove_space,
                return_word_list=return_word_list
            )
            data.cleaned_text = clean_text

    def _listing_pdf_files(self, files_path: Union[str, Path]) -> List[str]:
        files_path = Path(files_path)
        logger.info(f"Listing pdf files from {files_path} ...")
        if files_path.is_file():
            listed_files = [str(files_path)]
            log_msg = "We found 1 pdf file"

        elif files_path.is_dir():
            listed_files = [str(path) for path in files_path.glob("*.pdf")]
            log_msg = f"We found {len(listed_files)} pdf files"

        logger.info(log_msg)

        return listed_files

    @property
    def text_cleaner(self) -> TextCleaner:
        return self._text_cleaner

    @text_cleaner.setter
    def text_cleaner(self, text_cleaner) -> bool:
        logger.info("set new text_cleaner object")
        self._text_cleaner = text_cleaner
        return True

    @text_cleaner.deleter
    def text_cleaner(self) -> bool:
        logger.warning("deleting text_cleaner is not allowed")
        return False
