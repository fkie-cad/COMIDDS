import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import matplotlib.lines as lines
import seaborn

seaborn.set_theme()
seaborn.color_palette()
plt.style.use("seaborn-v0_8-colorblind")
sbn_colors = seaborn.color_palette("colorblind")

host_color = sbn_colors[1]
network_color = sbn_colors[0]
both_color = sbn_colors[7]

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
type_handles = [
    patches.Patch(color=network_color, label="Network Sources"),
    patches.Patch(color=host_color, label="Host Sources"),
]


def datasets_over_years(dataframe: pd.DataFrame):
    dataframe = dataframe.sort_values('End Year').reset_index(drop=True)

    dataset_names = dataframe["Name"].tolist()
    start_years = dataframe["Start Year"].tolist()
    end_years = dataframe["End Year"].tolist()

    fig, ax = plt.subplots(figsize=(11, 10))

    for i, (name, start, end) in enumerate(zip(dataset_names, start_years, end_years)):
        style = marker_style(dataframe.iloc[i])

        if start != end:
            ax.plot([name, name], [start, end], **style)
        else:
            ax.plot(name, end, "o", **style)

    ax.xaxis.tick_top()
    ax.tick_params(axis="x", labelrotation=90)

    ax.set_axisbelow(True)
    plt.grid(axis='y', linestyle='-', alpha=1)
    plt.grid(axis='x', linestyle='--', alpha=0.6)

    first_legend = ax.legend(handles=data_handles, loc="lower right", title="Contained Data")
    second_legend = ax.legend(handles=label_handles, loc="center right", title="Label Availability",
                              bbox_to_anchor=(1, 0.36))
    ax.add_artist(first_legend)
    ax.add_artist(second_legend)

    plt.tight_layout()
    plt.savefig("assets/data/plots/datasets_over_years.png")
    plt.savefig("assets/data/plots/datasets_over_years.pdf", format="pdf")


def datatypes_count(dataframe: pd.DataFrame):
    network_types, host_types = count_types(dataframe)
    total_count = dataframe.shape[0]

    labels = list(network_types.keys()) + list(host_types.keys())
    values = list(network_types.values()) + list(host_types.values())
    colors = [network_color] * len(network_types) + [host_color] * len(host_types)

    fig, ax = plt.subplots(figsize=(4.5, 5))

    ax.bar(labels, values, color=colors)

    plt.ylim(top=total_count)
    plt.ylabel("Number of Datasets")

    ax.tick_params(axis="x", labelrotation=90)
    ax.set_axisbelow(True)
    plt.grid(axis='x', linestyle='--', alpha=0)
    plt.grid(axis='y', linestyle='-', alpha=1)
    plt.legend(handles=type_handles, loc="upper right")

    plt.tight_layout()
    plt.savefig("assets/data/plots/datatypes_percentages.png")
    plt.savefig("assets/data/plots/datatypes_percentages.pdf", format="pdf")


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


def count_types(dataframe: pd.DataFrame):
    network_types = {
        "packet captures": 0,
        "network flows": 0,
        "NIDS alerts": 0,
        # "protocol logs": 0,
        "other": 0
    }
    host_types = {
        "HIDS alerts": 0,
        "host log files": 0,
        "system call traces": 0,
        " other": 0,
    }
    benign_activity = {
        "real": 0,
        "simulated": 0,
        "none": 0,
    }
    os_types = {
        "Windows": 0,
        "Linux": 0,
        "  other": 0,
    }
    os_count = {
        "single OS": 0,
        "multi OS": 0,
    }
    matches = {
        "packet captures": ["pcaps", "tcpdump"],
        "network flows": ["netflows", "connection records"],
        "NIDS alerts": ["snort", "suricata", "zeek", "wazuh", "ids", "aminer"],
        # "protocol logs": ["dns", "ssh", "http", "ssl"],
        "HIDS alerts": ["wazuh", "aminer", "sigma"],
        "host log files": ["event", "evtx", "audit", "logs", "sysmon"],
        "system call traces": ["syscall", "dll"],
    }

    for index, row in dataframe.iterrows():
        net_src = row["Network Data Source"].lower()
        host_src = row["Host Data Source"].lower()

        # Skip length =< 1 because datasets with no such source either have an empty string or "-"
        if len(net_src) > 1:
            found_something = False
            for tp in list(network_types.keys())[:-1]:
                if any(x in net_src for x in matches[tp]):
                    network_types[tp] += 1
                    found_something = True
            if not found_something:
                network_types["other"] += 1

        if len(host_src) > 1:
            found_something = False
            for tp in list(host_types.keys())[:-1]:
                if any(x in host_src for x in matches[tp]):
                    host_types[tp] += 1
                    found_something = True
            if not found_something:
                host_types[" other"] += 1

    sorted_network_types = dict(sorted(network_types.items(), key=lambda item: item[1], reverse=True))
    sorted_host_types = dict(sorted(host_types.items(), key=lambda item: item[1], reverse=True))

    return sorted_network_types, sorted_host_types


def cm2inch(*tupl):
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)
