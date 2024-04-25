---
title: Twente 2009 Dataset
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)

| <!-- -->                 | <!-- -->                                                                                    |
|--------------------------|---------------------------------------------------------------------------------------------|
| **Network Data Source**  | NetFlows                                                                                    |
| **Network Data Labeled** | Yes                                                                                         |
| **Host Data Source**     | -                                                                                           |
| **Host Data Labeled**    | -                                                                                           |
|                          |                                                                                             |
| **Overall Setting**      | Single OS / Honeypot                                                                        |
| **OS Types**             | Debian Etch 4.0                                                                             |
| **Number of Machines**   | 1                                                                                           |
| **Total Runtime**        | 6 days                                                                                      |
| **Year of Collection**   | 2009                                                                                        |
| **Attack Categories**    | Diverse                                                                                     |
| **Benign Activity**      | None                                                                                        |
|                          |                                                                                             |
| **Packed Size**          | 303 MB                                                                                      |
| **Unpacked Size**        | 1,85 GB                                                                                     |
| **Download Link**        | [goto](https://storage.dacs.utwente.nl/simpleweb-traces/traces/netflow/netflow2/index.html) |

***

### Overview

This dataset (unofficially named after the university where it was generated, Twente) originated from the desire for a
labeled dataset based on network flows originating from real traffic.
The authors discuss different possible environments and collection methods, settling for collecting flows from a single
honeypot over the span of 6 days.

### Environment

The honeypot consists of a single virtual machine running Debian Etch 4.0 with the following "non-standard" services
running:

- OpenSSH (with extensive logging patched in)
- Apache web server offering a log-in form
- ftp via proftp

### Activity

Due to the nature of honeypots, malicious activity can only be described in retrospect.
The machine ran for a total duration of 6 days, hosted inside the university network and directly connected to the
internet.

### Contained Data

During the collection period, all network traffic reaching the honeypot as well as various host logs were collected.
The labeling process is explained in detail in section 3 of the referenced paper, but can be summarized loosely as:
Pcaps are transformed into flows (Netflow v5), and collected host logs are used to label these flows and generate "
alerts", which are each correlated to one or more flows in a semi-automated way.
In other words, attacks get represented as alerts, which are then assigned to one or more flows.

For further information about alerts and how they are represented, consult `dataset_description.txt` in the download
source.
To represent the relations between flows and alerts, the authors made the decision to present the flow dataset in the
form of an SQL database, which can be built using the accompanying SQL statement file.

### Papers

- [A Labeled Data Set for Flow-Based Intrusion Detection (2009)](https://doi.org/10.1007/978-3-642-04968-2_4)

### Links

- ["Homepage"](https://storage.dacs.utwente.nl/simpleweb-traces/traces/netflow/netflow2/index.html)