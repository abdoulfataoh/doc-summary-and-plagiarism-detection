# coding: utf-8
# show dataset statistic

import json
from statistics import mean

from utils.data_loader import DataLoader
from config import Config


def count_words(dataset: str):
    files_name = set()
    count_word_list = []
    for word in dataset:  # build  unique file name list
        files_name.add(word["pdf_file_name"])
    files_name = list(files_name)  # convert files names set to list
    for file_name in files_name:  # count words
        count_words = 0
        for word in dataset:
            if word["pdf_file_name"] == file_name:
                count_words = count_words + 1
        count_word_list.append(count_words)

    # statistic
    sum_value = sum(count_word_list)
    min_value = min(count_word_list)
    mean_value = mean(count_word_list)
    max_value = max(count_word_list)

    # printer
    for file_name, count_word in zip(files_name, count_word_list):
        print(f'{count_word} \t :  {file_name}')
    print("-----------------------------------------------------------------")
    print(f"TOTAL: {sum_value}")
    print(f"MOYENNE: {mean_value}")
    print(f"MIN: {min_value} ({files_name[count_word_list.index(min_value)]})")
    print(f"MAX: {max_value} ({files_name[count_word_list.index(max_value)]})")


# launch
dataloader = DataLoader(Config.DATASET_PATH)
dataset = dataloader.load_original_data("word")
count_words(dataset)
