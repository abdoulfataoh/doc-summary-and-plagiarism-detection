# coding: utf-8

from models.summarization.bart_large_cnn import BartBargeCNN
from models.summarization.camembert2camembert_shared import Camembert2camembert_shared


__all__ = [
    'bart_large_cnn',
    'camembert2camembert_shared'
]


bart_large_cnn = BartBargeCNN()
camembert2camembert_shared = Camembert2camembert_shared()
