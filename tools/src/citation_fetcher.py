from datetime import datetime
import requests


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


def fetch_citation_info_from_ids(paper_ids):
    results = {}
    
    for paper_id in paper_ids:
        try:
            total_citation_count = get_total_citation_count(paper_id)
            if total_citation_count <= 1000:
                citation_info = single_citation_request(paper_id)
            else:
                citation_info = multi_citation_request(paper_id, total_citation_count)
            results[paper_id] = citation_info

        except requests.HTTPError:
            print(f"WARNING: Unable to fetch citation details for paper with id {paper_id}")
            results[paper_id] = None
            continue

    return results


def count_recent_citations(citation_info: dict, max_age):
    current_year = datetime.now().year
    results = {}

    for paper, citations in citation_info.items():
        if not citations:
            results[paper] = "n/a"
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


def get_total_citation_count(paper_id):
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}"
    params = {
        "fields": "citationCount",
    }
    req = requests.get(url, params)
    if req.status_code != 200:
        raise requests.HTTPError

    return req.json()["citationCount"]


def single_citation_request(paper_id, offset=0):
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations"
    params = {
        "fields": "year",
        "limit": 1000,
        "offset": offset,
    }
    req = requests.get(url, params)
    if req.status_code != 200:
        raise requests.HTTPError

    cited_papers = req.json()["data"]
    return cited_papers


def multi_citation_request(paper_id, remaining_citations):
    all_citations = []
    current_offset = 0

    while remaining_citations > 0:
        citations = single_citation_request(paper_id, offset=current_offset)
        all_citations.extend(citations)
        current_offset += 1000
        remaining_citations -= 1000

    return all_citations
