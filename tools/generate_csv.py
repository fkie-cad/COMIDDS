import src.string_parser as parse

FIRST_ENTRY_LINE = 11
LINES_AFTER_TABLE_END = 7
POS = {
    "Name": 0,
    "Focus": 1,
    "TL;DR": 2,
    "Year": 3,
    "Setting": 4,
    "OS Type": 5,
    "Labeled?": 6,
    "Data Type/Sources": 7,
    "Packed Size": 8,
    "Unpacked Size": 9,
}


def main():
    with open("content/all_datasets.md") as file:
        datasets = file.readlines()[FIRST_ENTRY_LINE - 1: - LINES_AFTER_TABLE_END]

    csv_string = (
        "Name;"
        "Network Focus;"
        "Host Focus;"
        "Start Year;"
        "End Year;"
        "Setting;"
        "OS Type;"
        
        "Network Log Source;"
        "Network Logs Labeled;"
        "Host Log Source;"
        "Host Logs Labeled;"
        
        "Attack Categories;"
        "User Emulation;"
        
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

        new_entry += parse.extract_from_table(details_md, "Network Log Source") + ";"
        new_entry += parse.extract_from_table(details_md, "Network Logs Labeled") + ";"
        new_entry += parse.extract_from_table(details_md, "Host Log Source") + ";"
        new_entry += parse.extract_from_table(details_md, "Host Logs Labeled") + ";"

        new_entry += parse.extract_from_table(details_md, "Attack Categories") + ";"
        new_entry += parse.extract_from_table(details_md, "User Emulation") + ";"

        new_entry += parse.size_in_mb(content[POS["Packed Size"]]) + ";"
        new_entry += parse.size_in_mb(content[POS["Unpacked Size"]]) + ";"

        new_entry += "\n"
        csv_string += new_entry

    print(csv_string)

    with open("datasets.csv", "w") as file:
        file.write(csv_string)


if __name__ == '__main__':
    main()
