# coding: utf-8

import json
from gensim.models.doc2vec import TaggedDocuments
from pathlib import Path

from utils.data_loader import DataLoader

def make_clean_dataset(dataset_path: str, cache_foler_path: str, granularities: list):
    for granulaty in granularities:
        dataloader = DataLoader(dataset_path)
        dataset = dataloader.load_cleaned_dataset(
            granularity=granulaty,
            spacy_lang="fr_core_news_sm",
            remove_punctuation=True,
            remove_stopword=True,
            remove_digit=True,
            remove_space=True,
            return_tokens=False
        )
        file_path = Path(cache_foler_path, f"dataset-clean-{granulaty}-text.json")
        with open(file_path, 'w') as file:
            json.dump(dataset, file)

# make_clean_dataset(r'dataset/pdf', ["paragraph", "page", "document"])

def make_tag_doc(dataset_path: str, cache_foler_path: str, granularities: list):
    for granulaty in granularities:
        file_path = Path(cache_foler_path, f"dataset-clean-{granulaty}-text.json")
        with open(file_path, 'r') as file:
            dataset = json.load(file)



 