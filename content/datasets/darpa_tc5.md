---
title: DARPA TC5
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Links](#links)
- [Related Entries](#related-entries)

| <!-- -->                 | <!-- -->                                                                         |
|--------------------------|----------------------------------------------------------------------------------|
| **Network Data Source**  | -                                                                                |
| **Network Data Labeled** | -                                                                                |
| **Host Data Source**     | Custom event logs                                                                |
| **Host Data Labeled**    | Ground truth provided                                                            |
|                          |                                                                                  |
| **Overall Setting**      | Enterprise IT                                                                    |
| **OS Types**             | Windows<br/>Ubuntu                                                               |
| **Number of Machines**   | n/a                                                                              |
| **Total Runtime**        | 10 days                                                                          |
| **Year of Collection**   | 2019                                                                             |
| **Attack Categories**    | All MITRE tactics                                                                |
| **Benign Activity**      | Present, but not specified                                                       |
|                          |                                                                                  |
| **Packed Size**          | n/a                                                                              |
| **Unpacked Size**        | n/a                                                                              |
| **Download Link**        | [goto](https://drive.google.com/drive/folders/1okt4AYElyBohW4XiOBqmsvjwXsnUjLVf) |

***

### Overview

The DARPA Transparent Computing (TC) 5 dataset originated from the last of five what the authors call engagements.
The purpose of these operations was to test and evaluate methods of providing visibility into system interactions, aka
technologies to read and record provenance data between entities (--> "Transparent Computing").
"Technical areas" (TAs) were defined, and each "TA performer" is tasked with fulfilling a certain goal:

- TA1: Tagging and Tracking (aka logging)
- TA2: Detection and Policy Enforcement
- TA3: Architecture
- TA4: Scenario Development
- TA5.1: Adversarial Challenge Team

The data released by DARPA contains information from TA1 and TA5.1, or in other words, log data and ground truth about
executed attacks.
Additionally, tools and instructions for visualizing this data are provided, with focus laying on potential insights
gained from exploiting provenance data.

### Environment

Sadly, no information regarding the underlying architecture is present;
The kind of attacks described in the ground truth suggest a larger network, with some machines running Windows and
Ubuntu.

### Activity

Unspecified "benign background traffic" was run continuously during the testing period, while attacks were only
performed from 0900 to 1700 on weekdays (though no exact details regarding runtime are listed).
The ground truth suggests a total runtime of 10 days, from 08.05.2019 to 17.05.2019.
Attacks mimicked those of APT groups, with methods growing in complexity and sophistication over the course of the
engagement.
Further details are available in the ground truth, which could also be used to label the present event logs.

### Contained Data

Log collection was done by five different TA1 performers, named after the corresponding project (cadets, clearscope,
fivedirections, theia, and trace).
These projects differ in how they balance tracking detail against the resulting system overhead, though exact details
are not available.
All of them store collected data using a predefined data model, offering information about the event, its parameters,
and its parents, accompanied by IDs to allow for the previously mentioned provenance visibility.
Further specifications of the data model are linked below, but no information regarding the actual collection process is
provided.

Data is provided in a serialized binary format, the Readme file within the linked GDrive provides instructions regarding
further processing, for example into JSON format.
As mentioned, labels are not available, but the provided ground truth could be used to identify IOCs.

### Links

- [GitHub README](https://github.com/darpa-i2o/Transparent-Computing/blob/master/README.md)
- [GDrive](https://drive.google.com/drive/folders/1okt4AYElyBohW4XiOBqmsvjwXsnUjLVf)
- [Ground Truth](https://drive.google.com/file/d/1cc3C5JW-Kn-VdXqeBGwvHBKSdR_YmSGj/view?usp=drive_link)
- [Data Model Description](https://drive.google.com/file/d/1bhkU9My_MkuSl_MymRPofKslkdkcZ-Yw/view?usp=drive_link)

### Related Entries

- [DARPA TC3](darpa_tc3.md)