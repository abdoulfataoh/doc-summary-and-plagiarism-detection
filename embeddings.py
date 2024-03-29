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


def create_embedings(
        model: plagiarism_model,
        dataloader,
        save: bool = False
) -> dict:

    model = model

    dataset = dataloader.load_data_from_pdf(
        granularity=G.PARAGRAPH,
        del_punctuation=False,
        del_stopword=False,
        del_digit=False,
        del_space=True,
    )

    for data in track(dataset, description="create embedings"):
        data['embeding'] = model.encode(data['clean_text'])

    if save:
        embedings_path = settings.CACHE_FOLDER / f'emdedings-{model}.pickle'  # noqa: E501
        with open(embedings_path, 'wb') as file:
            pickle.dump(dataset, file)

    return dataset


if __name__ == '__main__':
    models = [
        AllMiniLML6V2(),
        DistiluseBaseMultilingualV1(),
        Doc2vec(load_from='assets/models/model-Doc2vec.pickle'),
        CamembertLarge(),
    ]

    for model in models:
        create_embedings(model=model, dataloader=dataloader, save=True)
