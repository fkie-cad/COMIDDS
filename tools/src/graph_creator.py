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
        style = marker_style(dataframe, i)

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
    # plt.savefig("assets/data/plots/datasets_over_years.pdf", format="pdf")


def marker_style(dataframe: pd.DataFrame, index: int):
    style = dict(
        color=get_color(dataframe.loc[index, "Host Data"], dataframe.loc[index, "Network Data"]),
        markersize=10,
        lw=10,
        fillstyle=get_label(dataframe.loc[index, "Host Data Labeled"], dataframe.loc[index, "Network Data Labeled"]),
        solid_capstyle="round",
    )
    return style


def get_color(host_data: str, net_data: str):
    if host_data == "Yes" and net_data == "Yes":
        return both_color
    elif host_data == "Yes":
        return host_color
    elif net_data == "Yes":
        return network_color
    else:
        raise ValueError("Invalid data for fields 'Host Data' or 'Network Data'")


def get_label(host_lbl: str, net_lbl: str):
    descr = host_lbl.lower() + net_lbl.lower()

    if "yes" in descr:
        return "full"
    elif "ground truth" in descr:
        return "left"
    else:
        return "none"
