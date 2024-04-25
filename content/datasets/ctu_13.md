---
title: CTU-13 Dataset
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)

| <!-- -->                 | <!-- -->                                                                       |
|--------------------------|--------------------------------------------------------------------------------|
| **Network Data Source**  | pcaps, NetFlows                                                                |
| **Network Data Labeled** | Yes, NetFlows are labeled                                                      |
| **Host Data Source**     | -                                                                              |
| **Host Data Labeled**    | -                                                                              |
|                          |                                                                                |
| **Overall Setting**      | Enterprise IT                                                                  |
| **OS Types**             | Windows XP SP2                                                                 |
| **Number of Machines**   | n/a                                                                            |
| **Total Runtime**        | 1-67 hrs                                                                       |
| **Year of Collection**   | 2011                                                                           |
| **Attack Categories**    | Various Botnet activity<br/>(Neris, Rbot, Virut, Menti, Sogou, Murlo, NSIS.ay) |
| **Benign Activity**      | Real background traffic                                                        |
|                          |                                                                                |
| **Packed Size**          | n/a                                                                            |
| **Unpacked Size**        | 697 GB (sum of all 13 scenarios)                                               |
| **Download Link**        | [goto](https://www.stratosphereips.org/datasets-ctu13)                         |

***

### Overview

The Czech Technical University (CTU) dataset originated from the desire to compare different botnet detection methods.
For this purpose, the authors deemed it necessary to use a dataset which is publicly available (i.e., without sensitive
contents) and fulfils a number of requirements, such as containing real background traffic or representing different
botnets.
Thirteen different scenarios were executed, with each one representing a certain botnet behavior, resulting in thirteen
individual datasets.

Note that these thirteen datasets are a subset of the [Malware Capture Facility Project](https://mcfp.weebly.com/), though other datasets within this collection did not undergo any further analysis or study.

### Environment

The infected network consists of an unspecified number of virtualized machines running Windows XP SP2, with each machine
being bridged into the network of the university.

### Activity

For each of the thirteen scenarios, some botnet malware (Neris, Rbot, Virut, Menti, Sogou, Murlo, or NSIS.ay) was
deployed within the target network, configured to match certain desired behavior. More details regarding each scenario
can be found in section 6.1 of the linked paper.

### Contained Data

Traffic was captures on both infected hosts and university routers using tcpdump, the result of which was then converted
into the NetFlow format composed of the following fields:
_Start Time, End Time, Duration, Source IP address, Source Port, Direction, Destination IP address, Destination Port,
State, SToS, Total Packets, and Total Bytes._

For the labeling process, first each flow is labeled as `background`.
Next, flows originating from known and controlled machines within the university network were assigned the `normal`
label, while the `botnet` label was assigned to any flows coming to or from any of the known infected machines.
For each scenario, the following data is available:

- Full pcaps from infected machines
- Truncated pcaps from the complete capture (to preserve privacy)
- Unidirectional NetFlows (labeled)
- Bidirectional NetFlows (labeled)
- Bro (now Zeek) output files - presumably only those originating from infected machines?
- The original malware
- Config information (e.g., for converting pcaps to NetFlows)

The authors suggest that only the bidirectional NetFlows should be used for research efforts, stating that they
outperformed the unidirectional ones.
Note that NetFlows are only available in binary format and should be opened
with [Argus](https://openargus.org/using-argus), though other tools might work too.

### Papers

- [An Empirical Comparison of Botnet Detection Methods (2014)](https://doi.org/10.1016/j.cose.2014.05.011)

### Links

- [Homepage](https://www.stratosphereips.org/datasets-ctu13)
- [Malware Capture Facility Project](https://mcfp.weebly.com/)