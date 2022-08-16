# coding: utf-8


import logging
import pickle
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

from utils import pdf
from utils import text_cleaner
from utils import Config
from utils import DataLoader
from utils import Granularity
from models.plagiarism import all_mini_lm, doc2vec
from models.plagiarism import distiluse
from models.plagiarism import camembert_large


__all__ = [
    'TrainPlagiarismDetectionModels',
    'PlagiarismDetectionEmbeddings',
]


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dataloader = DataLoader(Config.DATASET_PATH, pdf, text_cleaner)
# dataloader = DataLoader('dataset/test', pdf, text_cleaner)


class TrainPlagiarismDetectionModels():
    def __init__(self, base_model, granularity: Granularity) -> None:
        if base_model == "gensim_doc2vec":

            # load original dataset
            dataset = dataloader.load_data(granularity=granularity)

            # cleaned dataset
            dataloader.clean_data(
                dataset=dataset,
                spacy_lang_model=Config.SPACY_MODEL,
                remove_punctuation=True,
                remove_stopword=True,
                remove_digit=True,
                remove_space=True,
                return_word_list=True
            )

            # get model
            model = doc2vec.get_model(
                vector_size=100,
                min_count=2,
                epochs=100,
                workers=Config.WORKERS
            )

            docs = [TaggedDocument(d.cleaned_text, [str(d.id)]) for d in dataset]

            # build vocabulary
            model.build_vocab(docs)

            # train model
            model.train(
                        docs,
                        total_examples=model.corpus_count,
                        epochs=model.epochs
            )

            # save model
            logger.info("save model")
            save_full_path = Config.TRAIN_MODELS_PATH / f"citadel-{granularity}-{base_model}.model"
            model.save(str(save_full_path))

        else:
            ...


class PlagiarismDetectionEmbeddings():
    def __init__(
        self,
        base_model,
        granularity: Granularity
    ) -> None:

        if base_model == 'gensim_doc2vec':
            # load original dataset
            dataset = dataloader.load_data(granularity=granularity)

            # cleaned dataset
            dataloader.clean_data(
                dataset=dataset,
                spacy_lang_model=Config.SPACY_MODEL,
                remove_punctuation=True,
                remove_stopword=True,
                remove_digit=True,
                remove_space=True,
                return_word_list=True
            )

            # embedinngs
            model_path = Config.TRAIN_MODELS_PATH / f"citadel-{granularity}-{base_model}.model"
            model = Doc2Vec.load(str(model_path))
            for data in dataset:
                data.vector = model.infer_vector(data.cleaned_text)

            # save embeddins
            self._save_embeddings(base_model, dataset, granularity)

        elif base_model == 'distiluse-base-multilingual-cased-v1':
            # load original dataset
            dataset = dataloader.load_data(granularity=granularity)

            # cleaned dataset
            dataloader.clean_data(
                dataset=dataset,
                spacy_lang_model=Config.SPACY_MODEL,
                remove_punctuation=False,
                remove_stopword=False,
                remove_digit=True,
                remove_space=True,
                return_word_list=False
            )

            # embeddings
            model = distiluse.get_model()
            for data in dataset:
                data.vector = model.encode(data.cleaned_text)

            # save embeddins
            self._save_embeddings(base_model, dataset, granularity)

        elif base_model == 'all-MiniLM-L6-v2':
            # load original dataset
            dataset = dataloader.load_data(granularity=granularity)

            # cleaned dataset
            dataloader.clean_data(
                dataset=dataset,
                spacy_lang_model=Config.SPACY_MODEL,
                remove_punctuation=False,
                remove_stopword=False,
                remove_digit=True,
                remove_space=True,
                return_word_list=False
            )

            # embeddings
            model = all_mini_lm.get_model()
            for data in dataset:
                data.vector = model.encode(data.cleaned_text)

            # save embeddins
            self._save_embeddings(base_model, dataset, granularity)

        elif base_model == 'camembert-large':
            # load original dataset
            dataset = dataloader.load_data(granularity=granularity)

            # cleaned dataset
            dataloader.clean_data(
                dataset=dataset,
                spacy_lang_model=Config.SPACY_MODEL,
                remove_punctuation=False,
                remove_stopword=False,
                remove_digit=True,
                remove_space=True,
                return_word_list=False
            )

            # embeddings
            model = camembert_large.get_model()
            for data in dataset:
                data.vector = model.encode(data.cleaned_text)

            # save embeddins
            self._save_embeddings(base_model, dataset, granularity)

    def _save_embeddings(
        self,
        base_model: str,
        dataset: dict,
        granularity: str
    ):
        logger.info(f"{base_model} - save embeddings")
        with open(Config.EMBEDDINGS_PATH / f"citadel-{granularity}-{base_model}.dict.pickle", "wb") as file:
            pickle.dump(
                dataset,
                file,
                protocol=pickle.HIGHEST_PROTOCOL
            )


# Launch
if __name__ == "__main__":
    TrainPlagiarismDetectionModels('gensim_doc2vec', Granularity.PARAGRAPH)
    PlagiarismDetectionEmbeddings('distiluse-base-multilingual-cased-v1', Granularity.PARAGRAPH)
    PlagiarismDetectionEmbeddings('all-MiniLM-L6-v2', Granularity.PARAGRAPH)
    PlagiarismDetectionEmbeddings('gensim_doc2vec', Granularity.PARAGRAPH)
