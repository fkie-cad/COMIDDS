---
title: UNSW-NB15
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                                           |
|--------------------------|----------------------------------------------------------------------------------------------------|
| **Network Log Source**   | pcaps, custom network features                                                                     |
| **Network Logs Labeled** | Yes                                                                                                |
| **Host Log Source**      | -                                                                                                  |
| **Host Logs Labeled**    | -                                                                                                  |
|                          |                                                                                                    |
| **Overall Setting**      | Miscellaneous                                                                                      |
| **OS Types**             | Undisclosed                                                                                        |
| **Number of Machines**   | <45                                                                                                |
| **Total Runtime**        | 31 hours                                                                                           |
| **Year of Collection**   | 2015                                                                                               |
| **Attack Categories**    | Scanning<br/>Backdoors<br/>DoS<br/>Exploits<br/>Reconnaissance<br/>Shellcode<br/>Worms<br/>Fuzzing |
| **User Emulation**       | Yes, via IXIA PerfectStorm                                                                         |
|                          |                                                                                                    |
| **Packed Size**          | ~100 GB                                                                                            |
| **Unpacked Size**        | n/a                                                                                                |
| **Download Link**        | n/a (Storage provider decommissioned)                                                              |

***

### Overview
The UNSW-NB15 dataset, developed at the University of New South Wales (UNSW), aims to provide an at the time modern network benchmark dataset.
It improves upon existing datasets like KDD98 by including newer attacks, which are realized using the IXIA PerfectStorm tool, providing both normal and malicious behavior.
It is mostly intended for anomaly-related use-cases, though the data also allows for application of signature-based IDS solutions.
However, as of right now, none of the data is publicly available due to the storage provider being shut down.

### Environment
The general setup consists of three virtual servers, two routers and an unspecified number of clients, divided into three networks and orchestrated as shown in the diagram below.
Server 1 and 3 generate normal traffic, while server 2 generates malicious traffic.
The paper lists the number of "distinct IP addresses" as 45, but the total number of machines is most definitely lower.

![UNSW-NB15 Network Architecture]({{ "/assets/img/unsw_nb15_network_architecture.jpeg" | relative_url }})

It seems to be implied that all traffic from router 2 is (also?) passed to router 1, where all traffic is dumped in the form of pcaps.
Section 4.A is not entirely clear in this regard.
Further documentation, especially regarding OS types, is not provided.

### Activity
Both benign and malicious activity is managed and executed by the IXIA PerfectStorm tool, specifically its traffic generator.
However, details regarding either process are not given, it is only stated that "the attack behaviour is nourished from the CVE site for the purpose of a real representation of a modern threat environment".
Attacks are grouped into one of nine categories:
- Fuzzers
- Analysis
- Backdoors
- DoS
- Exploits
- Generic
- Reconnaissance
- Shellcode
- Worms

Additionally, IXIA supplies a ground truth file, listing information like start time or source port and address.
Two simulation runs were performed, which differ only in the frequency of their attacks.
During the first run (16 hours), one attack is executed per second.
During the second run (15 hours), that number increases to ten attacks per second.

### Contained Data
As mentioned, pcaps of presumably the entire network are collected at a central location (Router 1) using tcpdump.
From these files, 49 features are derived, which are grouped into:
- 5 flow features (e.g., Source IP address)
- 13 basic features (e.g., Source to destination bytes)
- 8 content features (e.g., Source TCP sequence number)
- 9 time features (e.g. record start time)
- 12 additional features

All features are explained in section 4.E and 4.F of the paper.
In total, 2.540.044 records were derived, available in the form of `.csv` files.
These were then labelled using the ground truth supplied by IXIA PerfectStorm;
labeling per entry consists of:
- A binary label (0 for normal, 1 for malicious)
- An attack category (from those listed above)

### Papers
- [UNSQ-NB15: A Comprehensive Data Set for Network Intrusion Detection Systems (2015)](https://doi.org/10.1109/MilCIS.2015.7348942)

### Links
- [Homepage](https://research.unsw.edu.au/projects/unsw-nb15-dataset)
- [IXIA PerfectStorm](https://www.keysight.com/us/en/products/network-test/network-test-hardware/perfectstorm.html)

### Data Examples
*Dataset currently not available, the storage provider CloudStor has been decommissioned*