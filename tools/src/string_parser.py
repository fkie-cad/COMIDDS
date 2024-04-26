import re


def entry_path(full_name):
    match = re.search(r'\]\((.*?)\)', full_name)

    if match:
        return match.group(1).replace("../", "content/") + ".md"
    else:
        raise ValueError


def name(full_name):
    match = re.search(r'\[(.*?)]', full_name)
    if match:
        return match.group(1)
    else:
        return "PARSE_ERROR"


def network_focus(focus_info: str):
    if "Network" in focus_info or "Both" in focus_info:
        return "Yes"
    else:
        return "No"


def host_focus(focus_info: str):
    if "Host" in focus_info or "Both" in focus_info:
        return "Yes"
    else:
        return "No"


def year_start(year):
    return year.split("-")[0]


def year_end(year):
    try:
        return year.split("-")[1]
    except IndexError:
        return year.split("-")[0]


def size_in_mb(size: str):
    if size == "-":
        return ""
    size = size.replace("<", "").replace(">", "")

    number = float(size.split()[0].replace(",", "."))
    if "mb" in size.lower():
        return str(number)
    elif "gb" in size.lower():
        return str(number * 1000)
    elif "tb" in size.lower():
        return str(number * 1000000)


def extract_from_table(markdown, key):
    pattern = r"\| \*\*{}.*?\| (.*?)\s*\|".format(re.escape(key))
    match = re.search(pattern, markdown, re.DOTALL)
    if match:
        result = match.group(1).strip()
        return result.replace("\"", "").replace("<br/>", ", ").replace("<br>", ", ")
    else:
        return "PARSE_ERROR"
