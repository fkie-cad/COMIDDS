---
title: Related Work
---

The following is a (non-exhaustive) list of publications and collections covering IDS datasets.
Related publications, sorted by year of release, are any academic work that at least partially covers the topic of available IDS datasets.
Collections, sorted alphabetically, simply features agglomerations of IDS-related datasets not backed by a scientific publication.

Each entry consists of a citation and a brief description of the survey's scope of selected datasets.
Additionally, for publications, all datasets discussed in the survey are also listed, linking to their respective entries on this website, if available.

## Contents

- Publications
    - [A systematic literature review of methods and datasets for anomaly-based network intrusion detection (2022)](#a-systematic-literature-review-of-methods-and-datasets-for-anomaly-based-network-intrusion-detection-2022)
    - [Pillars of Sand: The current state of Datasets in the field of Network Intrusion Detection (2022)](#pillars-of-sand-the-current-state-of-datasets-in-the-field-of-network-intrusion-detection-2022)
    - [A Comprehensive Survey of Databases and Deep Learning Methods for Cybersecurity and Intrusion Detection Systems (2020)](#a-comprehensive-survey-of-databases-and-deep-learning-methods-for-cybersecurity-and-intrusion-detection-systems-2020)
    - [Are Public Intrusion Datasets Fit for Purpose Characterising the State of the Art in Intrusion Event Datasets (2020)](#are-public-intrusion-datasets-fit-for-purpose-characterising-the-state-of-the-art-in-intrusion-event-datasets-2020)
    - [A Review of the Advancements in Intrusion Detection Datasets (2019)](#a-review-of-the-advancements-in-intrusion-detection-datasets-2019)
    - [A Survey of Intrusion Detection Systems leveraging Host Data (2019)](#a-survey-of-intrusion-detection-systems-leveraging-host-data-2019)
    - [A Survey of Network-based Intrusion Detection Data Sets (2019)](#a-survey-of-network-based-intrusion-detection-data-sets-2019)
    - [Survey of Intrusion Detection Systems: Techniques, Datasets and Challenges (2019)](#survey-of-intrusion-detection-systems-techniques-datasets-and-challenges-2019)
    - [Cybersecurity Research Datasets: Taxonomy and Empirical Analysis (2018)](#cybersecurity-research-datasets-taxonomy-and-empirical-analysis-2018)
    - [A survey of deep learning-based network anomaly detection (2017)](#a-survey-of-deep-learning-based-network-anomaly-detection-2017)
    - [A Survey of Data Mining and Machine Learning Methods for Cyber Security Intrusion Detection (2015)](#a-survey-of-data-mining-and-machine-learning-methods-for-cyber-security-intrusion-detection-2015)
    - [A Detail Analysis on Intrusion Detection Datasets (2014)](#a-detail-analysis-on-intrusion-detection-datasets-2014)
    - [Network anomaly detection: Methods, systems and tools (2013)](#network-anomaly-detection-methods-systems-and-tools-2013)
- Other collections
    - [Awesome Cybersecurity Datasets](#awesome-cybersecurity-datasets)
    - [Digital Corpora](#digital-corpora)
    - [IMPACT](#impact)
    - [Malware Traffic Analysis](#malware-traffic-analysis)
    - [NETRESEC](#netresec)
    - [Public Security Log Sharing Site](#public-security-log-sharing-site)
    - [SecRepo - Samples of Security Related Data](#secrepo---samples-of-security-related-data)
    - [The Honeynet Project Challenges](#the-honeynet-project-challenges)
    - [The Internet Traffic Archive](#the-internet-traffic-archive)

## Publications

### A systematic literature review of methods and datasets for anomaly-based network intrusion detection (2022)

[Link to Paper](https://doi.org/10.1016/j.cose.2022.102675)
```
Yang, Z., Liu, X., Li, T., Wu, D., Wang, J., Zhao, Y., & Han, H. (2022). A systematic literature review of methods and datasets for anomaly-based network intrusion detection. Computers & Security, 116, 102675.
```
An extensive survey covering a broad range of publications (119 in total) and topics related to anomaly-based network intrusion detection systems, ranging from data preprocessing over evaluation metrics to, relevant here, datasets.
While it is one of the more comprehensive surveys in this regard, listing over 52 datasets and collections, there is very little information provided for each of them.
Every entry is described with four properties (real/emulated, event count, label existence and number of labels), along with a few sentences outlining some additional details, though in no particular order or consistent manner.
While significant in scope (though not complete), the provided coverage of dataset is negligible, i.e., there is no further analysis or conclusion on the basis of the surveyed datasets.

Referenced datasets:
- [ADFA-LD](/intrusion-detection-datasets/content/datasets/adfa_ld)
- [AWID](/intrusion-detection-datasets/content/datasets/awid)
- BoT-IoT
- Botnet 2014
- CDMX 2016
- [CDX CTF 2009](/intrusion-detection-datasets/content/datasets/cdx_2009)
- [CIC DoS](/intrusion-detection-datasets/content/datasets/cic_dos)
- [CIC-IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids2017)
- CIDDS
- CIRA-CIC-DoHBrw 2020
- CSIC 2010 HTTP Dataset
- [CTU 13](/intrusion-detection-datasets/content/datasets/ctu_13)
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- DARPA 1999
- DARPA 2000
- DDoS 2016
- ICML-09
- InSDN
- IoT-23
- IRSC
- [ISCX IDS 2012](/intrusion-detection-datasets/content/datasets/iscx_ids_2012)
- ISOT
- ISOT CID
- [ISOT Botnet](/intrusion-detection-datasets/content/datasets/isot_botnet)
- ISTS-12
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- Kharon
- [Kyoto Honeypot](/intrusion-detection-datasets/content/datasets/kyoto_honeypot)
- LDID
- NCCDC
- NDSec-1
- [NGIDS-DS](/intrusion-detection-datasets/content/datasets/ngids_dataset)
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)
- OPCUA
- PUF
- SANTA
- SSENET 2011
- SSENET 2014
- SSHCure
- SUEEE 2017
- TRAbID
- [Twente 2009](/intrusion-detection-datasets/content/datasets/twente_2009)
- UCSD
- [UGR'16](/intrusion-detection-datasets/content/datasets/ugr16)
- [Unified Host and Network dataset](/intrusion-detection-datasets/content/datasets/unified_host_and_network_dataset)
- [UNSW-NB15](/intrusion-detection-datasets/content/datasets/unsw_nb15)
- Witty Worm

Referenced collections:
- CAIDA
- DEFCON CTF Archive
- MAWILab

### Pillars of Sand: The current state of Datasets in the field of Network Intrusion Detection (2022)

[Link to Paper](https://doi.org/10.5281/zenodo.7068716)
```
Gints Engelen, Robert Flood, Lisa Liu, Vera Rimmer, Henry Clausen, David Aspinall, & Wouter Joosen. (2022). Pillars of Sand: The current state of Datasets in the field of Network Intrusion Detection. Zenodo. https://doi.org/10.5281/zenodo.7068716
```

An analysis of the five most commonly used datasets for anomaly-based NIDS evaluation, focusing on highlighting flaws and errors within these datasets, and discussing the lack of variability in benign and malicious traffic.
They also offer an allegedly improved version of one of the surveyed datasets, CSE-CIC-IDS 2018.

Referenced datasets:
- [CIC-IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids2017)
- [CSE-CIC-IDS 2018](/intrusion-detection-datasets/content/datasets/cse_cic_ids2018)
- [UNSW NB15](/intrusion-detection-datasets/content/datasets/unsw_nb15)
- TON-IoT
- IoT-23

### A Comprehensive Survey of Databases and Deep Learning Methods for Cybersecurity and Intrusion Detection Systems (2020)

[Link to Paper](https://doi.org/10.1109/JSYST.2020.2992966)
```
Gümüşbaş, D., Yıldırım, T., Genovese, A., & Scotti, F. (2020). A comprehensive survey of databases and deep learning methods for cybersecurity and intrusion detection systems. IEEE Systems Journal, 15(2), 1717-1731.
```

This survey focuses on machine learning methods for intrusion detection, especially those based on deep learning.
Alongside this, the authors present a list of datasets used to benchmark these approaches, which they categorize into either host-based (system calls) or network-based (pcaps and NetFlows).
Each dataset is described in a couple of sentences, with the six most commonly used ones undergoing some more analysis regarding properties like feature and sample count or attack types.

Referenced datasets:
- [ASNM CDX](/intrusion-detection-datasets/content/datasets/asnm_datasets)
- [CDX CTF 2009](/intrusion-detection-datasets/content/datasets/cdx_2009)
- [CIC-IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids2017)
- [CSE-CIC-IDS 2018](/intrusion-detection-datasets/content/datasets/cse_cic_ids2018)
- [CTU 13](/intrusion-detection-datasets/content/datasets/ctu_13)
- [CIC DoS](/intrusion-detection-datasets/content/datasets/cic_dos)
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- [gureKDDCup](/intrusion-detection-datasets/content/datasets/gure_kddcup)
- [ISCX IDS 2012](/intrusion-detection-datasets/content/datasets/iscx_ids_2012)
- [ISOT Botnet](/intrusion-detection-datasets/content/datasets/isot_botnet)
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [Kyoto Honeypot](/intrusion-detection-datasets/content/datasets/kyoto_honeypot)
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)
- [Twente 2009](/intrusion-detection-datasets/content/datasets/twente_2009)
- [UNSW NB15](/intrusion-detection-datasets/content/datasets/unsw_nb15)
- Mentioned, but not further detailed:<br>Metrosec, [UNIBS](/intrusion-detection-datasets/content/datasets/unibs), [TUIDS](/intrusion-detection-datasets/content/datasets/tuids), University of Napoli traffic dataset, CSIC 2010 HTTP dataset, UNM system call dataset

Referenced collections:
- CAIDA
- DEFCON CTF Archive
- [Lawrence Berkeley National Laboratory Traces](#the-internet-traffic-archive) (alias for: The Internet Traffic Archive)
- MAWILab
- UMass Trace Repository


### Are Public Intrusion Datasets Fit for Purpose Characterising the State of the Art in Intrusion Event Datasets (2020)

[Link to Paper](https://doi.org/10.1016/j.cose.2020.102022)
```
Kenyon, A., Deka, L., & Elizondo, D. (2020). Are public intrusion datasets fit for purpose characterising the state of the art in intrusion event datasets. Computers & Security, 99, 102022.
```

The authors focus on analysing the - according to them - most widely used  public intrusion datasets, also noting that their relative scarcity is compounded by the lack of central registry of some sort.
To alleviate this problem, and to investigate the current state of the art, they study 25 datasets as well as three collections, providing a small set of features (origin, anonymization, labeling, flow availability, attack types) and a description for each.
They also enumerate a number of characteristic a dataset should fulfil in order to be suitable for IDS research, and conclude that, at the time of writing, there is no such dataset.
However, the MAWI and CAIDA collection as well as the ISCX IDS 2012, CIC-IDS 2017 and CSE-CIC-IDS 2018 datasets are highlighted, as they fulfill at least most of the aforementioned characteristics.

Referenced datasets:
- [ADFA-LD](/intrusion-detection-datasets/content/datasets/adfa_ld), [ADFA-WD](/intrusion-detection-datasets/content/datasets/adfa_wd)
- [AWID](/intrusion-detection-datasets/content/datasets/awid)
- [CDX CTF 2009](/intrusion-detection-datasets/content/datasets/cdx_2009)
- CERT ITTD
- [CIC-IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids2017)
- [CSE-CIC-IDS 2018](/intrusion-detection-datasets/content/datasets/cse_cic_ids2018)
- [CIDD](/intrusion-detection-datasets/content/datasets/cidd)
- CIDDS
- CSIC HTTP 
- [CTU-13](/intrusion-detection-datasets/content/datasets/ctu_13)
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- ICS 2014
- [ISCX IDS 2012](/intrusion-detection-datasets/content/datasets/iscx_ids_2012)
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [Kyoto Honeypot](/intrusion-detection-datasets/content/datasets/kyoto_honeypot)
- LANL (by which the authors mean the following three datasets)
  - [Comprehensive Multi-Source Cybersecurity Events](/intrusion-detection-datasets/content/datasets/comp_multi_source_cybersec_events)
  - [Unified Host and Network dataset](/intrusion-detection-datasets/content/datasets/unified_host_and_network_dataset)
  - [User-Computer Authentication Associations in Time](/intrusion-detection-datasets/content/datasets/user_computer_associations)
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)
- UCKA-CSD
- [UNSW NB15](/intrusion-detection-datasets/content/datasets/unsw_nb15)
- RUU
- SEA
- [Twente 2009](/intrusion-detection-datasets/content/datasets/twente_2009)


Referenced collections:
- DEFCON CTF Archive
- [Lawrence Berkeley National Laboratory Traces](#the-internet-traffic-archive) (alias for: The Internet Traffic Archive)
- MAWI
- UMASS

### A Review of the Advancements in Intrusion Detection Datasets (2019)

[Link to Paper](http://dx.doi.org/10.1016/j.procs.2020.03.330)
```
Thakkar, A., & Lohiya, R. (2020). A review of the advancement in intrusion detection datasets. Procedia Computer Science, 167, 636-645.
```

This work focuses only on datasets used for the evaluation of network-based IDSs (mostly anomaly-based), presenting a brief overview in the form of feature count, attack types and one sentence of description.
It (very shortly) discusses some methods used in this field and goes into a bit more detail for two of the surveyed datasets, CIC IDS 2017 and CSE CIC IDS 2018.
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
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)
- [Twente 2009](/intrusion-detection-datasets/content/datasets/twente_2009)

Referenced Collections:
- CAIDA
- [Lawrence Berkeley National Laboratory Traces](#the-internet-traffic-archive) (alias for: The Internet Traffic Archive)
- DEFCON CTF Archive

### A Survey of Intrusion Detection Systems leveraging Host Data (2019)

[Link to Paper](https://doi.org/10.1145/3344382)
```
Bridges, R. A., Glass-Vanderlan, T. R., Iannacone, M. D., Vincent, M. S., & Chen, Q. (2019). A survey of intrusion detection systems leveraging host data. ACM Computing Surveys (CSUR), 52(6), 1-35.
```

This survey focuses on host based IDSs designed to detect attacks on enterprise networks, dividing them into categories based on their approach.
In addition to this, it provides an overview of several existing datasets and collections of datasets to "accommodate current researchers", describing each of them briefly.
Surprisingly, it also features datasets like KDD and NSL KDD, which positively do not feature any host data.

Referenced datasets:
- Active DNS Project
- [ADFA-LD](/intrusion-detection-datasets/content/datasets/adfa_ld), [ADFA-WD](/intrusion-detection-datasets/content/datasets/adfa_wd)
- [Comprehensive Multi-Source Cybersecurity Events](/intrusion-detection-datasets/content/datasets/comp_multi_source_cybersec_events)
- [CTU-13](/intrusion-detection-datasets/content/datasets/ctu_13)
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- [gureKDDCup](/intrusion-detection-datasets/content/datasets/gure_kddcup)
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [Malware Capture Facility Project](/intrusion-detection-datasets/content/datasets/ctu_13) (alias for: CTU 13)
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)
- UNM system call dataset
- [Unified Host and Network dataset](/intrusion-detection-datasets/content/datasets/unified_host_and_network_dataset)
- [UNSW-NB15](/intrusion-detection-datasets/content/datasets/unsw_nb15)
- [User-Computer Authentication Associations in Time](/intrusion-detection-datasets/content/datasets/user_computer_associations)
- [Vast Challenge 2012]((/intrusion-detection-datasets/content/datasets/vast_2012))
- Vast Challenge 2013

Referenced collections:
- CAIDA
- [Digital Corpora Database](#digital-corpora)
- [IMPACT](#impact)
- [Malware Traffic Analysis](#malware-traffic-analysis)
- [NETRESEC](#netresec)
- [SecRepo](#secrepo---samples-of-security-related-data)
- [The Honeypot Project](#the-honeynet-project-challenges)

### A Survey of Network-based Intrusion Detection Data Sets (2019)

[Link to Paper](https://doi.org/10.1016/j.cose.2019.06.005)
```
Ring, M., Wunderlich, S., Scheuring, D., Landes, D., & Hotho, A. (2019). A survey of network-based intrusion detection data sets. Computers & Security, 86, 147-167.
```

This survey focuses on datasets used for the evaluation of anomaly-based.
It does so by first defining 15 different properties to describe, such as year of creation, format, duration, or type of network, and then applying this methodology to 32 network datasets, along with a short description for each one.
Additionally, several existing collections of datasets are listed.

Referenced datasets:
- [AWID](/intrusion-detection-datasets/content/datasets/awid)
- Booters Dataset
- ISCX Botnet 2014
- [CDX CTF 2009](/intrusion-detection-datasets/content/datasets/cdx_2009)
- [CIC DoS](/intrusion-detection-datasets/content/datasets/cic_dos)
- [CIC-IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids2017)
- CIDDS-001 & 002
- [CSE-CIC-IDS 2018](/intrusion-detection-datasets/content/datasets/cse_cic_ids2018)
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- DDoS 2016
- IRSC
- [ISCX IDS 2012](/intrusion-detection-datasets/content/datasets/iscx_ids_2012)
- [ISOT Botnet](/intrusion-detection-datasets/content/datasets/isot_botnet)
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [Kent 2016](/intrusion-detection-datasets/content/datasets/comp_multi_source_cybersec_events) (alias for: Comprehensive, Multi-Source Cybersecurity Events)
- [Kyoto Honeypot](/intrusion-detection-datasets/content/datasets/kyoto_honeypot)
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
- [TUIDS](/intrusion-detection-datasets/content/datasets/tuids)
- [Twente 2009](/intrusion-detection-datasets/content/datasets/twente_2009)
- [UNIBS](/intrusion-detection-datasets/content/datasets/unibs)
- [Unified Host and Network dataset](/intrusion-detection-datasets/content/datasets/unified_host_and_network_dataset)
- [UNSW-NB15](/intrusion-detection-datasets/content/datasets/unsw_nb15)

Referenced collections:
- AZSecure
- CAIDA
- Contagiodump
- covert.io
- DEFCON CTF archive
- [IMPACT](#impact)
- [Internet Traffic Archive](#the-internet-traffic-archive)
- Kaggle
- [Lawrence Berkeley National Laboratory Traces](#the-internet-traffic-archive) (alias for: The Internet Traffic Archive)
- [Malware Traffic Analysis](#malware-traffic-analysis)
- Mid-Atlantic CCDC
- MAWILab
- [NETRESEC](#netresec)
- OpenML
- RIPE Data Repository
- [SecRepo](#secrepo---samples-of-security-related-data)
- Simple Web
- UMass Trace Repository
- Vast Challenges
- Waikato Internet Traffic Storage

### Survey of Intrusion Detection Systems: Techniques, Datasets and Challenges (2019)

[Link to Paper](https://doi.org/10.1186/s42400-019-0038-7)
```
Khraisat, A., Gondal, I., Vamplew, P., & Kamruzzaman, J. (2019). Survey of intrusion detection systems: techniques, datasets and challenges. Cybersecurity, 2(1), 1-22.
```

Mainly focuses on commonly used detection methodology (especially anomaly-based), but also shortly describes eight datasets commonly used to evaluate these approaches.

Referenced datasets:
- [ADFA-LD](/intrusion-detection-datasets/content/datasets/adfa_ld), [ADFA-WD](/intrusion-detection-datasets/content/datasets/adfa_wd)
- [CIC IDS 2017](/intrusion-detection-datasets/content/datasets/cic_ids_2017)
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- [ISCX IDS 2012](/intrusion-detection-datasets/content/datasets/iscx_ids_2012)
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)
- [UNIBS](/intrusion-detection-datasets/content/datasets/unibs)

Referenced collections:
- CAIDA

### Cybersecurity Research Datasets: Taxonomy and Empirical Analysis (2018)

[Link to Paper](https://www.usenix.org/conference/cset18/presentation/zheng)
```
Zheng, M., Robbins, H., Chai, Z., Thapa, P., & Moore, T. (2018). Cybersecurity research datasets: taxonomy and empirical analysis. In 11th USENIX Workshop on Cyber Security Experimentation and Test (CSET 18).
```

Tries to construct a taxonomy of the types of created and shared cybersecurity data(sets) by inspecting 965 related papers.
Does not provide an actual list, rather aims to describe general observations, like the fact that only 6% of the surveyed papers created a dataset
*and* made it publicly available.

### A survey of deep learning-based network anomaly detection (2017)

[Link to Paper](https://doi.org/10.1007/s10586-017-1117-8)
```
Kwon, D., Kim, H., Kim, J., Suh, S. C., Kim, I., & Kim, K. J. (2019). A survey of deep learning-based network anomaly detection. Cluster Computing, 22, 949-961.
```

This survey features various deep learning approaches in the field of anomaly-based intrusion detections.
Datasets, while acknowledged as an important factor, are only described in one section.
Weirdly, the two chosen datasets are quite out-of-date for a survey that has been published in 2017.

Referenced datasets:
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)

### A Survey of Data Mining and Machine Learning Methods for Cyber Security Intrusion Detection (2015)

[Link to Paper](https://doi.org/10.1109/COMST.2015.2494502)
```
Buczak, A. L., & Guven, E. (2015). A survey of data mining and machine learning methods for cyber security intrusion detection. IEEE Communications surveys & tutorials, 18(2), 1153-1176.
```

This survey only considers machine learning and datamining (i.e., anomaly-based) approaches and what they entail.
Given the relative recency of this work, the choice of described datasets, which were pretty much deprecated at the time of writing, is surprising.

Referenced datasets:
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- DARPA 1999
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)

### A Detail Analysis on Intrusion Detection Datasets (2014)

[Link to Paper](http://dx.doi.org/10.1109/IAdCC.2014.6779523)
```
Sahu, S. K., Sarangi, S., & Jena, S. K. (2014, February). A detail analysis on intrusion detection datasets. In 2014 ieee international advance computing conference (IACC) (pp. 1348-1353). IEEE.
```

This paper shortly analyzed three papers the authors deem suitable to test their novel preprocessing techniques, which are supposed to improve the performance of various data mining algorithms.

Referenced datasets:
- [gureKDDCup](/intrusion-detection-datasets/content/datasets/gure_kddcup)
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)

### Network anomaly detection: Methods, systems and tools (2013)

[Link to Paper](https://doi.org/10.1109/SURV.2013.052213.00046)
```
Bhuyan, M. H., Bhattacharyya, D. K., & Kalita, J. K. (2013). Network anomaly detection: methods, systems and tools. Ieee communications surveys & tutorials, 16(1), 303-336.
```

This survey mainly focuses on different approaches towards network anomaly detection, encountered attacks, patterns, etc.
Datasets that are suitable for this purpose are mentioned as a secondary talking point, and described only in brief.

Referenced datasets:
- [DARPA'98 Intrusion Detection Program](/intrusion-detection-datasets/content/datasets/darpa98)
- [ISCX IDS 2012](/intrusion-detection-datasets/content/datasets/iscx_ids_2012)
- [KDD Cup 1999](/intrusion-detection-datasets/content/datasets/kdd_cup_1999)
- [NSL-KDD](/intrusion-detection-datasets/content/datasets/nsl_kdd_dataset)
- [TUIDS](/intrusion-detection-datasets/content/datasets/tuids)

Referenced collections:
- CAIDA
- DEFCON CTF archive
- [Lawrence Berkeley National Laboratory Traces](#the-internet-traffic-archive) (alias for: The Internet Traffic Archive)

## Other collections

`Last updated` refers to the last time a new entry was added to the collection.

### Awesome Cybersecurity Datasets

https://github.com/shramos/Awesome-Cybersecurity-Datasets
(accessed 18.02.2024, last updated 23.01.2021)

A "curated" personal collection of various cybersecurity-related datasets or collections, grouped into several categories such as "Network", "Software" or "Fraud".
Each entry is described in only one or two sentences, and most datasets are not, or only partially, suitable for IDS research.
The list is somewhat deprecated and does especially lack meaningful host-based datasets.

### Digital Corpora

https://digitalcorpora.org/ <br>
(accessed 19.02.2024, last updated 05.05.2023)

A collection of datasets mostly designed for the use in forensics education.
It consists of various disk images, memory dumps and pcaps, as well as a bunch of benign and malicious files.
It does not seem to contain actual log data.

### IMPACT

https://www.impactcybertrust.org/search <br>
(accessed 19.02.2024, last updated 13.07.2021)

The "Information Marketplace for Policy and Analysis of Cyber-Risk and Trust" (IMPACT, formerly PREDICT), maintained by the US Department of Homeland Security, contains 70 datasets.
These are for the most part made up of network related files (pcaps and DNS logs) from a wide variety of scenarios (CTF events, IoT, corpo networks, etc.), as well as some miscellaneous things like network shapefiles.
55 of these datasets were created by IMPACT, 15 are external (mostly CAIDA). Many datasets require prior authorization to access them.

### Malware Traffic Analysis

https://www.malware-traffic-analysis.net/ <br>
(accessed 19.02.2024, last updated 14.02.2024)

Various pcaps and malware samples stemming from individual campaigns or attack instances, but without any overall categorization or even overview.
They are available as blog posts named something like "DarkGate activity" or "GootLoader Infection", which each one listing some references and download links to any relevant files.

### NETRESEC

https://www.netresec.com/?page=PcapFiles <br>
(accessed 19.02.2024, last updated 04.01.2024)

A large collection of pcap files and other repositories which are hosting pcaps themselves.
They are categorized into CDX, Malware Traffic, Network Forensics, SCADA/ICS, CTF, Packet Injection/Man-on-the-Side, and Uncategorized.

### Public Security Log Sharing Site

https://log-sharing.dreamhosters.com/ <br>
(accessed 18.02.2024, last updated 11.08.2010)

A collection which started as an effort to collect various log samples, but seems to have been discontinued after operating for about one year.
Currently, it consists of nine entries containing Linux syslogs, firewall logs, apache logs, and web proxy logs.

### SecRepo - Samples of Security Related Data

https://www.secrepo.com/ <br>
(accessed 18.02.2024, last updated 01.10.2020)

An individuals effort to "keep a somewhat curated list of Security related data I've found, created, or was pointed to".
It contains several entries of the authors own creation, some of which are described in a bit more detail, as well as 121 "3rd party" entries from a broad range of topics, each described in a single sentence.
Some of them are usable for IDS related purposes.

### The Honeynet Project Challenges

https://www.honeynet.org/challenges/ <br>
(accessed 19.02.2024, last updated 18.03.2015)

A collection of 14 forensic challenges related to pcaps, malware and log files.
However, underlying resources for several of these challenges are no longer available.

### The Internet Traffic Archive

https://ita.ee.lbl.gov/ <br>
(accessed 18.02.2024, last updated 09.04.2010)

An archive hosting 16 different network data from various sources, such as WWW servers, web clients, and some custom networks.
Most data is in the form of traces, some include http logs or traceroute measurements.