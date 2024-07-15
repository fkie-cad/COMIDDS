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

If you would like to cite this overview in your (academic) work, we recommend to cite the exact release that the cited information refers to, e.g.,
<!--  {% raw %} --> 
```
@misc{idd100,
  author = {{Intrusion Detection Datasets} contributors},
  title = {{Intrusion Detection Datasets v1.0.0 -- GitHub}},
  year = {2024},
  howpublished = {\url{https://github.com/fkie-cad/COMIDDS/releases/tag/v1.0.0}},
  note = {[Online; accessed DD-MMM-YYYY]},
}
```
<!-- {% endraw %} -->

### Acknowledgments

The webpage was made using [Beautiful Jekyll](https://beautifuljekyll.com/).