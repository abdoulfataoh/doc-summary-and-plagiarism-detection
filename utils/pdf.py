# coding: utf-8


import logging
from typing import List, Tuple, Union
from pathlib import Path

import fitz
from unidecode import unidecode

from utils.enumerations import Granularity
from utils.entities import Document, Page, Paragraph


__all__ = [
    'Pdf',
]


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Pdf():

    def __init__(self) -> None:
        ...

    def extract_text(
        self,
        pdf_path: str,
        granularity: Granularity
    ) -> List[Union[Document, Page, Paragraph]]:

        file_name = Path(pdf_path).name
        doc = fitz.open(pdf_path)
        data = []

        if granularity == Granularity.DOCUMENT:
            document_text = ''
            for page in doc:
                document_text = document_text + '\n' + page.get_text()
                document_text = unidecode(document_text)
            document = Document(file_name, document_text)
            data.append(document)

        elif granularity == Granularity.PAGE:
            for page in doc:
                page_number = page.number + 1
                page_text = page.get_text()
                page_text = unidecode(page_text)
                page = Page(file_name, page_number, page_text)
                data.append(page)

        elif granularity == Granularity.PARAGRAPH:
            for page in doc:
                page_number = page.number + 1
                blocks = page.get_text('blocks', sort=True)
                for block in blocks:
                    if block[6] == 0:  # if block contain text
                        block_coordinates = block[:4]
                        block_number = block[5] + 1
                        block_text = block[4]
                        block_text = unidecode(block_text)
                        paragraph = Paragraph(
                            file_name,
                            page_number,
                            block_number,
                            block_text,
                            block_coordinates 
                        )
                        data.append(paragraph)

        else:
            ...

        return data

    def highlight_annot(
        self,
        doc: fitz,
        page: int,
        coordinates: Tuple[float, float, float, float],
        content: str = ''
    ) -> bool:

        page = doc[page]
        annot = page.add_highlight_annot(coordinates)
        annot.set_info(content=content)

        return True
