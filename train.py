# coding: utf-8

import logging
from gensim.test.utils import get_tmpfile

from config import Config
from utils.data_loader import DataLoader
from models.doc2vec import Doc2vec


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dataloader = DataLoader(Config.DATASET_PATH)

# change granularity to paragraph, page, document
logger.info("load cleaner dataset")
dataset = dataloader.load_cleaned_dataset(
    granularity="paragraph",
    spacy_lang=Config.SPACY_MODEL,
    remove_punctuation=True,
    remove_stopword=True,
    remove_digit=True,
    remove_space=True,
    return_tokens=True
)
logger.info("tagged dataset")
tagged_dataset = dataloader.word2vec_tag_doc(dataset=dataset)

# get model
logger.info("get model")
model = Doc2vec().get_model(
    vector_size=100,
    min_count=2,
    epochs=100,
    workers=2
)

# build vocabulary
logger.info("build vocabulary")
model.build_vocab(tagged_dataset)

# train model
logger.info("train model")
model.train(
            tagged_dataset,
            total_examples=model.corpus_count,
            epochs=model.epochs
)

# save model
logger.info("save model")
fname = get_tmpfile("citadel-paragraph-doc2vec_model")
model.save(fname)
