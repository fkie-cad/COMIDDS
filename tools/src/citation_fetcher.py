from datetime import datetime
import requests
from time import sleep


def get_all_paper_ids(filename):
    all_ids = []
    with open(filename, "r") as file:
        for line in file:
            if line.startswith("| "):
                # Relevant value is in the fourth row
                paper_id = line.split("|")[4].strip()
                if len(paper_id) == 40:
                    all_ids.append(paper_id)
    return all_ids


def fetch_citation_info_from_ids(paper_ids, api_key):
    results = {}
    request_headers = {
        "x-api-key": api_key,
    }
    max_tries = 10
    wait_after_failure = 5  # seconds

    for paper_id in paper_ids:
        print(f"Now processing paper {paper_id}...")
        current_attempt = 0
        success = False

        while not success and current_attempt < max_tries:
            try:
                total_citation_count = get_total_citation_count(paper_id, request_headers)
                if total_citation_count <= 1000:
                    citation_info = single_citation_request(paper_id, request_headers)
                else:
                    citation_info = multi_citation_request(paper_id, total_citation_count, request_headers)
                results[paper_id] = citation_info
                success = True

            except requests.HTTPError as e:
                print(f"WARNING: Unable to fetch citation details for paper with id {paper_id} on attempt {current_attempt + 1}/{max_tries}.")
                print(f"The failed request returned the following:\n{e.args[0].json()}")
                print(f"Waiting for {wait_after_failure} seconds and trying again.")
                sleep(wait_after_failure)
                current_attempt += 1
                continue

        if success:
            print("Done.\n")
        else:
            results[paper_id] = None
            print(f"Unable to fetch citation info after {max_tries} attempts, moving on.\n")

    return results


def count_recent_citations(citation_info: dict, max_age):
    current_year = datetime.now().year
    results = {}

    for paper, citations in citation_info.items():
        if citations is None:
            results[paper] = "API ERROR"
            continue

        recent_citations = 0
        for cit in citations:
            year = cit["citingPaper"]["year"]
            if not year:
                # Some publications do not provide a year value
                continue
            if year >= current_year - max_age:
                recent_citations += 1

        results[paper] = recent_citations

    return results


def swap_placeholders_with_info(filename, processed_citation_info: dict):
    with open(filename, "r") as file:
        content = file.read()

    for placeholder, count in processed_citation_info.items():
        content = content.replace(placeholder, str(count))

    with open(filename, "w") as file:
        file.write(content)


def get_total_citation_count(paper_id, headers):
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}"
    params = {
        "fields": "citationCount",
    }
    req = requests.get(url, params=params, headers=headers)

    if req.status_code != 200:
        raise requests.HTTPError(req)

    sleep(1)
    return req.json()["citationCount"]


def single_citation_request(paper_id, headers, offset=0):
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations"
    params = {
        "fields": "year",
        "limit": 1000,
        "offset": offset,
    }
    req = requests.get(url, params)
    if req.status_code != 200:
        raise requests.HTTPError(req)

    cited_papers = req.json()["data"]
    sleep(1)
    return cited_papers


def multi_citation_request(paper_id, total_count, headers):
    all_citations = []
    current_offset = 0

    while total_count > current_offset:
        citations = single_citation_request(paper_id, headers, offset=current_offset)
        all_citations.extend(citations)
        current_offset += 1000

    return all_citations
