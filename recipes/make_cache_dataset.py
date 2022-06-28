# coding: utf-8

import json

from utils.data_loader import DataLoader

for granulaty in ["paragraph", "page", "document"]:
    dataloader = DataLoader(r'dataset/pdf')
    dataset = dataloader.load_cleaned_dataset(
        granularity=granulaty,
        spacy_lang="fr_core_news_sm",
        remove_punctuation=True,
        remove_stopword=True,
        remove_digit=True,
        remove_space=True,
        return_tokens=False
    )
    with open(f"dataset/cache/dataset-clean-{granulaty}-text.json", 'w') as file:
        json.dump(dataset, file)
        