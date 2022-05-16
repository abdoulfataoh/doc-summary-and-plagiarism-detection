# coding: utf-8

from asyncore import read
import re
from PyPDF2 import PdfFileReader

class Pdf():
    def __init__(self) -> None:
        ...
    
    def extract_text(self, file_path: str, start_page: str, end_page: str):
        reader = PdfFileReader(file_path)
        text = ""
        if start_page == "all":
            number_of_pages = reader.numPages
            for page in range(number_of_pages):
                text = text + reader.pages(page)
            return text
        else:
            regex = re.compile("(\d+)")
            pages_range = re.findall(regex, pages)
            pages_range = [ int(item) for item in pages_range]
            pages_range.sort()
            if len(pages_range) == 1:
                page_number = pages_range[0]
                text = reader.pages(page_number)
                return text
            elif len(pages_range) == 2:
                start_page = pages_range[0]
                end_page = pages_range[1]
                for page in range(start_page, end_page):
                    text = text + reader.pages(page)
                return text
                