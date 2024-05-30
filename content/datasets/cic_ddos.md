---
title: CICDDos2019 
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                      |
|--------------------------|---------------------------------------------------------------|
| **Network Data Source**  | pcaps, NetFlows                                               |
| **Network Data Labeled** | Flows are labeled                                             |
| **Host Data Source**     | Windows event logs, Ubuntu event logs                         |
| **Host Data Labeled**    | No                                                            |
|                          |                                                               |
| **Overall Setting**      | Enterprise IT                                                 |
| **OS Types**             | Windows Vista/7/8.1/10<br/>Ubuntu 16.04<br/>Fortinet          |
| **Number of Machines**   | 6                                                             |
| **Total Runtime**        | ~16 hours                                                     |
| **Year of Collection**   | 2019                                                          |
| **Attack Categories**    | Various DDoS attacks                                          |
| **Benign Activity**      | Synthetic, models complex behavior                            |
|                          |                                                               |
| **Packed Size**          | 24,4 GB                                                       |
| **Unpacked Size**        | n/a                                                           |
| **Download Link**        | [goto](http://205.174.165.80/CICDataset/CICDDoS2019/Dataset/) |

***

### Overview
The CICDDos2019 dataset, developed by the Canadian Institute for Cybersecurity (CIC), was created to enable evaluation of new DDoS detection methods, which, according to the authors, was not possible with previously existing datasets containing DDoS attacks.
The dataset is accompanied by a newly proposed taxonomy for DDoS attacks, dividing them into several subclasses.
These attacks are then executed within a small testbed, consisting of a victim network performing benign behavior and a separate attacker network.
This simulation was run on two separate days, namely training and testing day;
data was collected in the form of pcaps, which are then processed into labeled NetFlows.

### Environment
The victim network consists of four Windows machines (Vista/7/8.1/10), an Ubuntu 16.04 Web Server and a firewall.
Information regarding software is not available, IPs of individual machines can be found on the homepage.
Attacks originate from a separate attacker network, which is also not further detailed.

### Activity
So-called B(enign)-Profiles are leveraged to define normal behavior which is performed during the collection period;
this simulates 25 distinct users interacting with HTTP, HTTPS, FTP, SSH, and email-protocols.
Statistics for these interactions have been derived from observing real human behavior.

Executed attacks are based on the newly proposed taxonomy of DDoS attacks, for details regarding this refer to Chapter 3 of the cited paper.
On the first day (training day), 12 different DDoS attacks were executed at different points in time.
On the second day (testing day), a subset of 5 of these attacks were executed, plus a sixth one that was not performed previously.

### Contained Data
Attacks were exclusively executed within the collection period, i.e., no attack is running when data collection starts.
Data is organized per day and consists of pcaps, which were then processed into NetFlows using CICFlowMeter and subsequently labeled.
These flows are grouped by attack in separate `csv` files, but there are no flows available for benign behavior.
While these probably could be extracted manually from the available pcaps, I'm honestly not quite sure why they weren't included in the first place.

A detailed analysis of these flows, especially with respect to the effects of individual attacks on certain features, is available in Chapter 5 of the paper.

### Papers
- [Developing Realistic Distributed Denial of Service (DDoS) Attack Dataset and Taxonomy (2019)](https://doi.org/10.1109/CCST.2019.8888419)

### Links
- [Homepage](https://www.unb.ca/cic/datasets/ddos-2019.html)
- [Download](http://205.174.165.80/CICDataset/CICDDoS2019/Dataset/)

### Data Examples
Labeled flows taken from `CSVs/CSV-03-11/Portmap.csv`
```
Unnamed: 0,Flow ID, Source IP, Source Port, Destination IP, Destination Port, Protocol, Timestamp, Flow Duration, Total Fwd Packets, Total Backward Packets,Total Length of Fwd Packets, Total Length of Bwd Packets, Fwd Packet Length Max, Fwd Packet Length Min, Fwd Packet Length Mean, Fwd Packet Length Std,Bwd Packet Length Max, Bwd Packet Length Min, Bwd Packet Length Mean, Bwd Packet Length Std,Flow Bytes/s, Flow Packets/s, Flow IAT Mean, Flow IAT Std, Flow IAT Max, Flow IAT Min,Fwd IAT Total, Fwd IAT Mean, Fwd IAT Std, Fwd IAT Max, Fwd IAT Min,Bwd IAT Total, Bwd IAT Mean, Bwd IAT Std, Bwd IAT Max, Bwd IAT Min,Fwd PSH Flags, Bwd PSH Flags, Fwd URG Flags, Bwd URG Flags, Fwd Header Length, Bwd Header Length,Fwd Packets/s, Bwd Packets/s, Min Packet Length, Max Packet Length, Packet Length Mean, Packet Length Std, Packet Length Variance,FIN Flag Count, SYN Flag Count, RST Flag Count, PSH Flag Count, ACK Flag Count, URG Flag Count, CWE Flag Count, ECE Flag Count, Down/Up Ratio, Average Packet Size, Avg Fwd Segment Size, Avg Bwd Segment Size, Fwd Header Length.1,Fwd Avg Bytes/Bulk, Fwd Avg Packets/Bulk, Fwd Avg Bulk Rate, Bwd Avg Bytes/Bulk, Bwd Avg Packets/Bulk,Bwd Avg Bulk Rate,Subflow Fwd Packets, Subflow Fwd Bytes, Subflow Bwd Packets, Subflow Bwd Bytes,Init_Win_bytes_forward, Init_Win_bytes_backward, act_data_pkt_fwd, min_seg_size_forward,Active Mean, Active Std, Active Max, Active Min,Idle Mean, Idle Std, Idle Max, Idle Min,SimillarHTTP, Inbound, Label
[...]
162471,172.16.0.5-192.168.50.4-932-44723-17,172.16.0.5,932,192.168.50.4,44723,17,2018-11-03 10:01:35.983831,1,2,0,458.0,0.0,229.0,229.0,229.0,0.0,0.0,0.0,0.0,0.0,4.58E8,2000000.0,1.0,0.0,1.0,1.0,1.0,1.0,0.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,40,0,2000000.0,0.0,229.0,229.0,229.0,0.0,0.0,0,0,0,0,0,0,0,0,0.0,343.5,229.0,0.0,40,0,0,0,0,0,0,2,458,0,0,-1,-1,1,20,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,1,Portmap
61268,172.16.0.5-192.168.50.4-933-39983-17,172.16.0.5,933,192.168.50.4,39983,17,2018-11-03 10:01:35.984211,1,2,0,458.0,0.0,229.0,229.0,229.0,0.0,0.0,0.0,0.0,0.0,4.58E8,2000000.0,1.0,0.0,1.0,1.0,1.0,1.0,0.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,40,0,2000000.0,0.0,229.0,229.0,229.0,0.0,0.0,0,0,0,0,0,0,0,0,0.0,343.5,229.0,0.0,40,0,0,0,0,0,0,2,458,0,0,-1,-1,1,20,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,1,Portmap
27258,172.16.0.5-192.168.50.4-934-26737-17,172.16.0.5,934,192.168.50.4,26737,17,2018-11-03 10:01:35.984213,1,2,0,458.0,0.0,229.0,229.0,229.0,0.0,0.0,0.0,0.0,0.0,4.58E8,2000000.0,1.0,0.0,1.0,1.0,1.0,1.0,0.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,40,0,2000000.0,0.0,229.0,229.0,229.0,0.0,0.0,0,0,0,0,0,0,0,0,0.0,343.5,229.0,0.0,40,0,0,0,0,0,0,2,458,0,0,-1,-1,1,20,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,1,Portmap
85566,172.16.0.5-192.168.50.4-648-21313-17,172.16.0.5,648,192.168.50.4,21313,17,2018-11-03 10:01:35.984783,2,2,0,458.0,0.0,229.0,229.0,229.0,0.0,0.0,0.0,0.0,0.0,2.29E8,1000000.0,2.0,0.0,2.0,2.0,2.0,2.0,0.0,2.0,2.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,40,0,1000000.0,0.0,229.0,229.0,229.0,0.0,0.0,0,0,0,0,0,0,0,0,0.0,343.5,229.0,0.0,40,0,0,0,0,0,0,2,458,0,0,-1,-1,1,20,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,1,Portmap
108025,172.16.0.5-192.168.50.4-935-15051-17,172.16.0.5,935,192.168.50.4,15051,17,2018-11-03 10:01:35.984786,0,2,0,530.0,0.0,265.0,265.0,265.0,0.0,0.0,0.0,0.0,0.0,Infinity,Infinity,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,40,0,0.0,0.0,265.0,265.0,265.0,0.0,0.0,0,0,0,0,0,0,0,0,0.0,397.5,265.0,0.0,40,0,0,0,0,0,0,2,530,0,0,-1,-1,1,20,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,1,Portmap
87041,172.16.0.5-192.168.50.4-936-49469-17,172.16.0.5,936,192.168.50.4,49469,17,2018-11-03 10:01:35.985305,2,2,0,458.0,0.0,229.0,229.0,229.0,0.0,0.0,0.0,0.0,0.0,2.29E8,1000000.0,2.0,0.0,2.0,2.0,2.0,2.0,0.0,2.0,2.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,40,0,1000000.0,0.0,229.0,229.0,229.0,0.0,0.0,0,0,0,0,0,0,0,0,0.0,343.5,229.0,0.0,40,0,0,0,0,0,0,2,458,0,0,-1,-1,1,20,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,1,Portmap
```