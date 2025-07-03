---
title: UNR-IDD
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------ |
| **Network Data Source**  | Port statistics, selected flow features                                                    |
| **Network Data Labeled** | Yes                                                                                        |
| **Host Data Source**     | -                                                                                          |
| **Host Data Labeled**    | -                                                                                          |
|                          |                                                                                            |
| **Overall Setting**      | Miscellaneous                                                                              |
| **OS Types**             | Linux                                                                                      |
| **Number of Machines**   | 10 virtual hosts, 12 switches                                                              |
| **Total Runtime**        | n/a                                                                                        |
| **Year of Collection**   | 2023                                                                                       |
| **Attack Categories**    | TCP-SYN flood<br>Port scan<br>Flow table overflow<br>Backhole<br>Diversion                 |
| **User Emulation**       | Synthetic                                                                                  |
|                          |                                                                                            |
| **Packed Size**          | -                                                                                          |
| **Unpacked Size**        | 5,3 MB                                                                                     |
| **Download Link**        | [goto](https://drive.google.com/file/d/1ANnT1g7NjbGGOvL1uHDHEQF_Dzx9kK3f/view?usp=sharing) |

***

### Overview
The "University of Nevada - Intrusion Detection Dataset" (UNR-IDD) is centered around a Software-defined Network (SDN), designed for evaluating machine-learning-based intrusion detection systems.
It focuses on port-level and delta port-level statistics rather than purely flow-level features while aiming to achieve equal representation of all classes to avoid the need for over- or undersampling.

### Environment
A [Mininet](https://mininet.org/)-based testbed with 12 Open vSwitches and 10 virtual hosts was generated, controlled by an ONOS SDN controller (OpenFlow 1.4).
The authors note that this design choice allows for straightforward reproduction and modification of this generation process.
All measurements (port statistics, flow table usage, etc.) occurred on a single Linux machine.
Refer to the cited paper for further setup details.

### Activity
For benign user emulation, a Python script triggers iPerf transmissions (TCP/UDP) between two randomly chosen hosts every 5 seconds, with set bandwidth and duration parameters.
Malicious behavior is achieved via various scripts and configuration changes causing associated malicious network patterns:
- TCP-SYN flood (script repeatedly sends large bursts of SYN packets)
- Port scans (tools like nmap probe open ports on target hosts)
- Flow table overflow (quickly installs many new flow entries on switches)
- Blackhole/Diversion (manipulates flow rules so that traffic is silently dropped or rerouted to unintended paths)

### Contained Data
Data is collected via periodical snapshots from switches (every 5 seconds).
These snapshots include:
- Cumulative port stats: (packets, bytes, errors, drops)
- Delta port stats: changes in these values over 5-second intervals
- Flow table stats: partial data on flows, table size, etc.

Entries are labeled both by class and in binary form, though the labeling process is not detailed.

### Papers
- [UNR-IDD: Intrusion Detection Dataset using Network Port Statistics](https://doi.org/10.1109/CCNC51644.2023.10059640)

### Links
- [Homepage](https://www.tapadhirdas.com/das-lab/datasets/unr-idd)
- [Mininet](https://mininet.org/)

### Data Examples
Snippet of `UNR-IDD.csv`

<!--  {% raw %} -->
```
Switch ID,Port Number,Received Packets,Received Bytes,Sent Bytes,Sent Packets,Port alive Duration (S),Packets Rx Dropped,Packets Tx Dropped,Packets Rx Errors,Packets Tx Errors,Delta Received Packets,Delta Received Bytes,Delta Sent Bytes,Delta Sent Packets,Delta Port alive Duration (S),Delta Packets Rx Dropped, Delta Packets Tx Dropped,Delta Packets Rx Errors,Delta Packets Tx Errors,Connection Point,Total Load/Rate,Total Load/Latest,Unknown Load/Rate,Unknown Load/Latest,Latest bytes counter,is_valid,Table ID,Active Flow Entries,Packets Looked Up,Packets Matched,Max Size,Label,Binary Label
of:000000000000000c,Port#:1,132,9181,6311853,238,46,0,0,0,0,0,0,280,2,5,0,0,0,0,1,0,0,0,0,0,TRUE,0,9,767,688,-1,TCP-SYN,Attack
of:000000000000000c,Port#:2,187,6304498,15713,171,46,0,0,0,0,146,5908166,5969,84,5,0,0,0,0,2,0,0,0,0,0,TRUE,0,9,767,688,-1,TCP-SYN,Attack
of:000000000000000c,Port#:3,235,6311567,8030,58,46,0,0,0,0,2,278,280,2,5,0,0,0,0,3,0,0,0,0,0,TRUE,0,9,767,688,-1,TCP-SYN,Attack
of:000000000000000c,Port#:4,59,7878,16439,182,46,0,0,0,0,2,278,280,2,5,0,0,0,0,4,0,0,0,0,0,TRUE,0,9,767,688,-1,TCP-SYN,Attack
of:000000000000000a,Port#:1,188,6304547,16497,183,46,0,0,0,0,0,0,280,2,5,0,0,0,0,1,0,0,0,0,0,TRUE,0,7,489,403,-1,TCP-SYN,Attack
of:000000000000000a,Port#:2,10,856,8130,60,46,0,0,0,0,0,0,280,2,5,0,0,0,0,2,0,0,0,0,0,TRUE,0,7,489,403,-1,TCP-SYN,Attack
of:000000000000000a,Port#:3,60,8082,6311515,233,46,0,0,0,0,2,278,280,2,5,0,0,0,0,3,0,0,0,0,0,TRUE,0,7,489,403,-1,TCP-SYN,Attack
of:000000000000000a,Port#:4,179,16055,8040,59,46,0,0,0,0,2,278,280,2,5,0,0,0,0,5,0,0,0,0,0,TRUE,0,7,489,403,-1,TCP-SYN,Attack
of:000000000000000b,Port#:1,121,8487,6311952,239,46,0,0,0,0,79,5491,5777176,145,5,0,0,0,0,1,0,0,0,0,0,TRUE,0,7,409,353,-1,TCP-SYN,Attack
of:000000000000000b,Port#:2,60,8114,8198,62,46,0,0,0,0,2,280,280,2,5,0,0,0,0,2,0,0,0,0,0,TRUE,0,7,409,353,-1,TCP-SYN,Attack
of:0000000000000003,Port#:1,11,946,8214,62,46,0,0,0,0,0,0,278,2,5,0,0,0,0,1,0,0,0,0,0,TRUE,0,8,1233,1145,-1,TCP-SYN,Attack
of:0000000000000003,Port#:2,512,29635,6332447,621,46,0,0,0,0,100,5400,5678,102,5,0,0,0,0,2,-1501,0,-1501,0,-1501,TRUE,0,8,1233,1145,-1,TCP-SYN,Attack
of:0000000000000003,Port#:3,232,6311393,36529,556,46,0,0,0,0,2,278,5678,102,5,0,0,0,0,3,-1501,0,-1501,0,-1501,TRUE,0,8,1233,1145,-1,TCP-SYN,Attack
of:0000000000000003,Port#:4,446,28882,8124,61,46,0,0,0,0,102,5678,278,2,5,0,0,0,0,4,0,0,0,0,0,TRUE,0,8,1233,1145,-1,TCP-SYN,Attack
of:0000000000000004,Port#:1,444,28798,7966,58,46,0,0,0,0,101,5624,278,2,5,0,0,0,0,1,0,0,0,0,0,TRUE,0,5,605,516,-1,TCP-SYN,Attack
of:0000000000000004,Port#:2,61,8124,28882,446,46,0,0,0,0,2,278,5624,101,5,0,0,0,0,2,567,20682,567,20682,567,TRUE,0,5,605,516,-1,TCP-SYN,Attack
of:0000000000000004,Port#:3,55,7840,8008,59,46,0,0,0,0,2,278,278,2,5,0,0,0,0,3,0,0,0,0,0,TRUE,0,5,605,516,-1,TCP-SYN,Attack
of:0000000000000001,Port#:1,11,942,8098,60,46,0,0,0,0,0,0,278,2,5,0,0,0,0,1,0,0,0,0,0,TRUE,0,6,940,857,-1,TCP-SYN,Attack
of:0000000000000001,Port#:2,396,21676,28876,445,46,0,0,0,0,99,5346,5624,101,5,0,0,0,0,2,540,20412,540,20412,540,TRUE,0,6,940,857,-1,TCP-SYN,Attack
of:0000000000000001,Port#:3,442,28702,8008,59,46,0,0,0,0,101,5624,278,2,5,0,0,0,0,3,0,0,0,0,0,TRUE,0,6,940,857,-1,TCP-SYN,Attack
```
<!--  {% endraw %} -->