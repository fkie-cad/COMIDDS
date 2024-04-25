import pandas as pd
import csv

import src.graph_creator as gc


def main():
    with open("assets/data/datasets.csv") as file:
        data = pd.read_csv(file, delimiter=";")

    gc.datasets_per_year(data)
    gc.dataset_test(data)


if __name__ == '__main__':
    main()
