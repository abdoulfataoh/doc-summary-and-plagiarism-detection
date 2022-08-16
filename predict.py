# # coding: utf-8


import logging
import pickle
from pathlib import Path
from typing import Union

import fitz
from gensim.models.doc2vec import Doc2Vec
from sklearn.metrics.pairwise import cosine_similarity

from utils import pdf
from utils import text_cleaner
from utils import Config
from utils import DataLoader
from utils import Granularity
from models.plagiarism import doc2vec
from models.plagiarism import distiluse
from models.plagiarism import camembert_large
from models.plagiarism import all_mini_lm


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PredictionPlagiarismDetection(object):

    _dataloader: DataLoader
    _doc: fitz
    _base_model: str
    _file_path: Union[str, Path]
    _granularity: Granularity
    _line: str

    def __init__(
        self,
        base_model: str,
        file_path: Union[str, Path],
        granularity: Granularity
    ) -> None:

        self._dataloader = DataLoader(file_path, pdf, text_cleaner)
        self._doc = fitz.open(file_path)
        self._base_model = base_model
        self._file_path = file_path
        self._granularity = granularity
        self._line = '\n____________________________\n'

    def predict(self, threshold: float):
        if self._base_model == 'gensim_doc2vec':

            # load dataset
            dataset = self._dataloader.load_data(self._granularity)

            # clean dataset
            self._dataloader.clean_data(
                dataset=dataset,
                spacy_lang_model=Config.SPACY_MODEL,
                remove_punctuation=True,
                remove_stopword=True,
                remove_digit=True,
                remove_space=True,
                return_word_list=True
            )

            # load model
            model_path = Config.TRAIN_MODELS_PATH / f"citadel-{self._granularity}-{self._base_model}.model"
            model = Doc2Vec.load(str(model_path))

            # load db embedings
            db_embedings = self._load_embedings(
                self._base_model,
                self._granularity
            )
            progress_step = 100 / len(dataset)
            progress = 0
            for data in dataset:
                vector = model.infer_vector(data.cleaned_text)
                content = ''
                i = 0
                for embeding in db_embedings:
                    similarity = cosine_similarity(
                        vector.reshape(1, -1),
                        embeding.vector.reshape(1, -1)
                    )

                    similarity = similarity[0][0]
                    if similarity >= threshold:
                        i = i + 1
                        content = content + f'similarity: {similarity}\n{embeding.file_name}{self._line}{embeding.text}{self._line}'

                if i > 0:
                    pdf.highlight_annot(
                        doc=self._doc,
                        page=data.page_number - 1,
                        coordinates=data.coordinates,
                        content=content
                    )
                progress = progress + progress_step
                progress = 100 if progress > 100 else progress
                yield progress
                
        elif self._base_model == 'distiluse-base-multilingual-cased-v1':

            # load dataset
            dataset = self._dataloader.load_data(self._granularity)

            # clean dataset
            self._dataloader.clean_data(
                dataset=dataset,
                spacy_lang_model=Config.SPACY_MODEL,
                remove_punctuation=False,
                remove_stopword=False,
                remove_digit=True,
                remove_space=True,
                return_word_list=False
            )

            # load model
            model = distiluse.get_model()

            # load db embedings
            db_embedings = self._load_embedings(
                self._base_model,
                self._granularity
            )
            
            progress_step = 100 / len(dataset)
            progress = 0
            for data in dataset:
                vector = model.encode(data.cleaned_text)
                content = ''
                i = 0
                for embeding in db_embedings:
                    similarity = cosine_similarity(
                        vector.reshape(1, -1),
                        embeding.vector.reshape(1, -1)
                    )

                    similarity = similarity[0][0]
                    if similarity >= threshold:
                        i = i + 1
                        content = content + f'similarity: {similarity}\n{embeding.file_name}{self._line}{embeding.text}{self._line}'

                if i > 0:
                    pdf.highlight_annot(
                        doc=self._doc,
                        page=data.page_number - 1,
                        coordinates=data.coordinates,
                        content=content
                    )
                progress = progress + progress_step
                progress = 100 if progress > 100 else progress
                yield progress


        elif self._base_model == 'all-MiniLM-L6-v2':

            # load dataset
            dataset = self._dataloader.load_data(self._granularity)

            # clean dataset
            self._dataloader.clean_data(
                dataset=dataset,
                spacy_lang_model=Config.SPACY_MODEL,
                remove_punctuation=False,
                remove_stopword=False,
                remove_digit=True,
                remove_space=True,
                return_word_list=False
            )

            # load model
            model = distiluse.get_model()

            # load db embedings
            db_embedings = self._load_embedings(
                self._base_model,
                self._granularity
            )

            progress_step = 100 / len(dataset)
            progress = 0
            for data in dataset:
                vector = model.encode(data.cleaned_text)
                content = ''
                i = 0
                for embeding in db_embedings:
                    similarity = cosine_similarity(
                        vector.reshape(1, -1),
                        embeding.vector.reshape(1, -1)
                    )

                    similarity = similarity[0][0]
                    if similarity >= threshold:
                        i = i + 1
                        content = content + f'similarity: {similarity}\n{embeding.file_name}{self._line}{embeding.text}{self._line}'

                if i > 0:
                    pdf.highlight_annot(
                        doc=self._doc,
                        page=data.page_number - 1,
                        coordinates=data.coordinates,
                        content=content
                    )
                progress = progress + progress_step
                progress = 100 if progress > 100 else progress
                yield progress

        elif self._base_model == 'camembert-large':

            # load dataset
            dataset = self._dataloader.load_data(self._granularity)

            # clean dataset
            self._dataloader.clean_data(
                dataset=dataset,
                spacy_lang_model=Config.SPACY_MODEL,
                remove_punctuation=False,
                remove_stopword=False,
                remove_digit=True,
                remove_space=True,
                return_word_list=False
            )

            # load model
            model = distiluse.get_model()

            # load db embedings
            db_embedings = self._load_embedings(
                self._base_model,
                self._granularity
            )

            progress_step = 100 / len(dataset)
            progress = 0
            for data in dataset:
                vector = model.encode(data.cleaned_text)
                content = ''
                i = 0
                for embeding in db_embedings:
                    similarity = cosine_similarity(
                        vector.reshape(1, -1),
                        embeding.vector.reshape(1, -1)
                    )

                    similarity = similarity[0][0]
                    if similarity >= threshold:
                        i = i + 1
                        content = content + f'similarity: {similarity}\n{embeding.file_name}{self._line}{embeding.text}{self._line}'

                if i > 0:
                    pdf.highlight_annot(
                        doc=self._doc,
                        page=data.page_number - 1,
                        coordinates=data.coordinates,
                        content=content
                    )
                progress = progress + progress_step
                progress = 100 if progress > 100 else progress
                yield progress

        self._doc.save(self._file_path[:-4]+'-plagiarism.pdf')

    def _load_embedings(self, base_model: str, granularity: str):
        logger.info(f"load {base_model} embedings with granularity set to {granularity}")
        embedings_file = open(Config.EMBEDDINGS_PATH / f"citadel-{granularity}-{base_model}.dict.pickle", "rb")
        embedings = pickle.load(embedings_file)
        return embedings


# Test
if __name__ == "__main__":
    p = PredictionPlagiarismDetection(
        'gensim_doc2vec',
        'test.pdf',
        Granularity.PARAGRAPH
    )
    for progress in p.predict(0.5):
        print(progress)
