# coding: utf-8

import pytest

from app import settings
from app import pdf
from app import cleaner
from app.dataloader import DataLoader
from app.models.plagiarism import AllMiniLML6V2
from app.models.plagiarism import DistiluseBaseMultilingualV1
from app.models.plagiarism import Doc2vec
from app.models.plagiarism import CamembertLarge
from predict import predict_plagiarism


@pytest.fixture
def dt():
    doc_dataloader = DataLoader(
        filespath=settings.TEST_DATASET_FOLDER,
        pdf=pdf,
        cleaner=cleaner
    )
    return doc_dataloader


def test_predict_plagiarism(dt):
    models = [
        AllMiniLML6V2(),
        DistiluseBaseMultilingualV1(),
        Doc2vec(load_from='assets/models/model-Doc2vec.pickle'),
        CamembertLarge(),
    ]
    for model in models:
        database_path = settings.EMBEDDINGS_FOLDER / f'emdedings-{model}.pickle'  # noqa: E501
        predictions = predict_plagiarism(
            model=model,
            database_path=database_path,
            doc_dataloader=dt,
            threshold=50
        )
        assert predictions != []
