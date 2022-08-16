# coding: utf-8
# show dataset statistic

import json
from statistics import mean
from matplotlib import pyplot as plt

from utils import DataLoader
from utils import Config


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

    # results to dic
    results_dic = {}
    results_dic["sum_value"] = sum_value
    results_dic["min_value"] = min_value
    results_dic["mean_value"] = mean_value
    results_dic["max_value"] = max_value

    # printer
    for file_name, count_word in zip(files_name, count_word_list):
        print(f'{count_word} \t :  {file_name}')
        results_dic[file_name] = count_word

    print("-----------------------------------------------------------------")
    print(f"TOTAL: {sum_value}")
    print(f"MOYENNE: {mean_value}")
    print(f"MIN: {min_value} ({files_name[count_word_list.index(min_value)]})")
    print(f"MAX: {max_value} ({files_name[count_word_list.index(max_value)]})")

    # save result dic
    with open(Config.OTHERS_DATA_PATH / "result_statistic.json", "w") as file:
        json.dump(results_dic, file, indent=2)


def plot_figure():
    file = open("result_statistic.json", "r")
    data = json.load(file)

    del data["sum_value"]
    del data["mean_value"]
    del data["max_value"]
    del data["min_value"]

    values = []
    indexs = [i for i in range(len(data))]
    values = list(data.values())

    plt.figure(figsize=(14, 10))
    plt.bar(indexs, values)
    plt.plot([0, 100], [14931.787234042553, 14931.787234042553], c="orange", label="moyenne")
    plt.title("Nombre de mots par documents", fontdict={'fontsize': 18})
    plt.xlabel("Identidiants documents", fontdict={'fontsize': 16})
    plt.ylabel("Nombre de mots", fontdict={'fontsize': 16})
    plt.legend()
    plt.savefig("dataset.png")


# launch
if __name__ == '__main__':
    dataloader = DataLoader(Config.DATASET_PATH)
    dataset = dataloader.load_original_data("word")
    # count_words(dataset)
    plot_figure()
