---
title: Related Work
---

This page lists publications and other collections covering IDS datasets, sorted by their year of release.
Each entry consists of citation and a brief description of the surveys scope of selected datasets.
Additionally, for publications, all datasets contained in the survey are also listed, linking to their respective
entries on this website, if available.

Note that datasets are listed separately from collection, where a collection is any assembly of datasets that cannot
reasonably be grouped together by a common file type or scenario/origin, i.e., it cannot be adequately summarized in a
single entry on this website.

## Contents

- Publications
    - [Pillars of Sand: The current state of Datasets in the field of Network Intrusion Detection (2022)](#pillars-of-sand-the-current-state-of-datasets-in-the-field-of-network-intrusion-detection-2022)
    - [A Comprehensive Survey of Databases and Deep Learning Methods for Cybersecurity and Intrusion Detection Systems (2020)](#a-comprehensive-survey-of-databases-and-deep-learning-methods-for-cybersecurity-and-intrusion-detection-systems-2020)
    - [A Survey of Intrusion Detection Systems leveraging Host Data (2019)](#a-survey-of-intrusion-detection-systems-leveraging-host-data-2019)
    - [Survey of Intrusion Detection Systems: Techniques, Datasets and Challenges (2019)](#survey-of-intrusion-detection-systems-techniques-datasets-and-challenges-2019)
    - [Cybersecurity Research Datasets: Taxonomy and Empirical Analysis (2018)](#cybersecurity-research-datasets-taxonomy-and-empirical-analysis-2018)
    - [A Detail Analysis on Intrusion Detection Datasets (2014)](#a-detail-analysis-on-intrusion-detection-datasets-2014)
- Other collections
    - [Malware Traffic Analysis (2024)](#malware-traffic-analysis-2024)
    - [NETRESEC (2024)](#netresec-2024)
    - [Digital Corpora (2023)](#digital-corpora-2023)
    - [Awesome Cybersecurity Datasets (2021)](#awesome-cybersecurity-datasets-2021)
    - [IMPACT (2021)](#impact-2021)
    - [Public Security Log Sharing Site (2020)](#public-security-log-sharing-site-2010)
    - [The Honeynet Project Challenges (2015)](#the-honeynet-project-challenges-2015)
    - [SecRepo - Samples of Security Related Data (2010)](#secrepo---samples-of-security-related-data-2020)
    - [The Internet Traffic Archive (2008)](#the-internet-traffic-archive-2008)

## Publications

### Pillars of Sand: The current state of Datasets in the field of Network Intrusion Detection (2022)

```
Gints Engelen, Robert Flood, Lisa Liu, Vera Rimmer, Henry Clausen, David Aspinall, & Wouter Joosen. (2022). Pillars of Sand: The current state of Datasets in the field of Network Intrusion Detection. Zenodo. https://doi.org/10.5281/zenodo.7068716
```

An analysis of the five most commonly used datasets for anomaly-based NIDS evaluation, focusing on highlighting flaws
and errors within these datasets, and discussing the lack of variability in benign and malicious traffic.
They also offer an allegedly improved version of one of the surveyed datasets, CSE-CIC-IDS 2018.

Referenced datasets:

- [CIC-IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids2017)
- [CSE-CIC-IDS 2018](/intrusion-detection-datasets/content/datasets/cse_cic_ids2018)
- [UNSW NB15](/intrusion-detection-datasets/content/datasets/unsw_nb15)
- TON-IoT
- IoT-23

### A Comprehensive Survey of Databases and Deep Learning Methods for Cybersecurity and Intrusion Detection Systems (2020)

```
Gümüşbaş, D., Yıldırım, T., Genovese, A., & Scotti, F. (2020). A comprehensive survey of databases and deep learning methods for cybersecurity and intrusion detection systems. IEEE Systems Journal, 15(2), 1717-1731.
```

This survey focuses on machine learning methods for intrusion detection, especially those based on deep learning.
Alongside this, the authors present a list of datasets used to benchmark these approaches, which they categorize into
either host-based (system calls) or network-based (pcaps and NetFlows).
Each dataset is described in a couple of sentences, with the six most commonly used ones undergoing some more analysis
regarding properties like feature and sample count or attack types.

Referenced datasets:

- [ASNM CDX](/intrusion-detection-datasets/content/datasets/asnm_datasets)
- [CDX CTF 2009](/intrusion-detection-datasets/content/datasets/cdx_2009)
- [CIC-IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids2017)
- [CSE-CIC-IDS 2018](/intrusion-detection-datasets/content/datasets/cse_cic_ids2018)
- [CTU 13](/intrusion-detection-datasets/content/datasets/ctu_13)
- CIC DoS
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- Gure-KDD-Cup
- [ISCX IDS 2012](/intrusion-detection-datasets/content/datasets/iscx_ids_2012)
- ISOT
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [Kyoto Honeypot](/intrusion-detection-datasets/content/datasets/kyoto_honeypot)
- Lawrence Berkeley National Laboratory Traces
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)
- [Twente 2009](/intrusion-detection-datasets/content/datasets/twente_2009)
- [UNSW NB15](/intrusion-detection-datasets/content/datasets/unsw_nb15)
- Mentioned, but not further detailed:<br>Metrosec, UNIBS 2009, TUIDS, University of Napoli traffic dataset, CSIC 2010
  HTTP dataset, UNM system call dataset

Referenced collections:

- CAIDA
- DEFCON CTF Archive
- MAWILab
- UMass Trace Repository

### A Review of the Advancements in Intrusion Detection Datasets (2019)

```
Thakkar, A., & Lohiya, R. (2020). A review of the advancement in intrusion detection datasets. Procedia Computer Science, 167, 636-645.
```

This work focuses only on datasets used for the evaluation of network-based IDSs (mostly anomaly-based), presenting a
brief overview in the
form of feature count, attack types and one sentence of description.
It (very shortly) discusses some methods used in this field and goes into a bit more detail for two of the surveyed
datasets, CIC IDS 2017 and CSE CIC IDS 2018.
Strangely, it also includes some datasets that are not really network-related, like ADFA-LD.

Referenced datasets:

- [ADFA-LD](/intrusion-detection-datasets/content/datasets/adfa_ld), [ADFA-WD](/intrusion-detection-datasets/content/datasets/adfa_wd)
- [CDX CTF 2009](/intrusion-detection-datasets/content/datasets/cdx_2009)
- [CIC-IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids2017)
- [CSE-CIC-IDS 2018](/intrusion-detection-datasets/content/datasets/cse_cic_ids2018)
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- [ISCX IDS 2012](/intrusion-detection-datasets/content/datasets/iscx_ids_2012)
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [Kyoto Honeypot](/intrusion-detection-datasets/content/datasets/kyoto_honeypot)
- Lawrence Berkeley National Laboratory Traces
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)
- [Twente 2009](/intrusion-detection-datasets/content/datasets/twente_2009)

Referenced Collections:

- CAIDA
- DEFCON CTF Archive

### A Survey of Intrusion Detection Systems leveraging Host Data (2019)

```
Bridges, R. A., Glass-Vanderlan, T. R., Iannacone, M. D., Vincent, M. S., & Chen, Q. (2019). A survey of intrusion detection systems leveraging host data. ACM Computing Surveys (CSUR), 52(6), 1-35.
```

This survey focuses on host based IDSs designed to detect attacks on enterprise networks, dividing them into categories
based on their approach.
In addition to this, it provides an overview of several existing datasets and collections of datasets to "accommodate
current researchers", describing each of them briefly.
Surprisingly, it also features datasets like KDD and NSL KDD, which positively do not feature any host data.

Referenced datasets:

- Active DNS Project
- [ADFA-LD](/intrusion-detection-datasets/content/datasets/adfa_ld), [ADFA-WD](/intrusion-detection-datasets/content/datasets/adfa_wd)
- [Comprehensive Multi-Source Cybersecurity Events](/intrusion-detection-datasets/content/datasets/comp_multi_source_cybersec_events)
- [CTU 13](/intrusion-detection-datasets/content/datasets/ctu_13)
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- GURE-KDD
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- Malware Capture Facility Project
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)
- UNM system call dataset
- [Unified Host and Network dataset](/intrusion-detection-datasets/content/datasets/unified_host_and_network_dataset)
- [UNSW-NB15](/intrusion-detection-datasets/content/datasets/unsw_nb15)
- User-Computer Authentication Associations in Time
- [Vast Challenge 2012]((/intrusion-detection-datasets/content/datasets/vast_2012))
- Vast Challenge 2013

Referenced collections:

- CAIDA
- [Digital Corpora Database](#digital-corpora-2023)
- [IMPACT](#impact-2021)
- [Malware Traffic Analysis](#malware-traffic-analysis-2024)
- [NETRESEC](#netresec-2024)
- [SecRepo](#secrepo---samples-of-security-related-data-2020)
- [The Honeypot Project](#the-honeynet-project)

### A Survey of Network-based Intrusion Detection Data Sets

```
Ring, M., Wunderlich, S., Scheuring, D., Landes, D., & Hotho, A. (2019). A survey of network-based intrusion detection data sets. Computers & Security, 86, 147-167.
```

This survey focuses on datasets used for the evaluation of anomaly-based.
It does so by first defining 15 different properties to describe, such as year of creation, format, duration, or type of
network, and then applying this methodology to 32 network datasets, along with a short description for each one.
Additionally, several existing collections of datasets are listed.

Referenced datasets:

- AWID
- Booters Dataset
- ISCX Botnet 2014
- [CDX CTF 2009](/intrusion-detection-datasets/content/datasets/cdx_2009)
- CIC DoS
- [CIC-IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids2017)
- CIDDS-001 & 002
- [CSE-CIC-IDS 2018](/intrusion-detection-datasets/content/datasets/cse_cic_ids2018)
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- DDoS 2016
- IRSC
- [ISCX IDS 2012](/intrusion-detection-datasets/content/datasets/iscx_ids_2012)
- ISOT
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- Kent 2016
- [Kyoto Honeypot](/intrusion-detection-datasets/content/datasets/kyoto_honeypot)
- Lawrence Berkeley National Laboratory Traces
- NDSec-1
- [NGIDS-DS](/intrusion-detection-datasets/content/datasets/ngids_dataset)
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)
- PU-IDS
- PUF
- SANTA
- SSENET 2011
- SSENET 2014
- SSHCure
- TRAbID
- TUIDS
- [Twente 2009](/intrusion-detection-datasets/content/datasets/twente_2009)
- UNIBS
- [Unified Host and Network dataset](/intrusion-detection-datasets/content/datasets/unified_host_and_network_dataset)
- [UNSW-NB15](/intrusion-detection-datasets/content/datasets/unsw_nb15)

Referenced collections:

- AZSecure
- CAIDA
- Contagiodump
- covert.io
- DEFCON CTF archive
- [IMPACT](#impact-2021)
- [Internet Traffic Archive](#the-internet-traffic-archive-2008)
- Kaggle
- [Malware Traffic Analysis](#malware-traffic-analysis-2024)
- Mid-Atlantic CCDC
- MAWILab
- [NETRESEC](#netresec-2024)
- OpenML
- RIPE Data Repository
- [SecRepo](#secrepo---samples-of-security-related-data-2020)
- Simple Web
- UMass Trace Repository
- Vast Challenges
- Waikato Internet Traffic Storage

### Survey of Intrusion Detection Systems: Techniques, Datasets and Challenges (2019)

```
Khraisat, A., Gondal, I., Vamplew, P., & Kamruzzaman, J. (2019). Survey of intrusion detection systems: techniques, datasets and challenges. Cybersecurity, 2(1), 1-22.
```

Mainly focuses on commonly used detection methodology (especially anomaly-based), but also shortly describes eight
datasets commonly used to evaluate these approaches.

Referenced datasets:

- [ADFA-LD](/intrusion-detection-datasets/content/datasets/adfa_ld), [ADFA-WD](/intrusion-detection-datasets/content/datasets/adfa_wd)
- [CIC IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids_2017)
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- [ISCX IDS 2012](/intrusion-detection-datasets/content/datasets/iscx_ids_2012)
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)

Referenced collections:

- CAIDA

### Cybersecurity Research Datasets: Taxonomy and Empirical Analysis (2018)

```
Zheng, M., Robbins, H., Chai, Z., Thapa, P., & Moore, T. (2018). Cybersecurity research datasets: taxonomy and empirical analysis. In 11th USENIX Workshop on Cyber Security Experimentation and Test (CSET 18).
```

Tries to construct a taxonomy of the types of created and shared cybersecurity data(sets) by inspecting 965 related
papers.
Does not provide an actual list, rather aims to describe general observations, like the fact that only 6% of the
surveyed papers created a dataset *and* made it publicly available.

### A Detail Analysis on Intrusion Detection Datasets (2014)

```
Sahu, S. K., Sarangi, S., & Jena, S. K. (2014, February). A detail analysis on intrusion detection datasets. In 2014 ieee international advance computing conference (IACC) (pp. 1348-1353). IEEE.
```

This paper shortly analyzed three papers the authors deem suitable to test their novel preprocessing techniques,
which are supposed to improve the performance of various data mining algorithms.

Referenced datasets:

- GURE-KDD
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)

## Other collections

`Last updated` refers to the last time a new entry was added to the collection.

### Malware Traffic Analysis (2024)

```
https://www.netresec.com/?page=PcapFiles
(accessed 19.02.2024, last updated 14.02.2024)
```

Various pcaps and malware samples stemming from individual campaigns or attack instances, but without any overall
categorization or even overview.
They are available as blog posts named something like "DarkGate activity" or "GootLoader Infection", which each one
listing some references and download links to any relevant files.

### NETRESEC (2024)

```
https://www.netresec.com/?page=PcapFiles
(accessed 19.02.2024, last updated 04.01.2024)
```

A large collection of pcap files and other repositories which are hosting pcaps themselves.
They are categorized into CDX, Malware Traffic, Network Forensics, SCADA/ICS, CTF, Packet Injection/Man-on-the-Side, and
Uncategorized.

### Digital Corpora (2023)

```
https://digitalcorpora.org/
(accessed 19.02.2024, last updated 05.05.2023)
```

A collection of datasets mostly designed for the use in forensics education.
It consists of various disk images, memory dumps and pcaps, as well as a bunch of benign and malicious files.
It does not seem to contain actual log data.

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

### IMPACT (2021)

```
https://www.impactcybertrust.org/search
(accessed 19.02.2024, last updated 13.07.2021)
```

The "Information Marketplace for Policy and Analysis of Cyber-Risk and Trust" (IMPACT, formerly PREDICT), maintained by
the US Department of Homeland Security, contains 70 datasets.
These are for the mostly made up of network related files (pcaps and DNS logs) from a wide variety of scenarios (CTF
events, IoT, corpo networks, etc.), as well as some miscellaneous things like network shapefiles.
55 of these datasets were created by IMPACT, 15 are external (mostly CAIDA). Many datasets require prior authorization
to access them.

### SecRepo - Samples of Security Related Data (2020)

```
https://www.secrepo.com/
(accessed 18.02.2024, last updated 01.10.2020)
```

An individuals effort to "keep a somewhat curated list of Security related data I've found, created, or was pointed to".
It contains several entries of the authors own creation, some of which are described in a bit more detail, as well as
121 "3rd party" entries from a broad range of topics, each described in a single sentence.
Some of them are usable for IDS related purposes.

### The Honeynet Project Challenges (2015)

```
https://www.honeynet.org/challenges/
(accessed 19.02.2024, last updated 18.03.2015)
```

A collection of 14 forensic challenges related to pcaps, malware and log files.
However, most resources, except for the two newest challenges, are no longer available.

### Public Security Log Sharing Site (2010)

```
https://log-sharing.dreamhosters.com/
(accessed 18.02.2024, last updated 11.08.2010)
```

A collection which started as an effort to collect various log samples, but seems to have been discontinued after
operating for about one year.
Currently, it consists of nine entries containing Linux syslogs, firewall logs, apache logs, and web proxy logs.

### The Internet Traffic Archive (2008)

```
https://ita.ee.lbl.gov/
(accessed 18.02.2024, last updated 11.08.2010)
```

An archive hosting 16 different network data from various sources, such as WWW servers, web clients, and some custom
networks.
Most data is in the form of traces, some include http logs or traceroute measurements.