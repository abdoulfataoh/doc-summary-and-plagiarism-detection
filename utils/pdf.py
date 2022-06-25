# coding: utf-8

from dataclasses import dataclass
import logging

import fitz
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Pdf():
    def __init__(self) -> None:
        ...


    def extract_pages_text(self, pdf_file_path: str, granularity: str, page_numbers: list = []):
        doc = fitz.open(pdf_file_path)
        data = []
        if page_numbers == []:
            for page in doc.pages():
                data = data + self._extract_text(page, granularity)
            return data
        else:
            doc_pages = list(doc.pages())
            for number in page_numbers:
                number = number - 1 # the first page number is 0
                page = doc_pages[number]
                data = data + self._extract_text(page, granularity)
            return data


    def _extract_text(self, page, type: str) -> list:
        page_number = page.number + 1
        if type == "page":
            page_text = page.get_text()
            return [
                    {
                        "page_number": page_number,
                        "page_text": page_text
                    }
            ]        
            return page_text
        elif type == "paragraph":
            paragraphs = []
            blocks = page.get_text("blocks", sort=True)
            for block in blocks:
                if block[6] == 0: #if  block contain text
                    paragraphs_text = block[4]
                    paragraphs_number = block[5]
                    paragraphs.append(
                        {
                            "page_number": page_number,
                            "paragraphs_number": paragraphs_number,
                            "paragraphs_text": paragraphs_text
                        }
                    )
            return paragraphs
                       

if __name__ == '__main__':
    pdf = Pdf()
    r = pdf.extract_pages_text('dataset/pdf/test/test.pdf', "paragraph", [1])
    print(r)