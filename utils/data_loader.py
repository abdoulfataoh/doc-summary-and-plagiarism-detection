# coding: utf-8

from pathlib import Path
import logging
import json

from pdf import Pdf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataLoader(object):

    def __init__(self, pdf_folder_path: str) -> None:
        self.pdf_folder_path = pdf_folder_path
        self.pdf_tool = Pdf()
        ...
    
    def get_pdf_files_name(self) -> list:
        pdf_files_name = []
        for pdf_file_name in Path(self.pdf_folder_path).glob("*.pdf"):
            pdf_files_name.append(pdf_file_name)
        logger.info(f'we found {len(pdf_files_name)} pdf files from <{self.pdf_folder_path}>')
        print(pdf_files_name[0])
        return pdf_files_name
    
    
    def load_data(self, granularity: str) -> list:
        data = []
        for pdf_file_name in self.get_pdf_files_name():
                logger.info(f'extract {granularity} from {pdf_file_name}')
                data = data + self.pdf_tool.extract_text(pdf_file_name, granularity)
        return data




if __name__ == "__main__":
    import json

    data_loader = DataLoader(r'dataset/pdf/test/01')
    data = data_loader.load_data(granularity='document')
    print(data)
    # with open("dataset/cache/dataset-words.json", 'w') as file:
    #     json.dump(data, file)


            

