# coding: utf-8

from transformers import pipeline


class BartBargeCNN:
    def __init__(self) -> None:
        ...

    def get_model(self):
        model = pipeline('summarization', model='facebook/bart-large-cnn')
        return model
