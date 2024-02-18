---
title: Related Work
---

This page lists publications and other collections covering IDS datasets, sorted by their year of release.
Each entry consists of citation and a brief description of the surveys scope of selected datasets.
Additionally, for publications, all datasets contained in the survey are also listed, linking to their respective
entries on this website, if available.

## Contents

- Publications
    - [A Comprehensive Survey of Databases and Deep Learning Methods for Cybersecurity and Intrusion Detection Systems (2020)](#a-comprehensive-survey-of-databases-and-deep-learning-methods-for-cybersecurity-and-intrusion-detection-systems-2020)
    - [Pillars of Sand: The current state of Datasets in the field of Network Intrusion Detection (2022)](#pillars-of-sand-the-current-state-of-datasets-in-the-field-of-network-intrusion-detection-2022)
    - [Survey of Intrusion Detection Systems: Techniques, Datasets and Challenges (2019)](#survey-of-intrusion-detection-systems-techniques-datasets-and-challenges-2019)
- Other collections
    - [Awesome Cybersecurity Datasets (2021)](#awesome-cybersecurity-datasets-2021)
    - [Public Security Log Sharing Site](#public-security-log-sharing-site-2010)
    - [SecRepo - Samples of Security Related Data](#secrepo---samples-of-security-related-data-2020)

## Publications

### A Comprehensive Survey of Databases and Deep Learning Methods for Cybersecurity and Intrusion Detection Systems (2020)

```
Gümüşbaş, D., Yıldırım, T., Genovese, A., & Scotti, F. (2020). A comprehensive survey of databases and deep learning methods for cybersecurity and intrusion detection systems. IEEE Systems Journal, 15(2), 1717-1731.
```

This survey focuses on machine learning methods for intrusion detection, especially those based on deep learning.
Alongside this, the authors present a list of datasets used to benchmark these approaches, which they categorize into
either host-based (system calls) or network-based (pcaps and NetFlows).
Each dataset is described in a couple of sentences, with the six most commonly used ones undergoing some more analysis
regarding properties like feature and sample count or attack types.

- [ASNM CDX](/intrusion-detection-datasets/content/datasets/asnm_datasets)
- CAIDA
- [CDX CTF 2009](/intrusion-detection-datasets/content/datasets/cdx_2009)
- [CIC-IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids2017)
- [CSE-CIC-IDS 2018](/intrusion-detection-datasets/content/datasets/cse_cic_ids2018)
- [CTU 13](/intrusion-detection-datasets/content/datasets/ctu_13)
- CIC DoS
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- DEFCON
- Gure-KDD-Cup
- [ISCX IDS 2012](/intrusion-detection-datasets/content/datasets/iscx_ids_2012)
- ISOT
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [Kyoto Honeypot](/intrusion-detection-datasets/content/datasets/kyoto_honeypot)
- Lawrence Berkeley National Laboratory
- MAWI
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)
- [Twente 2009](/intrusion-detection-datasets/content/datasets/twente_2009)
- UMass
- [UNSW NB15](/intrusion-detection-datasets/content/datasets/unsw_nb15)
- Mentioned, but not further detailed:<br>Metrosec, UNIBS 2009, TUIDS, University of Napoli traffic dataset, CSIC 2010
  HTTP
  dataset, UNM system call dataset

### Pillars of Sand: The current state of Datasets in the field of Network Intrusion Detection (2022)

```
Gints Engelen, Robert Flood, Lisa Liu, Vera Rimmer, Henry Clausen, David Aspinall, & Wouter Joosen. (2022). Pillars of Sand: The current state of Datasets in the field of Network Intrusion Detection. Zenodo. https://doi.org/10.5281/zenodo.7068716
```

An analysis of the five most commonly used datasets for anomaly-based NIDS evaluation, focusing on highlighting flaws
and errors within these datasets, and discussing the lack of variability in benign and malicious traffic.
They also offer an allegedly improved version of one of the surveyed datasets, CSE-CIC-IDS 2018.

- [CIC-IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids2017)
- [CSE-CIC-IDS 2018](/intrusion-detection-datasets/content/datasets/cse_cic_ids2018)
- [UNSW NB15](/intrusion-detection-datasets/content/datasets/unsw_nb15)
- TON-IoT
- IoT-23

### Survey of Intrusion Detection Systems: Techniques, Datasets and Challenges (2019)

```
Khraisat, A., Gondal, I., Vamplew, P., & Kamruzzaman, J. (2019). Survey of intrusion detection systems: techniques, datasets and challenges. Cybersecurity, 2(1), 1-22.
```

Mainly focuses on commonly used detection methodology (especially anomaly-based), but also shortly describes eight
datasets commonly used to evaluate these approaches.

- [ADFA-LD](/intrusion-detection-datasets/content/datasets/adfa_ld)
- [ADFA-WD](/intrusion-detection-datasets/content/datasets/adfa_wd)
- CAIDA
- [CIC IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids_2017)
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- [ISCX IDS 2012](/intrusion-detection-datasets/content/datasets/iscx_ids_2012)
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)

### Cybersecurity Research Datasets: Taxonomy and Empirical Analysis

```
Zheng, M., Robbins, H., Chai, Z., Thapa, P., & Moore, T. (2018). Cybersecurity research datasets: taxonomy and empirical analysis. In 11th USENIX Workshop on Cyber Security Experimentation and Test (CSET 18).
```

Tries to construct a taxonomy of the types of created and shared cybersecurity data(sets) by inspecting 965 related
papers.
Does not provide an actual list, rather aims to describe general observations, like the fact that only 6% of the
surveyed papers created a dataset *and* made it publicly available.

## Other collections

### Awesome Cybersecurity Datasets (2021)

```
https://github.com/shramos/Awesome-Cybersecurity-Datasets
(accessed 18.02.2024, last updated 23.01.2021)
```

A "curated" personal collection of various cybersecurity-related datasets or collections, grouped into several
categories such as "Network", "Software" or "Fraud".
Each entry is described in only one or two sentences, and most datasets are not, or only partially, suitable for IDS
research.
The list is somewhat deprecated and does especially lack meaningful host-based datasets.

### SecRepo - Samples of Security Related Data (2020)

```
https://www.secrepo.com/
(accessed 18.02.2024, last updated 01.10.2020)
```

An individuals effort to "keep a somewhat curated list of Security related data I've found, created, or was pointed to".
It contains several entries of the authors own creation, some of which are described in a bit more detail, as well as 
121 "3rd party" entries from a broad range of topics, each described in a single sentence.
Some of them are usable for IDS related purposes.

### Public Security Log Sharing Site (2010)

```
https://log-sharing.dreamhosters.com/
(accessed 18.02.2024, last updated 11.08.2010)
```

A collection which started as an effort to collect various log samples, but seems to have been discontinued after
operating for about one year.
Currently, it consists of nine entries containing Linux syslogs, firewall logs, apache logs, and web proxy logs.