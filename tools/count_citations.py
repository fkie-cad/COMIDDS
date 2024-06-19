import src.citation_fetcher as cf


MAIN_FILE = "content/all_datasets.md"
MAX_AGE_IN_YEARS = 5


def main():
    paper_ids = cf.get_all_paper_ids(MAIN_FILE)
    citation_info = cf.fetch_citation_info_from_ids(paper_ids)
    processed_citation_info = cf.count_recent_citations(citation_info, MAX_AGE_IN_YEARS)
    cf.swap_placeholders_with_info(MAIN_FILE, processed_citation_info)


if __name__ == '__main__':
    main()
