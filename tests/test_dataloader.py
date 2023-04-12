# coding: utf-8

from app import settings
from app.settings import Granularity as G
from app import dataloader


def test_dataloader():
    dataset = dataloader.load_data(
        granularity=G.PARAGRAPH,
        del_punctuation=False,
        del_stopword=False,
        del_digit=False,
        del_space=False,
    )

    assert dataset[0]['filename'] == 'doc.pdf'
    assert dataset[0]['page_number'] == 1
    assert dataset[0]['paragraph_number'] == 1
    assert dataset[0]['text'] == '1ere Page\n'
    assert dataset[0]['clean_text'] == '1ere page'
    assert len(dataset[0]['coordinates']) == 4
    assert dataset[0]['id'] != ''