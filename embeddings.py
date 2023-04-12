# coding: utf-8

import logging
import pickle

from rich.progress import track

from app import settings
from app.settings import Granularity as G
from app import dataloader
from app.models.plagiarism.base import PlagiarismModelInterface as plagiarism_model # noqa: 
from app.models.plagiarism import AllMiniLML6V2
from app.models.plagiarism import DistiluseBaseMultilingualV1
from app.models.plagiarism import Doc2vec
from app.models.plagiarism import CamembertLarge


logger = logging.getLogger(__name__)


def create_embedings(model: plagiarism_model, dataloader):
    model = model

    dataset = dataloader.load_data(
        granularity=G.PARAGRAPH,
        del_punctuation=False,
        del_stopword=False,
        del_digit=True,
        del_space=True,
    )

    for data in track(dataset, description="create embedings"):
        data['embeding'] = model.encode(data['clean_text'])

    embedings_path = settings.EMBEDDINGS_FOLDER / f'emdedings-{model}.pickle'
    with open(embedings_path, 'wb') as file:
        pickle.dump(dataset, file)


if __name__ == '__main__':
    models = [
        AllMiniLML6V2(),
        DistiluseBaseMultilingualV1(),
        Doc2vec(load_from='assets/models/model-Doc2vec.pickle'),
        CamembertLarge(),
    ]

    for model in models:
        create_embedings(model=model, dataloader=dataloader)
