---
title: OD-IDS2022
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                        |
|--------------------------|-------------------------------------------------|
| **Network Data Source**  | NetFlows                                        |
| **Network Data Labeled** | Yes                                             |
| **Host Data Source**     | -                                               |
| **Host Data Labeled**    | -                                               |
|                          |                                                 |
| **Overall Setting**      | Enterprise IT                                   |
| **OS Types**             | Windows Server 2016<br/>Linux Server 18.04      |
| **Number of Machines**   | 2                                               |
| **Total Runtime**        | 30 days                                         |
| **Year of Collection**   | 2022                                            |
| **Attack Categories**    | OWASP Top Ten web application risks             |
| **User Emulation**       | Yes, but not detailed                           |
|                          |                                                 |
| **Packed Size**          | n/a                                             |
| **Unpacked Size**        | n/a                                             |
| **Download Link**        | *must be requested via mail* (see source paper) |

***

### Overview
The Offensive Defensive Intrusion Detection System (OD-IDS2022) dataset is an effort to create a network-based dataset consisting of NetFlows, fulfilling a number of requirements cited out by the authors.
These include commonly named dataset characteristics such as Complete Capture, Complete Network Configuration, Labels, Anonymity, etc.
The defining features of this dataset are its comparatively long runtime (30 days) along with a large number of different network-based attacks (28), inspired by the Open Web Application Security Project's (OWASP) Top 10 list of web application security risks in 2021.
However, it seems to suffer from poor documentation regarding both benign and malicious activity, and access to the dataset must be requested manually via email.

### Environment
The target environment consists of a virtualized network hosting two servers, Windows Server 2016 and Ubuntu Server 18.04 (relatively old systems given that this dataset was created in 2022).
Each machine runs an Apache HTTP server as well as an instance of both MySQL and PostgreSQL databases.
This victim network can only be accessed through a firewall.
This architecture is also depicted in Figure 2 of the paper.

Two additional internal networks labeled "Blue Team Observation" and "Red Team Observation" are connected to this network, although their purpose is not explained *at all*, besides shortly defining the general meaning of the terms red and blue team.
Attacks originate from a third, external network, accessing the victim through the internet.
The authors state that packet captures are collected *somewhere* using tcpdump and Wireshark, and the "Blue Team Observation" network is shown containing a "Network Capturing Server", most likely indicating its involvement in this process (though leaving this as guesswork to the reader is a questionable decision by the authors).

### Activity
As mentioned, the choice of attacks is inspired by the OWASP's list of top 10 security risk, with 28 different attacks covering various scenarios.
These attacks are executed by using commonly available frameworks or existing malware, for example:
- Apache Flink Directory Traversal (using Burp Suite)
- DDoS (using Slowloris or Trinoo)
- Ransomware (using MalwareBuster or WannaCry)
- Package Update Escape Bypass (using metasploit)

The full list of attacks and tools is available in Table 3 within the cited paper.
Unfortunately, no further details beyond name and leveraged tool per attack are available, although this is an improvement over the description of included benign behavior, whose general existence is mentioned, but not explained in any fashion.

### Contained Data
Collected packet captures are processed into NetFlows using [CICFlowMeter](https://www.unb.ca/cic/research/applications.html#CICFlowMeter), producing the same set of 81 features that are for example leveraged by the [CSE-CIC-IDS2018](cse_cic_ids2018.md) dataset, which utilizes the same tool.
An explanation for each of these 81 features can be found in Section 3.5 of the cited paper;
an 82nd features holds the label of a given flow, which can be either "benign" or any of the 28 attack classes.
This data was then split into a training and a validation subset with a ratio of 75:25 along with other minor pre-processing steps, detailed in Chapter 4 of the paper.

The labeling process is not detailed, other than briefly mentioning that this process is typically performed manually.

### Papers
- [OD-IDS2022: Generating a New Offensive Defensive Intrusion Detection Dataset for Machine Laerning-Based Attack Classification (2022)](http://dx.doi.org/10.1007/s41870-023-01464-8)

### Links
- [OWASP Top 10](https://owasp.org/Top10/)

### Data Examples
*unavailable*