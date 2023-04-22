# coding: utf-8

import logging
from typing import List, Tuple, Union
from pathlib import Path

import fitz

from app.settings import Granularity as G
from app.templates import Document, Page, Paragraph


__all__ = [
    'Pdf',
]


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Pdf():

    def __init__(self) -> None:
        ...

    @staticmethod
    def extract_text(
        pdfpath: Path,
        granularity: G
    ) -> List[dict]:

        filename = Path(pdfpath).name
        doc = fitz.open(pdfpath)
        data = []

        if granularity == G.DOCUMENT:
            document_text = ''
            for page in doc:
                document_text = document_text + '\n' + page.get_text()
            document = Document.to_dict(
                filename=filename,
                text=document_text,
            )
            data.append(document)

        elif granularity == G.PAGE:
            for page in doc:
                page_number = page.number
                page_text = page.get_text()
                page = Page.to_dict(
                    filename=filename,
                    page_number=page_number,
                    text=page_text
                )
                data.append(page)

        elif granularity == G.PARAGRAPH:
            for page in doc:
                page_number = page.number
                blocks = page.get_text('blocks', sort=True)
                for block in blocks:
                    if block[6] == 0:  # if block contain text
                        block_coordinates = block[:4]
                        block_number = block[5] + 1
                        block_text = block[4]
                        paragraph = Paragraph.to_dict(
                            filename=filename,
                            page_number=page_number,
                            paragraph_number=block_number,
                            text=block_text,
                            coordinates=block_coordinates
                        )
                        data.append(paragraph)
        else:
            raise ValueError(f"Unexpected granulary value: '{granularity}'")

        return data

    @staticmethod
    def highlight_annot(
        document: Union[Path, fitz.fitz.Document],
        page_number: int,
        coordinates: Tuple[float, float, float, float],
        content: str = ''
    ) -> None:

        if type(document) is not fitz.fitz.Document:
            document = fitz.open(document)
        page = document[page_number]
        annot = page.add_highlight_annot(coordinates)
        annot.set_info(content=content)

    @staticmethod
    def replace_text(
        document: Union[Path, fitz.fitz.Document],
        page_number: int,
        coordinates: Tuple[float, float, float, float],
        text: str,
        **kwargs
    ) -> None:

        if type(document) is not fitz.fitz.Document:
            document = fitz.open(document)

        page = document[page_number]
        rect = fitz.Rect(coordinates)
        blocks = page.get_text('dict')['blocks']
        for block in blocks:
            try:
                spans = block['lines'][0]['spans'][0]
                fontsize = spans['size']
                fontname = spans['font']
                color = (1, 1, 1)  # spans['color']
            except Exception:
                fontsize = 12
                color = (1, 1, 1)
            if coordinates == block['bbox']:
                break
        page.draw_rect(rect, color=color, fill=color, overlay=True)
        page.insert_textbox(
            rect,
            text,
            fontsize=fontsize,
        )
        document.saveIncr()
