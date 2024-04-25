---
title: Comprehensive, Multi-Source Cybersecurity Events
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Example Data](#example-data)

| <!-- -->                 | <!-- -->                                               |
|--------------------------|--------------------------------------------------------|
| **Network Data Source**  | NetFlows, DNS lookups                                  |
| **Network Data Labeled** | No                                                     |
| **Host Data Source**     | Auth events, Process events                            |
| **Host Data Labeled**    | Yes, for auth events                                   |
|                          |                                                        |
| **Overall Setting**      | Enterprise IT                                          |
| **OS Types**             | Windows <br> Others undisclosed                        |
| **Number of Machines**   | 17,684                                                 |
| **Total Runtime**        | 58 days                                                |
| **Year of Collection**   | 2015                                                   |
| **Attack Categories**    | Authentication with stolen credentials                 |
| **Benign Activity**      | Real users                                             |
|                          |                                                        |
| **Packed Size**          | 12 GB                                                  |
| **Unpacked Size**        | n/a                                                    |
| **Download Link**        | [must be requested](https://csr.lanl.gov/data/cyber1/) |

***

### Overview

This data set represents 58 consecutive days of de-identified event data collected from five sources within Los Alamos
National Laboratory’s corporate, internal computer network, including some red team activity.
These events are presented as brief, anonymized one-liners, intended to enable novel research, for example by studying
certain patterns present in such a dataset, which has the benefit of originating from a real production network.
However, the level of detail per event is extremely limited.

### Environment

Exact details besides "corporate, internal computer network" are not provided, except for some statistical values.
Within the network, there are 12.425 users, 17.684 machines, and 62.974 processes.

### Activity

Benign activity is not specified.
At various points in time, a red team performed authentication using stolen user credentials - this is again not further
explained.

### Contained Data

The dataset contains five different types of events, 1.648.275.307 events in total.
Specific details as to how each data entry is structured in detail, what each field means etc., can be easily found on
the homepage.
Events do not consist of the full log, but only contain a small subset of data.

- Authentication events collected from individual Windows-based desktop computers, servers, and Active Directory
  servers.
- Process start and stop events collected from individual Windows-based desktop computers and servers.
- Network flow events collected from central routers within the network.
    - due to a configuration error, this data is only available for the first 29 days
- DNS lookup events collected from the central DNS servers within the network.
- Specific events taken from the authentication data that presents known red team compromise events.

Further details regarding each data source are available in section 4.1 through 4.5 of the cited paper.
The dataset has been anonymized uniformly, i.e., entity names match across data sources.
In addition, anything allowing for association outside the lab network has been removed.
Data is partially labeled in the sense that the fifth event type, the redteam events, can be used as limited ground
truth for some malicious behavior.
The authors note that other indicators of compromise may exist throughout the dataset, but they have not been validated
or correlated.

### Papers

- [Cybersecurity Data Sources for Dynamic Network Research (2016)](https://doi.org/10.1142/9781786340757_0002)

### Links

- [Homepage](https://csr.lanl.gov/data/cyber1/)
    - Data access must be requested here

### Related Entries
- Other LANL datasets:
    - [Unified Host and Network Dataset](unified_host_and_network_dataset.md)
    - [User-Computer Authentication Associations in Time](user_computer_associations.md)

### Example Data

Authentication events in `auth.txt`

```shell
# time,source user@domain,destination user@domain,source computer,destination computer,authentication type,logon type,authentication orientation,success/failure
1,C625$@DOM1,U147@DOM1,C625,C625,Negotiate,Batch,LogOn,Success
1,C653$@DOM1,SYSTEM@C653,C653,C653,Negotiate,Service,LogOn,Success
1,C660$@DOM1,SYSTEM@C660,C660,C660,Negotiate,Service,LogOn,Success
```

Process events in `proc.txt`

```shell
# time,user@domain,computer,process name,start/end
1,C553$@DOM1,C553,P16,Start
1,C553$@DOM1,C553,P25,End
1,C553$@DOM1,C553,P25,Start
```

Network flow events in `flows.txt`

```shell
# time,duration,source computer,source port,destination computer,destination port,protocol,packet count,byte count
1,9,C3090,N10471,C3420,N46,6,3,144
1,9,C3538,N2600,C3371,N46,6,3,144
2,0,C4316,N10199,C5030,443,6,2,92
```

DNS lookup events in `dns.txt`

```shell
# time,source computer,computer resolved
31,C161,C2109
35,C5642,C528
38,C3380,C22841
```

Process events in `redteam.txt`

```shell
# time,user@domain,source computer,destination computer
151648,U748@DOM1,C17693,C728
151993,U6115@DOM1,C17693,C1173
153792,U636@DOM1,C17693,C294
```