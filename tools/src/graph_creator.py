import matplotlib.pyplot as plt
import pandas as pd
from src.field_names import FieldNames as Fn
import numpy as np


def datasets_per_year(dataframe: pd.DataFrame):
    year_range = list(range(dataframe[Fn.end_year].min(), dataframe[Fn.end_year].max() + 1))
    no_attacks = [0] * len(year_range)
    host_attacks = [0] * len(year_range)
    network_attacks = [0] * len(year_range)
    both_attacks = [0] * len(year_range)

    for _, ds_entry in dataframe.iterrows():
        host = ds_entry[Fn.host_attacks]
        network = ds_entry[Fn.network_attacks]
        year_index = year_range.index(ds_entry[Fn.end_year])

        if host == "Yes" and network == "Yes":
            both_attacks[year_index] += 1
        elif host == "Yes":
            host_attacks[year_index] += 1
        elif network == "Yes":
            network_attacks[year_index] += 1
        else:
            no_attacks[year_index] += 1

    attack_focus = {
        "Network Attacks": network_attacks,
        "Host Attacks": host_attacks,
        "Host&Network Attacks": both_attacks,
        "No Attacks": no_attacks,
    }

    width = 0.6
    figure, axis = plt.subplots(figsize=(12, 8))
    bottom = np.zeros(len(year_range))

    for category, count in attack_focus.items():
        axis.bar(year_range, count, width, label=category, bottom=bottom)
        bottom += count

    axis.set_title("Datasets per year and included attacks")
    axis.set_xlabel("Year")
    axis.set_ylabel("Number of Datasets")
    axis.legend()

    plt.tight_layout()
    plt.savefig("tools/testplot.png")


def dataset_test(dataframe: pd.DataFrame):
    dataframe = dataframe.sort_values(Fn.end_year)

    x_year = dataframe[Fn.end_year].tolist()
    y_names = dataframe[Fn.ds_name].tolist()

    fig, ax = plt.subplots(figsize=(8, 12))

    ax.scatter(x_year, y_names)  # alpha controls the transparency of the points

    plt.title('Datasets Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Dataset')
    plt.xticks(x_year, rotation=90)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.savefig("tools/test.png")
