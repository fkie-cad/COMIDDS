---
title: TUIDS
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)

| <!-- -->                 | <!-- -->                               |
|--------------------------|----------------------------------------|
| **Network Data Source**  | pcaps, NetFlows                        |
| **Network Data Labeled** | Features are labeled                   |
| **Host Data Source**     | -                                      |
| **Host Data Labeled**    | -                                      |
|                          |                                        |
| **Overall Setting**      | Enterprise IT                          |
| **OS Types**             | Undisclosed                            |
| **Number of Machines**   | 44                                     |
| **Total Runtime**        | 4 weeks                                |
| **Year of Collection**   | 2012                                   |
| **Attack Categories**    | DoS                                    |
| **Benign Activity**      | Presumably synthetic, but not detailed |
|                          |                                        |
| **Packed Size**          | n/a                                    |
| **Unpacked Size**        | n/a                                    |
| **Download Link**        | n/a                                    |

***

### Overview
The TUIDS dataset (presumably standing for Tezpur University IDS) was an attempt to improve upon the deprecated DARPA'98 dataset and its derivatives like NSL KDD -
though some of the raised criticism is a bit nonsensical (e.g., NSL KDD is criticised for being "simulated", although they use the exact same methodology of collecting data in a testbed).
This dataset is derived from a medium-sized testbed of 44 machines, which are then subjected to various DoS attacks.
However, the dataset is no longer available for unknown reasons, making it both difficult and somewhat pointless to provide a lot of detailed information here.

### Environment
The testbed consists of one router, one server, two workstations, and 44 nodes (plus three switches).
Details regarding operating systems or running services are not available, nor is it made clear what a node exactly is.
The exact network setup is explained in section 5.1 of the referenced paper.

### Activity
Malicious activity comes in the form of various DoS attacks (bonk, saihyousen, oshare, window, syn, xmas, fraggle, smurf) which were executed using the [targa2.c tool](https://packetstormsecurity.com/files/15949/targa2.c.html).
The paper seems to suggest that there is some kind normal activity going on, but does not provide any detail whatsoever.

### Contained Data
Data is (or should) be available in the form of pcaps and NetFlows, collected from mirror ports on two separate machines (resulting in two datasets, "Packet" and "Flow Based").
Only 24 NetFlow features are considered, which are listed in 5.3.
Labeling is done by simply considering all traffic from and to attacking machines as malicious, and all other traffic as normal.
Without the data actually available, there is little more to say here.

### Papers
- [Packet and Flow Based Network Intrusion Dataset (2012)](https://doi.org/10.1007/978-3-642-32129-0_34)

### Links
- [Homepage](https://www.tezu.ernet.in/) (paper references this as a download source. I gave up after 15 minutes of sifting through the website.)
