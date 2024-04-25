---
title: CIC DoS
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)

| <!-- -->                 | <!-- -->              |
|--------------------------|-----------------------|
| **Network Data Source**  | Unknown               |
| **Network Data Labeled** | Presumably            |
| **Host Data Source**     | -                     |
| **Host Data Labeled**    | -                     |
|                          |                       |
| **Overall Setting**      | Single OS             |
| **OS Types**             | Apache Linux          |
| **Number of Machines**   | 1                     |
| **Total Runtime**        | 24 hours              |
| **Year of Collection**   | 2017                  |
| **Attack Categories**    | Application-layer DoS |
| **Benign Activity**      | n/a                   |
|                          |                       |
| **Packed Size**          | n/a                   |
| **Unpacked Size**        | 4,6 GB                |
| **Download Link**        | Currently unavailable |

***

### Overview
The Canadian Institute for Cybersecurity (CIC) DoS dataset focuses on Denial-of-Services attacks targeting the application layer (as opposed to the network layer).
The authors argue that these types of DoS attacks commonly avoid traditional network-layer based detection mechanisms, requiring a novel approach.
Specifically, they focus mostly on low-volume DoS attacks, which are characterized by "small amounts of attack traffic transmitted strategically to a victim", whereas high-volume attacks are more similar to traditional DoS attacks, relying on flooding the application layer with requests.
As part of this research, and due to the lack of usable datasets of this kind, the authors introduce the CIC DoS dataset, which consists of 24 hours of traffic collected from a webserver being the victim of such attacks.
However, the dataset is no longer available for unknown reasons, making it both difficult and somewhat pointless to provide a lot of detailed information here.

### Environment
The victim setup consists of a webserver running Apache Linux v2.2.22, PHP5 and Drupal v7 as a content management system.
Further details are not available.

### Activity
The declared goal of executed attacks was to render services on the server side unresponsive while being as stealthy and resource-efficient as possible, including stopping attacks as soon as servers became unresponsive.
The authors state that attacks were selected to match the most common types of application layer DoS, resulting in a mix of high- and log-volume attacks.
These attacks were executed leveraging several publicly available tools such as [Goldeneye](https://github.com/jseidl/GoldenEye) or [Slowloris](https://github.com/gkbrk/slowloris), for a total of eight attacks:
- High-volume HTTP attacks:
    - DoS improved GET
    - DDoS GET
    - DoS GET
- Low-volume HTTP attacks
    - slow-send body (twice with different tools)
    - slow-send headers (twice with different tools)
    - slow-read

Additional details can be found in chapter 6 of the cited paper.

### Contained Data
Traffic from executed attacks was intermixed with benign traces from the [ISCX Intrusion Detection Evaluation Dataset](iscx_ids_2012.md).
Attack traffic was presumably modified to target servers from the ISCX environment, for a total of 24 hours of attack traffic.
In which format (pcaps, NetFlows, custom features, etc.) this data is available is unknown and also not detailed in the paper.
I would assume data is labeled, but obviously have no way to confirm this.

### Papers
- [Detecting HTTP-based Application Layer DoS Attacks on Web Servers in the Presence of Sampling (2017)](https://doi.org/10.1016/j.comnet.2017.03.018)

### Links
- [Homepage](https://www.unb.ca/cic/datasets/dos-dataset.html)

### Related Entries
- [ISCX Intrusion Detection Evaluation Dataset](iscx_ids_2012.md)