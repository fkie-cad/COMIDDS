---
title: UNIBS
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)

| <!-- -->                 | <!-- -->                                                           |
|--------------------------|--------------------------------------------------------------------|
| **Network Data Source**  | NetFlows                                                           |
| **Network Data Labeled** | No                                                                 |
| **Host Data Source**     | -                                                                  |
| **Host Data Labeled**    | -                                                                  |
|                          |                                                                    |
| **Overall Setting**      | Enterprise IT                                                      |
| **OS Types**             | Undisclosed                                                        |
| **Number of Machines**   | 20                                                                 |
| **Total Runtime**        | 3 days                                                             |
| **Year of Collection**   | 2009                                                               |
| **Attack Categories**    | None                                                               |
| **Benign Activity**      | Real users                                                         |
|                          |                                                                    |
| **Packed Size**          | -                                                                  |
| **Unpacked Size**        | 2,7 GB                                                             |
| **Download Link**        | [must be requested](http://netweb.ing.unibs.it/~ntw/tools/traces/) |

***

### Overview
The University of Brescia (UNIBS) dataset was created to showcase the capabilities of the "GT" software, an open source toolset facilitating the association of application-level ground truth with network traffic traces.
This is done by probing a monitored host's kernel to gather ground truth at the application level, which can then later be assigned to any collected traces with minimal CPU overhead.
Beyond this, the dataset does not seem to serve a greater purpose, as it does not contain any malicious activity (that the authors are aware of) and is also anonymized.

### Environment
Traffic was collected from 20 workstations located in the campus network of the University of Brescia over the course of three consecutive days (2009-09-30 to 2009-10-02).
Each workstation is running a "GT client daemon", information regarding network configuration or specific operating systems is not available.

### Activity
(Presumably) real users used a variety of traffic generating applications and protocols, namely:
- Web (HTTP, HTTPS)
- Mail (POP3, IMAP4, SMTP)
- Skype
- P2P (Bittorrent, Edonkey)
- Other (FTP, SSH, MSN)

Any further details are not available, most likely because the focus of this dataset was simply on correctly assigning flows to these services or protocols.
Intentional malicious activity is not present.

### Contained Data
Traffic was collected from the central faculty router via `tcpdump` and enriched with ground truth from the GT tool (in the form of related protocol and application).
It is available in an anonymized and payload-stripped form, presumably in as NetFlows, but has to be requested via mail.

### Papers
- [GT: picking up the truth from the ground for internet traffic (2009)](https://doi.org/10.1145/1629607.1629610)

### Links
- [Homepage](http://netweb.ing.unibs.it/~ntw/tools/traces/)