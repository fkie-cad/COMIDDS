---
title: DARPA'98 Intrusion Detection Program
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)

| <!-- -->                 | <!-- -->                                                                                      |
|--------------------------|-----------------------------------------------------------------------------------------------|
| **Network Log Source**   | tcpdumps                                                                                      |
| **Network Logs Labeled** | Yes, via ground truth                                                                         |
| **Host Log Source**      | bsm audits, file system dumps                                                                 |
| **Host Logs Labeled**    | No                                                                                            |
|                          |                                                                                               |
| **Overall Setting**      | Military IT                                                                                   |
| **OS Types**             | Linux 2.0.27<br/>SunOS 4.1.4<br/>Sun Solaris 2.5.1<br/>Windows NT                             |
| **Number of Machines**   | 1000's                                                                                        |
| **Total Runtime**        | Nine weeks                                                                                    |
| **Year of Collection**   | 1998                                                                                          |
| **Attack Categories**    | DoS<br/>Remote to Local<br/>User to Root<br/>Surveillance/Probing                             |
| **User Emulation**       | Scripts for traffic generation, actual humans for performing complex tasks                    |
|                          |                                                                                               |
| **Packed Size**          | 5 GB                                                                                          |
| **Unpacked Size**        | _n/a_                                                                                         |
| **Download Link**        | [goto](https://www.ll.mit.edu/r-d/datasets/1998-darpa-intrusion-detection-evaluation-dataset) |

***

### Overview

One of the first major attempts to create a comprehensive dataset for intrusion detection research, tailored to aid
development and evaluation of IDSs.
It simulates a small Air Force base connected to the "Outside" (internet), and contains a substantial number of hosts,
including automation of certain user behavior.
It was originally planned to record actual operational traffic while executing attacks in a controlled manner, which in
the end was not possible due to privacy and security concerns.
Due to its age and a number of flaws, it should be used with reservations, if at all.

### Environment

Refer to the underlying [DARPA'98 Intrusion Detection Program](darpa98.md).

### Activity

Refer to the underlying [DARPA'98 Intrusion Detection Program](darpa98.md).

### Contained Data

Data is available in the form of tcpdumps, divided by day and week.
Labels are available via a separate ground truth, listing information like IPs, ports, services and attack names.
Additionally, host audit data as well as raw filesystems can be downloaded.
Later publications found a number of issues with this dataset, such as the presence of simulation artifacts - for
example, the TTL of malicious traffic is always 126 or 253, while benign traffic usually has the values 127 or 254.

### Papers

- [Evaluating Intrusion Detection Systems: The 1998 DARPA Off-line Intrusion Detection Evaluation (1998)](https://doi.org/10.1109/discex.2000.821506)

### Links

- [Homepage](https://www.ll.mit.edu/r-d/datasets/1998-darpa-intrusion-detection-evaluation-dataset)

### Related Entries

- [KDD Cup 1999](kdd_cup_1999.md)