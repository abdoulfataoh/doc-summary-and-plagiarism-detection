# coding: utf-8

from distutils.command.clean import clean
import logging
import json
import sys

from config import Config
from utils.data_loader import DataLoader
from models.doc2vec import Doc2vec


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dataloader = DataLoader(Config.DATASET_PATH)

class TrainPlagiarismDetection():
    def __init__(self, base_model, granularity) -> None:
        if base_model == "doc2vec":

            # load original dataset
            dataset = dataloader.load_original_data(granularity=granularity)

            # cleaned dataset
            cleaned_dataset = dataloader.load_cleaned_dataset(
                dataset=dataset,
                spacy_lang=Config.SPACY_MODEL,
                remove_punctuation=True,
                remove_stopword=True,
                remove_digit=True,
                remove_space=True,
                return_tokens=True
            )
    
            # tag cleaned dataset
            tagged_dataset = dataloader.word2vec_tag_doc(cleaned_dataset)

            # get model
            model = Doc2vec().get_model(
                vector_size=100,
                min_count=2,
                epochs=100,
                workers=Config.WORKERS
            )

            # build vocabulary
            model.build_vocab(tagged_dataset)

            # train model
            model.train(
                        tagged_dataset,
                        total_examples=model.corpus_count,
                        epochs=model.epochs
            )

            # save model
            logger.info("save model")
            save_full_path = Config.TRAIN_MODELS_PATH / f"citadel-{granularity}-{base_model}.model"
            model.save(str(save_full_path))

            # save original dataset
            logger.info("save dataset")
            with open(Config.TRAIN_DATASET_PATH / f"dataset-{granularity}.json", "w") as file:
                json.dump(dataset, file, indent=2)
            
            # save cleaned dataset
            logger.info("save cleaned dataset")
            with open(Config.TRAIN_DATASET_PATH / f"cleaned-dataset-{granularity}.json", "w") as file:
                json.dump(cleaned_dataset, file, indent=2)
            
            # save cleaned dataset
            logger.info("save tagged dataset")
            with open(Config.TRAIN_DATASET_PATH / f"tagged-dataset-{granularity}.json", "w") as file:
                json.dump(tagged_dataset, file, indent=2)

        elif base_model == "some model":
            ...

# commande line execution
if sys.argv[1] == "plagiarism":
    model = sys.argv[2]
    granularity = sys.argv[3]
    TrainPlagiarismDetection(model, granularity)
elif sys.argv[1] == "summary":
    ...
else:
    print("error refer to documentation")