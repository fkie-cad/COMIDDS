import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.lines as lines

host_color = "#fcba00"
network_color = "#004e9f"
both_color = "#909085"

data_handles = [
    lines.Line2D([], [], linewidth=0, color=network_color, marker='o',
                 label="Network Data", markersize=10),
    lines.Line2D([], [], linewidth=0, marker='o', color=host_color,
                 label="Host Data", markersize=10),
    lines.Line2D([], [], linewidth=0, marker='o', color=both_color,
                 label="Both", markersize=10),
]
label_handles = [
    lines.Line2D([], [], linewidth=0, marker='o', color="black",
                 label="Labeled", markersize=10, fillstyle="full"),
    lines.Line2D([], [], linewidth=0, marker='o', color="black",
                 label="Ground Truth", markersize=10, fillstyle="left"),
    lines.Line2D([], [], linewidth=0, marker='o', color="black",
                 label="No Labels", markersize=10, fillstyle="none"),
]


def datasets_over_years(dataframe: pd.DataFrame):
    dataframe = dataframe.sort_values('End Year').reset_index(drop=True)

    dataset_names = dataframe["Name"].tolist()
    start_years = dataframe["Start Year"].tolist()
    end_years = dataframe["End Year"].tolist()

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, (name, start, end) in enumerate(zip(dataset_names, start_years, end_years)):
        style = marker_style(dataframe.iloc[i])

        if start != end:
            ax.plot([name, name], [start, end], **style)
        else:
            ax.plot(name, end, "o", **style)

    plt.ylabel("Year")

    ax.xaxis.tick_top()
    ax.tick_params(axis="x", labelrotation=90)

    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.grid(axis='x', linestyle='-', alpha=0.1)

    first_legend = ax.legend(handles=data_handles, loc="lower right", title="Contained Data")
    second_legend = ax.legend(handles=label_handles, loc="center right", title="Label Availability",
                              bbox_to_anchor=(1, 0.36))
    ax.add_artist(first_legend)
    ax.add_artist(second_legend)

    plt.tight_layout()
    plt.savefig("assets/data/plots/datasets_over_years.png")
    plt.savefig("assets/data/plots/datasets_over_years.pdf", format="pdf")


def marker_style(data_row: pd.DataFrame):
    host_data = data_row["Host Data"]
    net_data = data_row["Network Data"]
    if host_data == "Yes" and net_data == "Yes":
        color = both_color
    elif host_data == "Yes":
        color = host_color
    elif net_data == "Yes":
        color = network_color
    else:
        raise ValueError("Invalid data, a dataset must contain at least one of the above (Host or Network data)")

    descr = data_row["Host Data Labeled"].lower() + data_row["Network Data Labeled"].lower()
    if "yes" in descr:
        fillstyle = "full"
    elif "ground truth" in descr:
        fillstyle = "left"
    else:
        fillstyle = "none"

    style = dict(
        color=color,
        markersize=10,
        lw=10,
        fillstyle=fillstyle,
        solid_capstyle="round",
    )
    return style
