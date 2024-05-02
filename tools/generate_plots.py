import pandas as pd

import src.graph_creator as gc


def main():
    with open("assets/data/datasets.csv") as file:
        data = pd.read_csv(file, delimiter=";")

    gc.datasets_over_years(data)
    gc.datatypes_count(data)


if __name__ == '__main__':
    main()
