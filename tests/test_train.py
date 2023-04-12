# coding: utf-8

import pytest

from app import dataloader
from train import train_doc2vec


@pytest.fixture
def dt():
    return dataloader


def test_train_doc2vec(dt):
    train_doc2vec(dt)
