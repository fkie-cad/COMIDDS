---
title: About
---

This is an overview of datasets for research in intrusion detection.
Our goal is to provide a comprehensive and detailed list of relevant datasets along with descriptions and links, aiding researchers in finding and selecting suitable data to work with.

### Scope

We mainly focus on datasets suited for developing and evaluating methods for intrusion detection in enterprise networks, i.e., common office environments involving applications such as browsing, emailing, or text processing as well as services such as web, email, or database servers.
We intentionally omit datasets from very different environments such as industrial control systems or Internet exchange points.

### Features

All datasets are summarized in a [table](/COMIDDS/content/all_datasets), which lists some relevant information for each entry - helpful when you want to quickly determine which of them might me useful to you.

For every dataset, there is a separate entry (for example [this one](/COMIDDS/content/datasets/ait_log_dataset)) describing the following characteristics of a given dataset:
- Overview (A general description of the dataset, giving a brief overview over origin, intended usage and some properties of the dataset)
- Environment (A description of the environment the dataset originated from, including networks, operating systems, running services, etc.)
- Activity (What kind of activity, benign and malicious, was performed during the period of data collection)
- Contained Data (What kind of data was collected and how it is present in the dataset, including any processing and labeling)

Additional information includes:
- Data examples wherever possible (i.e., not for binary data)
- A table summarizing all key characteristics of the dataset
- Related published papers
- Related links (homepages, download sources, documentation, etc.)

### Citing this Work

If you are using COMIDDS for your academic work, please cite our [paper](https://doi.org/10.1145/3675741.3675754):
<!--  {% raw %} --> 
```
@inproceedings{10.1145/3675741.3675754,
  author = {B\"{o}nninghausen, Philipp and Uetz, Rafael and Henze, Martin},
  title = {Introducing a Comprehensive, Continuous, and Collaborative Survey of Intrusion Detection Datasets},
  year = {2024},
  isbn = {9798400709579},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/3675741.3675754},
  doi = {10.1145/3675741.3675754},
  booktitle = {Proceedings of the 17th Cyber Security Experimentation and Test Workshop},
  pages = {34–40},
  numpages = {7},
  keywords = {Cyber Range, Cyberattack, Dataset, Enterprise Network, Intrusion Detection, Log Data, Netflow Data, Simulation, Survey, Testbed},
  location = {Philadelphia, PA, USA},
  series = {CSET '24}
}
```
<!-- {% endraw %} -->

If you (additionally) would like to cite specific information from within COMIDDS, we recommend to cite the release that the information is contained in, e.g.,
<!--  {% raw %} --> 
```
@misc{comidds100,
  author = {{COMIDDS} contributors},
  title = {{COMIDDS v1.0.0 -- GitHub}},
  year = {2024},
  howpublished = {\url{https://github.com/fkie-cad/COMIDDS/releases/tag/v1.0.0}},
  note = {[Online; accessed DD-MMM-YYYY]},
}
```
<!-- {% endraw %} -->

### Acknowledgments

The webpage was made using [Beautiful Jekyll](https://beautifuljekyll.com/).