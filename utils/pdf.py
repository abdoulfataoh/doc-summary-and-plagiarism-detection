# coding: utf-8


import logging
from pathlib import Path

import fitz

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Pdf():
    def __init__(self) -> None:
        ...

    def extract_text(
        self, pdf_file_path: str,
        granularity: str,
        page_numbers: list = []
    ):
        pdf_file_name = Path(pdf_file_path).name
        doc = fitz.open(pdf_file_path)
        data = []
        if granularity == "document":
            pages_text = ""
            for page in doc:
                pages_text = pages_text + "\n\n" + page.get_text()
            data.append(
                {
                    "type": granularity,
                    "pdf_file_name": pdf_file_name,
                    "text": pages_text

                }
            )
            return data
        else:
            if page_numbers == []:
                for page in doc.pages():
                    data = data + self._extract_text(page, pdf_file_name, granularity)
                return data
            else:
                doc_pages = list(doc.pages())
                for number in page_numbers:
                    number = number - 1  # the first page number is 0
                    page = doc_pages[number]
                    data = data + self._extract_text(page, pdf_file_name, granularity)
                return data

    def _extract_text(self, page, pdf_file_name: str, granularity: str) -> list:
        page_number = page.number + 1
        if granularity == "page":
            page_text = page.get_text()
            return [
                    {
                        "type": granularity,
                        "pdf_file_name": pdf_file_name,
                        "page_number": page_number,
                        "text": page_text
                    }
            ]
            return page_text
        elif granularity == "paragraph":
            paragraphs = []
            blocks = page.get_text("blocks", sort=True)
            for block in blocks:
                if block[6] == 0:  # if  block contain text
                    paragraphs_text = block[4]
                    paragraphs_number = block[5]
                    paragraphs.append(
                        {
                            "type": granularity,
                            "pdf_file_name": pdf_file_name,
                            "page_number": page_number,
                            "paragraphs_number": paragraphs_number,
                            "text": paragraphs_text
                        }
                    )
            return paragraphs
        elif granularity == "word":
            words = []
            word_number = 1
            for word in page.get_text("words", sort=True):
                words_text = word[4]
                word_number = word_number + 1
                words.append(
                    {
                        "type": granularity,
                        "pdf_file_name": pdf_file_name,
                        "page_number": page_number,
                        "word_number": word_number,
                        "text": words_text

                    }
                )
            return words
