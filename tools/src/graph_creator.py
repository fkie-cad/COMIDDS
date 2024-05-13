import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import matplotlib.lines as lines
import seaborn

seaborn.set_theme()
seaborn.color_palette()
plt.style.use("seaborn-v0_8-colorblind")
sbn_colors = seaborn.color_palette("colorblind")

# Uni Bonn colors
# host_color = "#fcba00"
# network_color = "#004e9f"
# both_color = "#909085"

# default colorblind-friendly colors
host_color = sbn_colors[1]
network_color = sbn_colors[0]
both_color = sbn_colors[7]

benign_activity_color = sbn_colors[2]
os_type_color = sbn_colors[8]
os_count_color = sbn_colors[9]

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
                 label="Direct", markersize=10, fillstyle="full"),
    lines.Line2D([], [], linewidth=0, marker='o', color="black",
                 label="Indirect", markersize=10, fillstyle="left"),
    lines.Line2D([], [], linewidth=0, marker='o', color="black",
                 label="No Labels", markersize=10, fillstyle="none"),
]
type_handles = [
    patches.Patch(color=network_color, label="Network Data Formats"),
    patches.Patch(color=host_color, label="Host Data Formats"),
    patches.Patch(color=benign_activity_color, label="Benign Activity"),
    patches.Patch(color=os_type_color, label="Operating Systems"),
    patches.Patch(color=os_count_color, label="Number of Systems"),
]


def datasets_over_years(dataframe: pd.DataFrame):
    dataframe = dataframe.sort_values('End Year').reset_index(drop=True)

    dataset_names = dataframe["Name"].tolist()
    start_years = dataframe["Start Year"].tolist()
    end_years = dataframe["End Year"].tolist()

    fig, ax = plt.subplots(figsize=(11, 4.75))

    for i, (name, start, end) in enumerate(zip(dataset_names, start_years, end_years)):
        style = marker_style(dataframe.iloc[i])

        if start != end:
            ax.plot([name, name], [start, end], **style)
        else:
            ax.plot(name, end, "o", **style)

    ax.xaxis.tick_top()
    ax.tick_params(axis="x", labelrotation=90)
    plt.ylabel("Year")

    ax.set_axisbelow(True)
    plt.grid(axis='y', linestyle='-', alpha=1)
    plt.grid(axis='x', linestyle='--', alpha=0.6)

    first_legend = ax.legend(handles=data_handles, loc="lower right", title="Contained Data", alignment="left",
                             framealpha=1)
    first_legend.get_frame().set_facecolor("white")
    first_legend.get_frame().set_linewidth(0)
    second_legend = ax.legend(handles=label_handles, loc="lower center", title="Label Availability",
                              bbox_to_anchor=(0.746, 0), alignment="left", framealpha=1)
    second_legend.get_frame().set_facecolor("white")
    second_legend.get_frame().set_linewidth(0)
    ax.add_artist(first_legend)
    ax.add_artist(second_legend)

    plt.tight_layout()
    plt.savefig("assets/data/plots/datasets_over_years.png")
    plt.savefig("assets/data/plots/datasets_over_years.pdf", format="pdf")


def datatypes_count(dataframe: pd.DataFrame):
    all_dicts = count_types(dataframe)
    total_count = dataframe.shape[0]

    labels, values, colors, x_pos = order_bar_data(all_dicts)

    fig, ax = plt.subplots(figsize=(5.5, 5.05))

    plt.bar(x_pos, values, color=colors)
    plt.xticks(x_pos, labels)

    plt.ylim(top=total_count)
    plt.ylabel("Number of Datasets")

    ax.tick_params(axis="x", labelrotation=90)
    ax.set_axisbelow(True)
    plt.grid(axis='x', linestyle='--', alpha=0)
    plt.grid(axis='y', linestyle='-', alpha=1)

    legend = ax.legend(handles=type_handles, loc="upper left", framealpha=1)
    legend.get_frame().set_facecolor("white")
    legend.get_frame().set_linewidth(0)
    ax.add_artist(legend)

    plt.tight_layout()
    plt.savefig("assets/data/plots/datatypes_count.png")
    plt.savefig("assets/data/plots/datatypes_count.pdf", format="pdf")


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
    # The spaces before some "other" keys are there to prevent matplotlib from merging them all into a single label
    network_types = {
        "packet captures": 0,
        "network flows": 0,
        "NIDS alerts": 0,
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
    os_counts = {
        "single OS": 0,
        "multiple OS": 0,
    }
    matches = {
        "packet captures": ["pcaps", "tcpdump"],
        "network flows": ["netflows", "connection records"],
        "NIDS alerts": ["snort", "suricata", "zeek", "wazuh", " ids ", "aminer"],

        "HIDS alerts": ["wazuh", "aminer", "sigma"],
        "host log files": ["event", "evtx", "audit", "logs", "sysmon"],
        "system call traces": ["syscall", "dll"],

        "real": ["real"],
        "simulated": ["synthetic"],
        "none": [],  # everything else

        "Windows": ["windows"],
        "Linux": ["linux"],
        "  other": [],  # everything else

        "single OS": ["single os"],
        "multiple OS": [],  # everything else
    }
    dicts = [network_types, host_types, benign_activity, os_types, os_counts]

    for index, row in dataframe.iterrows():
        net_src = row["Network Data Source"].lower()
        host_src = row["Host Data Source"].lower()
        activity_descr = row["Benign Activity"].lower()
        os_type = row["OS Type"].lower()
        os_count = row["Setting"].lower()

        data = [net_src, host_src, activity_descr, os_type, os_count]
        default_key_names = ["other", " other", "none", "  other", "multiple OS"]

        for i in range(len(data)):
            # Skip length =< 1 because data values of this length are either empty or "-"
            if len(data[i]) > 1:
                found_something = False
                for entry in list(dicts[i].keys())[:-1]:
                    if any(keyword in data[i] for keyword in matches[entry]):
                        dicts[i][entry] += 1
                        found_something = True
                if not found_something:
                    dicts[i][default_key_names[i]] += 1

    for i, dct in enumerate(dicts):
        if i == 2:
            # dont order benign activity
            continue
        dicts[i] = dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))

    return list(dicts)


def order_bar_data(all_dicts: list[dict]):
    color_list = [network_color, host_color, benign_activity_color, os_type_color, os_count_color]
    labels = []
    values = []
    colors = []
    positions = []

    for i, entry in enumerate(all_dicts):
        labels += list(entry.keys())
        values += list(entry.values())
        colors += [color_list[i]] * len(entry)

        cur_min = max(positions, default=0)
        if i < 1:
            spacing = 1
        else:
            spacing = 2
        new_positions = list(range(cur_min + spacing, cur_min + len(entry) + spacing))
        positions += new_positions

    return labels, values, colors, positions
