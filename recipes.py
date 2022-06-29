# coding: utf-8

import json
from pathlib import Path

from utils.data_loader import DataLoader

def make_clean_datasets(dataset_path: str, cache_foler_path: str, granularities: list):
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


# make_clean_datasets(r'dataset/pdf', ["paragraph", "page", "document"])


def make_tag_doc(dataset_json_path: str, save_file_path):
        with open(dataset_json_path, 'r') as file:
            dataset = json.load(file)
            tagged_dataset = DataLoader.word2vec_tag_doc(dataset)
            with open(save_file_path, "w") as file:
                json.dump(tagged_dataset, file, indent=2)

# make_tag_doc(
#     "dataset/cache/dataset-clean-document.json",
#     "dataset/cache/tagged-dataset-clean-document.json"
# )
