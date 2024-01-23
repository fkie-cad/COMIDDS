---
layout: post
title: First release of Intrusion Detection Datasets
subtitle: 43 datasets described in detail, with more to come!
gh-repo: fkie-cad/intrusion-detection-datasets
gh-badge: [star, fork, follow]
tags: [datasets, webpage]
comments: true
author: Philipp Bönninghausen
---

This post marks the beginning of the "Intrusion Detection Datasets" collection.
It is intended to be a comprehensive resource for anyone looking for a dataset suitable for IDS development and evaluation.
However, with research requirements often being complex (and dataset documentation often being lacking), this collection aims to be more than just a list of names and one-line descriptions.

### Features
All datasets are summarized in a [table](/intrusion-detection-datasets/content/all_datasets), which lists some relevant information for each entry - helpful when you want to quickly determine which of them might me useful to you.

For every dataset, there is a separate entry (for example [this one](/intrusion-detection-datasets/content/datasets/ait_log_dataset)) describing the following characteristics of a given dataset:
- Overview (A general description of the dataset, giving a brief overview over origin, intended usage and some properties of the dataset)
- Environment (A description of the environment the dataset originated from, including networks, operating systems, running services, etc.)
- Activity (What kind of activity, benign and malicious, was performed during the period of data collection)
- Contained Data (What kind of data was collected and how it is present in the dataset, including any processing and labeling)

Additional information includes:
- Data examples wherever possible (i.e., not for binary data)
- A table summarizing all key characteristics of the dataset
- Related published papers
- Related links (homepages, download sources, documentation, etc.)

### Contributing
As there are certainly more than 43 IDS-adjacent datasets out there, any help in documenting them in the level of detail outlined above is more than welcome.
Alternatively, although I tried to be as thorough as possible during my research (while spending a reasonable amount of time per dataset), it is of course likely that I have missed some information, or made slight mistakes.
Any help in this regard, as in improving existing entries, is also much appreciated.
For more information, visit the [Contribution Guide](/intrusion-detection-datasets/content/contributing)
