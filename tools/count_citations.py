from scholarly import scholarly
from pprint import pp
from datetime import datetime

# phrase = "Reproducible and Adaptable Log Data Generation for Sound Cybersecurity Experiments"
# phrase = "Maintainable Log Datasets for Evaluation of Intrusion Detection Systems"
phrase = "Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization"

current_year = datetime.now().year

search_query = scholarly.search_pubs(phrase)
paper = next(search_query)

pp(paper)

cited_by = scholarly.citedby(paper)
count = 0

for i, ppr in enumerate(cited_by):
    print(f"Paper {i + 1}:")
    try:
        year = ppr["bib"]["pub_year"]
    except KeyError:
        continue
    print(year)
    if current_year - int(year) <= 5:
        count += 1

print(count)

# does not seem to work without proxies
# see https://scholarly.readthedocs.io/en/latest/quickstart.html#using-proxies