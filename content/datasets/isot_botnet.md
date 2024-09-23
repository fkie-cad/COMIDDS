---
title: ISOT BOTNET
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)

| <!-- -->                 | <!-- -->                                                                       |
| ------------------------ | ------------------------------------------------------------------------------ |
| **Network Data Source**  | pcaps                                                                          |
| **Network Data Labeled** | Yes                                                                            |
| **Host Data Source**     | -                                                                              |
| **Host Data Labeled**    | -                                                                              |
|                          |                                                                                |
| **Overall Setting**      | Enterprise IT                                                                  |
| **OS Types**             | Undisclosed                                                                    |
| **Number of Machines**   | 2000+                                                                          |
| **Total Runtime**        | n/a                                                                            |
| **Year of Collection**   | 2004-2010                                                                      |
| **Attack Categories**    | Botnets (Storm, Waledac)                                                       |
| **Benign Activity**      | Real users                                                                     |
|                          |                                                                                |
| **Packed Size**          | 3 GB                                                                           |
| **Unpacked Size**        | 10,6 GB                                                                        |
| **Download Link**        | [goto](https://drive.google.com/file/d/1X1zPBJFPHU1ToQbpyd1Is1tJJuz2BeRd/view) |

***

### Overview
The ISOT Botnet dataset is an amalgamation of several individual datasets, two containing malicious botnet traffic, and five datasets consisting of benign traffic.
Malicious data was taken from the "French Chapter" of the Honeynet project, while (anonymized) benign traces come from the LBNL Enterprise Trace Repository.
The combination of these traces, after some preprocessing to make them appear as if they would stem from the same network, are then used to test several botnet detection methods leveraging network behavior analysis and machine learning.
However, we were unable to find any information regarding the source of malicious traces, as linked pages no longer exist and further search remained fruitless.

### Environment
The merged dataset contains traces from 23 individual subnets, 22 with only benign traffic (stemming from the LBNL traces) and one with both malicious and benign traffic (merged traffic from both sources).
The IPs of the latter subnet can be obtained from Table 2 of the linked documentation.
Information regarding services, operating systems and so on are not available.

### Activity
Details regarding activity are not available;
there might be some additional information hidden in LBNL publications, but we consider this to be out of scope.

### Contained Data
As a first step to merge benign and malicious traces, the IP addresses of infected machines were mapped to two of the machines providing benign background traffic.
Then, the authors used to the `TcpReplay` tool to replay all traces on the same network interface in order to homogenize the network behavior shown by individual datasets.
These traces are simply available in the form of a single large pcap file with 1,675,424 unique flows, of which 3.33% are malicious.
Labels are available via malicious traffic having a specific MAC, as per Table 2 of the linked documentation.

It should be noted that the application of methods based on machine learning on merged datasets bears some additional risks;
researchers must ensure that results are not a byproducts of anomalies that remained after the merging process, which might not actually be caused by the malicious behavior, but rather the simple fact that these traces stem from separate environments.

### Papers
- [Detecting P2P botnets through network behavior analysis and machine learning (2011)](https://doi.org/10.1109/PST.2011.5971980)

### Links
- [Documentation](https://onlineacademiccommunity.uvic.ca/isot/wp-content/uploads/sites/7295/2023/03/ISOT-Dataset-Overview-v0.5.pdf)
- [LBNL/ICSI Enterprise Tracing Project](https://www.icir.org/enterprise-tracing/download.html)