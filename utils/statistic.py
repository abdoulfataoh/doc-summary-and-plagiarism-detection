# coding: utf-8

import json
from statistics import mean

def count_words(dataset_cache_file: str):
    file = open(dataset_cache_file, "r")
    data = json.load(file)
    files_name = set()
    count_word_list = []
    
    # get all files names
    for word in data:
        files_name.add(word["pdf_file_name"])


    # convert to list
    files_name = list(files_name)

    # count words
    for file_name in files_name:
        count_words = 0
        for word in data:
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
    print("--------------------------------------------------------")
    print(f"TOTAL : {sum_value}")
    print(f"MOYENNE : {mean_value}")
    print(f"MIN : {min_value} ({files_name[count_word_list.index(min_value)]})")
    print(f"MAX : {max_value} ({files_name[count_word_list.index(max_value)]})")
    print()
    


# launch
count_words("dataset/cache/dataset-words.json")

