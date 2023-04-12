# coding: utf-8


import logging

from app import settings
from app.settings import Granularity as G
from app import dataloader
from app.models.plagiarism import Doc2vec

logger = logging.getLogger(__name__)


def train_doc2vec(dataloader):
    dataset = dataloader.load_data(
        granularity=G.PARAGRAPH,
        del_punctuation=True,
        del_stopword=False,
        del_digit=False,
        del_space=True,
    )

    model = Doc2vec()

    texts_words = (data['clean_text'].split() for data in dataset)

    model.train(
        documents=texts_words,
        vector_size=300,
        window=2,
        min_count=1,
        workers=4
    )

    savepath = settings.MODELS_FOLDER / f'model-{model}.pickle'
    logger.info("save model at {savepath}")
    model._model.save(str(savepath))


if __name__ == '__main__':
    train_doc2vec(dataloader)
