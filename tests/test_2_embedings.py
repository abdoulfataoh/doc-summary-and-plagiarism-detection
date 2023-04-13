# coding: utf-8

import pytest

from app import dataloader
from embeddings import create_embedings
from app.models.plagiarism import AllMiniLML6V2
from app.models.plagiarism import DistiluseBaseMultilingualV1
from app.models.plagiarism import Doc2vec
from app.models.plagiarism import CamembertLarge


@pytest.fixture
def dt():
    return dataloader


def test_create_embedings(dt):
    models = [
        AllMiniLML6V2(),
        DistiluseBaseMultilingualV1(),
        Doc2vec(load_from='assets/models/model-Doc2vec.pickle'),
        CamembertLarge(),
    ]
    for model in models:
        create_embedings(model=model, dataloader=dt)
