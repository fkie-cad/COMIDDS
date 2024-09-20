import requests
import sys
import os
import re
from pprint import pprint

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Must be executed from repository root
# ONLY FORMATTED LINKS "[text](link)" WILL BE CHECKED


CONTENT_DIR = "content/"
PATTERN = re.compile(r"\[(.*?)\]\((.*?)\)")


EXCEPTIONS = {
    # Some valid links return nonsensical status codes
    # Only add links that are known to be valid with that specific status code
    # Do not add 404s
    "https://www.keysight.com/us/en/products/network-test/network-test-hardware/perfectstorm.html": 403,
    "https://onlineacademiccommunity.uvic.ca/isot/wp-content/uploads/sites/7295/2023/03/ISOT-Dataset-Overview-v0.5.pdf": 403,
    "https://doi.org/10.1142/9781786340757_0002": 403,
    "https://unsw-my.sharepoint.com/personal/z5025758_ad_unsw_edu_au/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fz5025758%5Fad%5Funsw%5Fedu%5Fau%2FDocuments%2FUNSW%2DNB15%20dataset&ga=1": 401,
    "https://unsw-my.sharepoint.com/personal/z5025758_ad_unsw_edu_au/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fz5025758%5Fad%5Funsw%5Fedu%5Fau%2FDocuments%2FUNSW%2DNB15%20dataset": 401,
    "https://unsw-my.sharepoint.com/personal/z5025758_ad_unsw_edu_au/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fz5025758%5Fad%5Funsw%5Fedu%5Fau%2FDocuments%2FUNSW%2DNB15%20dataset%2FReadMe%2Epdf&parent=%2Fpersonal%2Fz5025758%5Fad%5Funsw%5Fedu%5Fau%2FDocuments%2FUNSW%2DNB15%20dataset": 401,
    "https://unsw-my.sharepoint.com/:x:/r/personal/z5025758_ad_unsw_edu_au/_layouts/15/Doc.aspx?sourcedoc=%7B975B24E4-7E36-4CE1-B98A-9FBE4BB521B7%7D&file=NUSW-NB15_features.csv&action=default&mobileredirect=true": 401,
}


class InvalidLink(Exception):
    pass


def grab_all_links(directory: str) -> dict[str, list[str]]:
    all_files = []
    links_per_file = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))

    for file in all_files:
        with open(file, "r") as f:
            # Do not check for URLs in the example data section, if present
            content = f.read().split("### Data Examples")[0]

            full_match = PATTERN.findall(content)
            links = [link[1] for link in full_match]
            links_per_file[file] = links
    return links_per_file


def verify_internal_anchor(content: str, link: str):
    heading = "# " + link.lstrip("#").replace("---", " ").replace("-", " ")
    if heading not in content:
        raise InvalidLink(f"Anchor does not have a matching heading.")


def verify_internal_absolute_link(link: str):
    if not os.path.exists(link.replace("/COMIDDS/", "") + ".md"):
        raise InvalidLink(f"Absolute link does not point to a valid markdown file.")


def verify_internal_relative_link(link_origin: str, link: str):
    # The first "../" does not actually traverse a path, but it's required by GitHub Pages
    link = link.lstrip("../")

    if not link.endswith(".md"):
        link = link + ".md"
    path = os.path.join(os.path.dirname(link_origin), link)

    if not os.path.exists(path):
        raise InvalidLink(f"Relative link does not point to a valid markdown file.")


def verify_jekyll_link(link: str):
    if any([file in link for file in ["datasets.csv"]]):
        # These files are created at deploy time, can't check for them here
        return

    pattern = re.compile(r"(\/.*?\.[\w:]+)")
    match = pattern.search(link).group(1)
    if not match or not os.path.exists(match.lstrip("/")):
        print(match)
        raise InvalidLink(f"Jekyll link does not point to a valid file.")


def get_url(link: str, verify_ssl: bool):
    return requests.get(
        link, stream=True, timeout=5, allow_redirects=True, verify=verify_ssl
    )


def verify_web_link(link: str):
    verify_ssl = True
    try:
        response = get_url(link, verify_ssl)
    except requests.exceptions.SSLError:
        verify_ssl = False
        response = get_url(link, verify_ssl)
    except Exception as e:
        raise InvalidLink(f"Request failed with:\n{e}")

    if 200 <= response.status_code < 300:
        if not verify_ssl:
            print(
                f"\033[94mINFO:\n\033[0mURL \033[4m{link}\033[0m was accessible, but only when disabling SSL verification.\n"
            )
        return
    elif response.status_code == 418 and "doi.org" in link:
        # Some DOI links return 418 for some reason, even though all of the links are valid
        return
    elif EXCEPTIONS.get(link) == response.status_code:
        return
    elif 300 <= response.status_code < 400:
        raise InvalidLink(
            f"Received a {response.status_code} redirect to {response.headers['Location']}."
        )
    else:
        raise InvalidLink(f"Request returned with status code {response.status_code}.")


def verify_links(file_name: str, links: list[str]):
    chars_not_in_anchors = ["(", ")", ":", ","]
    with open(file_name, "r") as f:
        # This deals with how markdown converts headings to anchors
        file_content = f.read().lower().replace(" - ", " ").replace("-", " ")
        for char in chars_not_in_anchors:
            file_content = file_content.replace(char, "")

    print(f"Checking links in {file_name}...\n")
    counter = 0

    for link in links:
        try:
            if link.startswith("#"):
                verify_internal_anchor(file_content, link)
            elif link.startswith("/"):
                verify_internal_absolute_link(link)
            elif (
                link.startswith("../")
                or link.endswith(".md")
                and not link.startswith("http")
            ):
                verify_internal_relative_link(file_name, link)
            elif link.startswith("{{"):
                verify_jekyll_link(link)
            else:
                verify_web_link(link)
        except InvalidLink as e:
            counter += 1
            print(
                f"\033[93mWARNING:\n\033[0mInvalid link \033[4m{link}\033[0m in file \033[1m{file_name}\033[0m:\n{e}\n"
            )
            continue
    return counter


def main():
    all_links = grab_all_links(CONTENT_DIR)
    counter = 0

    for filename, links in all_links.items():
        counter += verify_links(filename, links)

    if counter:
        print(f"\033[91m{counter} invalid links found.\033[0m")
        sys.exit(1)


if __name__ == "__main__":
    main()