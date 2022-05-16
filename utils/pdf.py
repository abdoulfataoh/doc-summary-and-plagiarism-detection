# coding: utf-8

from pdfminer.high_level import extract_text


class Pdf():
    def __init__(self) -> None:
        ...

    def extract_text(self, pdf_file_path: str, page_numbers: list = []):
        text = extract_text(pdf_file_path, page_numbers=page_numbers)
        return text

