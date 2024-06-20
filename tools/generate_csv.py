import src.string_parser as parse

POS = {
    "Name": 0,
    "Focus": 1,
    "Year": 2,
    # "Times Recently Cited": 3,
    "TL;DR": 4,
    "Setting": 5,
    "OS Type": 6,
    "Labeled?": 7,
    "Data Type/Sources": 8,
    "Packed Size": 9,
    "Unpacked Size": 10,
}


# EXECUTE FROM REPO ROOT

def main():
    with open("content/all_datasets.md") as file:
        file_content = file.readlines()

    datasets_table = [line for line in file_content if line.startswith("|")]
    datasets = datasets_table[2:]  # First two lines are the table header

    csv_string = (
        "Name;"
        "Network Data;"
        "Host Data;"
        "Start Year;"
        "End Year;"
        "Setting;"
        "OS Type;"

        "Network Data Source;"
        "Network Data Labeled;"
        "Host Data Source;"
        "Host Data Labeled;"

        "Attack Categories;"
        "Benign Activity;"

        "Packed Size in MB;"
        "Unpacked Size in MB"
        "\n")

    for dataset in datasets:
        new_entry = ""

        content = dataset.split("|")[1:-1]
        content = [data.strip() for data in content]
        with open(parse.entry_path(content[POS["Name"]])) as file:
            details_md = file.read()

        new_entry += parse.name(content[POS["Name"]]) + ";"
        new_entry += parse.network_focus(content[POS["Focus"]]) + ";"
        new_entry += parse.host_focus(content[POS["Focus"]]) + ";"
        new_entry += parse.year_start(content[POS["Year"]]) + ";"
        new_entry += parse.year_end(content[POS["Year"]]) + ";"
        new_entry += content[POS["Setting"]] + ";"
        new_entry += content[POS["OS Type"]] + ";"

        new_entry += parse.extract_from_table(details_md, "Network Data Source") + ";"
        new_entry += parse.extract_from_table(details_md, "Network Data Labeled") + ";"
        new_entry += parse.extract_from_table(details_md, "Host Data Source") + ";"
        new_entry += parse.extract_from_table(details_md, "Host Data Labeled") + ";"

        new_entry += parse.extract_from_table(details_md, "Attack Categories") + ";"
        new_entry += parse.extract_from_table(details_md, "Benign Activity") + ";"

        new_entry += parse.size_in_mb(content[POS["Packed Size"]]) + ";"
        new_entry += parse.size_in_mb(content[POS["Unpacked Size"]])

        new_entry += "\n"
        csv_string += new_entry

    with open("assets/data/datasets.csv", "w") as file:
        file.write(csv_string)


if __name__ == '__main__':
    main()
