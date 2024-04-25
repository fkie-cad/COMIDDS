---
title: CIC-IDS2017
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                                         |
|--------------------------|--------------------------------------------------------------------------------------------------|
| **Network Data Source**  | pcaps, derived features                                                                          |
| **Network Data Labeled** | Yes                                                                                              |
| **Host Data Source**     | -                                                                                                |
| **Host Data Labeled**    | -                                                                                                |
|                          |                                                                                                  |
| **Overall Setting**      | Enterprise IT                                                                                    |
| **OS Types**             | Windows Server 2016<br/>Ubuntu 12/16.04<br/>Windows Vista/7/8.1/10<br/>macOS<br/>Kali (Attacker) |
| **Number of Machines**   | 14 (+ 4 attacker)                                                                                |
| **Total Runtime**        | ~5 days                                                                                          |
| **Year of Collection**   | 2017                                                                                             |
| **Attack Categories**    | Brute Force FTP/SSH<br/>DoS & DDoS<br/>Web Attacks<br/>Botnets                                   |
| **Benign Activity**      | Synthetic, models complex behavior                                                               |
|                          |                                                                                                  |
| **Packed Size**          | 48,4 GB                                                                                          |
| **Unpacked Size**        | 50 GB                                                                                            |
| **Download Link**        | [goto](http://205.174.165.80/CICDataset/CIC-IDS-2017/Dataset/)                                   |

***

### Overview

The Canadian Institute for Cybersecurity (CIC) IDS dataset is based on a number of requirements, targeted at datasets
intended to be used fo IDS research,
which were laid out by the same authors in a publication released shortly before this dataset.
To accomplish this, it uses to concept of profiles to model both benign and malicious behavior.
As most related efforts, it aims to improve upon existing datasets, with the general scenario being that of an
enterprise network under attack.
It is the predecessor to the CDE CIC IDS2018 dataset.

### Environment

The network is divided into a separate victim and attacker network, each consisting of multiple machines, running
various Versions of Windows and Linux, as well as macOS.

![CIC IDS 2017 Network Diagram]({{ "/assets/img/cic_ids_2017_diagram.svg" | relative_url }})

### Activity

Both benign and malicious traffic is defined using the notion of benign (B) and malicious (M) profiles, defining what
action is taken at which point in time.
For the former, traffic from 25 real users was collected and abstracted into a set of features, defining usage of five
different protocols (HTTP, HTTPS, FTP, SSH, SMPT) to mimic normal behavior.
M-profiles define six different attacks to be carried out during the simulation, with details for each being available
in section 3.3 of paper [1]:

- Brute force
- Heartbleed
- Botnet
- DoS & DDoS
- Web attacks (SQLi, XSS, etc)
- Infiltration attacks

The total capturing period lasted ~5 days, with attacks being performed on every day except the first.

### Contained Data

Raw data consists of packet captures (pcaps) and is grouped by day.
In addition, for every day but the first, two processed versions are available, flows and features, the latter being
intended to be used for ML approaches (pruned of information like IP).
Both processed data types are labelled with either benign or, in case of a malicious event, the type of attack this
event originated from.

### Papers

- [Toward Generating a New Intrusion Detection Dataset and Intrusion Detection Traffic Characterization (2017)](https://doi.org/10.5220/0006639801080116)
- [An Evaluation Framework for Intrusion Detection Datasets (2016)](https://doi.org/10.1109/ICISSEC.2016.7885840)
- [Troubleshooting an Intrusion Detection Dataset: the CICIDS2017 Case Study (2021)](https://doi.org/10.1109/SPW53761.2021.00009)
- [Error Prevalence in NIDS datasets: A Case Study on CIC-IDS-2017 and CSE-CIC-IDS-2018 (2022)](https://doi.org/10.1109/CNS56114.2022.9947235)
- [Network Intrusion Detection: A Comprehensive Analysis of CIC-IDS2017 (2022)](https://dx.doi.org/10.5220/0000157000003120)
- [Errors in the CICIDS2017 Dataset and the Significant Differences in Detection Performances It Makes (2022)](https://doi.org/10.1007/978-3-031-31108-6_2)

### Links

- [Homepage](https://www.unb.ca/cic/datasets/ids-2017.html)
- [Download Page](http://205.174.165.80/CICDataset/CIC-IDS-2017/Dataset/)

### Related Entries

- [CSE CIC IDS2018](cse_cic_ids2018.md)

### Data Examples

Snippet of traffic flows taken from `TrafficLabelling/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv`

```
192.168.10.16-116.213.214.215-56360-443-6,192.168.10.16,56360,116.213.214.215,443,6,6/7/2017 9:15,113,2,0,0,0,0,0,0,0,0,0,0,0,0,17699.11504,113,0,113,113,113,113,0,113,113,0,0,0,0,0,0,0,0,0,64,0,17699.11504,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,64,0,0,0,0,0,0,2,0,0,0,681,-1,0,32,0,0,0,0,0,0,0,0,BENIGN
172.16.0.1-192.168.10.50-44380-80-6,172.16.0.1,44380,192.168.10.50,80,6,6/7/2017 9:15,5185118,7,7,1022,2321,372,0,146,184.0787875,1047,0,331.5714286,439.6592837,644.7297824,2.700034985,398855.2308,1372180.71,4963956,4,221162,36860.33333,56141.02125,141434,4,5185004,864167.3333,2027593.314,5001548,879,0,0,0,0,232,232,1.350017492,1.350017492,0,1047,222.8666667,331.3239387,109775.5524,0,0,0,1,0,0,0,0,1,238.7857143,146,331.5714286,232,0,0,0,0,0,0,7,1022,7,2321,29200,252,3,32,0,0,0,0,0,0,0,0,Web Attack – Brute Force
192.168.10.15-23.194.182.63-50346-80-6,192.168.10.15,50346,23.194.182.63,80,6,6/7/2017 9:15,259762,4,4,207,1709,195,0,51.75,95.54187564,1697,0,427.25,846.5047253,7375.98263,30.79742226,37108.85714,77386.88179,210781,51,48981,16327,13973.63943,24489,192,235408,78469.33333,115202.6524,210832,810,0,0,0,0,92,92,15.39871113,15.39871113,0,1697,212.8888889,560.1431613,313760.3611,0,0,0,1,0,0,0,0,1,239.5,51.75,427.25,92,0,0,0,0,0,0,4,207,4,1709,8192,946,3,20,0,0,0,0,0,0,0,0,BENIGN
192.168.10.15-23.194.182.63-50347-80-6,192.168.10.15,50347,23.194.182.63,80,6,6/7/2017 9:15,357626,4,4,210,1552,198,0,52.5,97.04122835,1540,0,388,768.0052083,4926.934843,22.36973822,51089.42857,113924.299,308242,42,49384,16461.33333,14219.05483,25065,49,333461,111153.6667,171065.931,308284,1713,0,0,0,0,92,92,11.18486911,11.18486911,0,1540,195.7777778,508.1815074,258248.4444,0,0,0,1,0,0,0,0,1,220.25,52.5,388,92,0,0,0,0,0,0,4,210,4,1552,8192,946,3,20,0,0,0,0,0,0,0,0,BENIGN
```

Snippet of features taken from `MachineLearningCVE/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv`

```
80,5185118,7,7,1022,2321,372,0,146,184.0787875,1047,0,331.5714286,439.6592837,644.7297824,2.700034985,398855.2308,1372180.71,4963956,4,221162,36860.33333,56141.02125,141434,4,5185004,864167.3333,2027593.314,5001548,879,0,0,0,0,232,232,1.350017492,1.350017492,0,1047,222.8666667,331.3239387,109775.5524,0,0,0,1,0,0,0,0,1,238.7857143,146,331.5714286,232,0,0,0,0,0,0,7,1022,7,2321,29200,252,3,32,0,0,0,0,0,0,0,0,Web Attack � Brute Force
80,259762,4,4,207,1709,195,0,51.75,95.54187564,1697,0,427.25,846.5047253,7375.98263,30.79742226,37108.85714,77386.88179,210781,51,48981,16327,13973.63943,24489,192,235408,78469.33333,115202.6524,210832,810,0,0,0,0,92,92,15.39871113,15.39871113,0,1697,212.8888889,560.1431613,313760.3611,0,0,0,1,0,0,0,0,1,239.5,51.75,427.25,92,0,0,0,0,0,0,4,207,4,1709,8192,946,3,20,0,0,0,0,0,0,0,0,BENIGN
80,357626,4,4,210,1552,198,0,52.5,97.04122835,1540,0,388,768.0052083,4926.934843,22.36973822,51089.42857,113924.299,308242,42,49384,16461.33333,14219.05483,25065,49,333461,111153.6667,171065.931,308284,1713,0,0,0,0,92,92,11.18486911,11.18486911,0,1540,195.7777778,508.1815074,258248.4444,0,0,0,1,0,0,0,0,1,220.25,52.5,388,92,0,0,0,0,0,0,4,210,4,1552,8192,946,3,20,0,0,0,0,0,0,0,0,BENIGN
80,394177,4,4,209,1581,197,0,52.25,96.54144188,1569,0,395.25,782.5051118,4541.107168,20.29545103,56311,95460.54537,262095,100,132082,44027.33333,56213.14882,107403,192,369873,123291,123996.2342,262195,23767,0,0,0,0,92,92,10.14772551,10.14772551,0,1569,198.8888889,517.7720165,268087.8611,0,0,0,1,0,0,0,0,1,223.75,52.25,395.25,92,0,0,0,0,0,0,4,209,4,1581,8192,946,3,20,0,0,0,0,0,0,0,0,BENIGN
```