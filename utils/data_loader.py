# coding: utf-8

from pathlib import Path
import logging
import json

from utils.pdf import Pdf
from utils.nlp_toolbox import Tokenizer
from utils.nlp_toolbox import unidecoder
from gensim.models.doc2vec import TaggedDocument

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


    def load_cleaned_dataset(
        self,
        granularity: str,
        spacy_lang: str,
        remove_punctuation: bool,
        remove_stopword: bool,
        remove_digit: bool,
        remove_space: bool,
        return_tokens: bool
    ):
        dataset = self.load_original_data(granularity)
        return_dataset = []
        logger.info("load clean dataset")
        tokenizer = Tokenizer(spacy_lang)
        for index, item in enumerate(dataset):
            pdf_file_name = item["pdf_file_name"]
            remove_items = []
            logger.info(f"clean {pdf_file_name}")
            item_text = unidecoder(item["text"])
            tokens = tokenizer.get_words_tokens(
                text=item_text,
                remove_punctuation=remove_punctuation,
                remove_stopword=remove_stopword,
                remove_digit=remove_digit,
                remove_space=remove_space,
            )
            
            if return_tokens:
                item["text"] = tokens
            else:
                item["text"] = " ".join(tokens)

            if type(tokens) is list and tokens != []:
                return_dataset.append(item)

        return return_dataset


    def load_original_data(self, granularity: str) -> list:
        data = []
        for pdf_file_name in self.get_pdf_files_name():
                logger.info(f'extract {granularity} from {pdf_file_name}')
                data = data + self.pdf_tool.extract_text(pdf_file_name, granularity)
        return data
    
    @staticmethod
    def word2vec_tag_doc(dataset: list) -> list:
        granularity = dataset[0]["type"]
        tagged_doc = []

        logger.info(f"we will tag {granularity} by {granularity}")

        if granularity == "paragraph":
            for paragraph in dataset:
                text = paragraph["text"]
                logger.info(f"tag {text} by {text}")
                tagged_doc.append(
                    TaggedDocument(
                        words=text,
                        tags=[paragraph["pdf_file_name"], paragraph["page_number"], paragraph["paragraphs_number"]]
                    )
                )
        elif granularity == "page":
            for page in dataset:
                text = page["text"]
                logger.info(f"tag {text} by {text}")
                tagged_doc.append(
                    TaggedDocument(
                        words=text,
                        tags=[page["pdf_file_name"], page["page_number"], page["page_number"]]
                    )
                )
        elif granularity == "doc":
            for doc in dataset:
                text = doc["text"]
                logger.info(f"tag {text} by {text}")
                tagged_doc.append(
                    TaggedDocument(
                        words=text,
                        tags=[doc["pdf_file_name"]]
                    )
                )
        return tagged_doc

