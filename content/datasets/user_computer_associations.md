---
title: User-Computer Authentication Associations in Time
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->              |
|--------------------------|-----------------------|
| **Network Data Source**  | -                     |
| **Network Data Labeled** | -                     |
| **Host Data Source**     | Authentication events |
| **Host Data Labeled**    | No                    |
|                          |                       |
| **Overall Setting**      | Enterprise IT         |
| **OS Types**             | Undisclosed           |
| **Number of Machines**   | 22,284                |
| **Total Runtime**        | 9 months              |
| **Year of Collection**   | 2014                  |
| **Attack Categories**    | none                  |
| **Benign Activity**      | Real users            |
|                          |                       |
| **Packed Size**          | 2,3 GB                |
| **Unpacked Size**        | n/a                   |
| **Download Link**        | see below             |

***

### Overview
The "User-Computer Authentication in Time" dataset contains 708.304.516 anonymized authentication events collected over a period of 9 continuous months from the Los Alamos National Laboratory (LANL) enterprise network.
This data was used to study the concept of "Credential Hopping" - where an attacker uses stored/cached credentials on a machine to authenticate on another in the network - and which strategies can be taken to mitigate associated risks.
For this purpose, an "authentication graph" was built from these events and analyzed and/or modified using various assumptions and methodologies.
As it does not contain any known malicious events, it is most likely of little interest for intrusion detection research.

### Environment
Details other than "LANL enterprise network" are not provided, except for some statistical values.
There are a total of 11,362 distinct users, and 22,284 distinct computers.

### Activity
There is no mention of any malicious activity during the collection period.

### Contained Data
The dataset consists of 708,304,516 authentication events, one event per line, each described with three values:
- an epoch timestamp (epoch 1 is the start of the collection period, an exact time is not provided)
- the user who successfully authenticated, in the form of "U" plus a unique number for that user (e.g., U1337)
- the computer the given user authenticated on, in the form of "C" plus a unique number for that computer (e.g., C42)

The authors note that authentication events for some centralized computers, specifically the Active Directory Servers, have been removed.
Access to the dataset can easily be requested on the homepage linked below (the email address you need to supply does not have to be valid).
It can either be downloaded as one text file containing the full nine months (2,3 GB), or nine text files with 30 days of events each.

### Papers
- [Connected Components and Credential Hopping in Authentication Graphs (2014)](https://doi.org/10.1109/SITIS.2014.95)

### Links
- [Homepage](https://csr.lanl.gov/data/auth/)

### Related Entries
- Other LANL datasets:
    - [Comprehensive, Multi-Source Cybersecurity Events](comp_multi_source_cybersec_events.md)
    - [Unified Host and Network Dataset](unified_host_and_network_dataset.md)

### Data Examples
The first 10 lines of the dataset
```
1,U1,C1
1,U1,C2
2,U2,C3
3,U3,C4
6,U4,C5
7,U4,C5
7,U5,C6
8,U6,C7
11,U7,C8
12,U8,C9
```