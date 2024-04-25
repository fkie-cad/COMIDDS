---
title: NF-UQ-NIDS
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                                                                                          |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Network Data Source**  | Custom NetFlows                                                                                                                                   |
| **Network Data Labeled** | Yes                                                                                                                                               |
| **Host Data Source**     | -                                                                                                                                                 |
| **Host Data Labeled**    | -                                                                                                                                                 |
|                          |                                                                                                                                                   |
| **Overall Setting**      | Enterprise IT / Miscellaneous                                                                                                                     |
| **OS Types**             | Windows, Linux, MacOS, IoT                                                                                                                        |
| **Number of Machines**   | n/a                                                                                                                                               |
| **Total Runtime**        | n/a                                                                                                                                               |
| **Year of Collection**   | 2015 / 2018 / 2019                                                                                                                                |
| **Attack Categories**    | DoS / DDoS<br/>Reconnaissance<br/>Injection<br/>Infiltration<br/>Backdoor<br/>Botnet<br/>Shellcode<br/>MITM<br/>Worms<br/>Ransomware<br/>Exploits |
| **Benign Activity**      | Synthetic                                                                                                                                         |
|                          |                                                                                                                                                   |
| **Packed Size**          | 2 GB                                                                                                                                              |
| **Unpacked Size**        | 14,8 GB                                                                                                                                           |
| **Download Link**        | [v1](https://rdm.uq.edu.au/files/76b6edf0-ef9c-11ed-b5f6-b1a04f482c13), [v2](https://rdm.uq.edu.au/files/e2412450-ef9c-11ed-827d-e762de186848)    |

***

### Overview
The NetFlow University of Queensland Network Intrusion Detection Dataset (NF-UQ-NIDS) is a combination of four distinct datasets using a newly proposed set of standardized features.
These datasets are UNSW-NB15 (2015), CSE-CIC-IDS2018 (2018), BoT-IoT (2018), and ToN-IoT (2019) - the former two are also present in this collection (see related entries), while the latter two deal with IoT systems and are thus not included.
The main goal of the authors is the introduction of the aforementioned standard feature set (based on NetFlow v9) to be used with anomaly-based NIDS, facilitating evaluation and comparison between different models and classifiers - efforts which are normally hardly useful due to feature spaces that are almost exclusive from one another.
Additionally, a standardized feature set allows for agglomeration of different datasets, which is precisely what NF-UQ-NIDS is.
Two different feature sets were developed, a shorter version containing twelve features (v1) as well as a longer version made up of 43 features (v2).

### Environment
Details regarding the environment of UNSW-NB15 and CSE-CIC-IDS2018 can be found in their respective entries.
The homepages of BoT-IoT and ToN-IoT are also linked below.

### Activity
Specific details of benign and malicious behavior within a given dataset can again be found using the respective entries/links.
Here, the authors simply condensed all categories of behavior from each dataset into a single list (ordered by frequency of occurrence):
- Benign
- DDoS
- Reconnaissance
- Injection
- DoS
- Brute Force
- Password
- XSS
- Infiltration
- Exploits
- Scanning
- Fuzzers
- Backdoor
- Bot
- Generic
- Analysis
- Theft
- Shellcode
- MITM
- Worms
- Ransomware

### Contained Data
Two different feature set, both based (i.e., a subset) on the NetFlow v9 protocol, were introduced.
The first set, v1, consists of 12 features, the second, v2, of 43.
These features are both listed in the Data Example section below and explained in the cited papers, which also discuss the decisions leading to those selections.

For each version, a separate dataset was generated, aptly named NF-UQ-NIDS and NF-UQ-NIDS-v2.
In both cases, pcaps that were part of the underlying datasets were used to generate NetFlows with the required 12 or 43 features, respectively.
Then, ground truth supplied with each dataset was leveraged to label every generated flow, assigning two labels:
- A binary classifier (benign/malicious)
- An attack category (from those listed in [Activity](#activity))

Additionally, the name of the original dataset a given flow originated from is added as a third label.
Every transformed dataset is also available as a standalone version, available on their homepage.
For example, for UNSW-NB-15, these are named NF-UNSW-NB15 and NF-UNSW-NB15-v2.

### Papers
- [Towards a Standard Feature Set for Network Intrusion Detection System Datasets (2021)](https://doi.org/10.1007/s11036-021-01843-0)
- [NetFlow Datasets for Machine Learning-based Network Intrusion Detection Systems (2021)](https://doi.org/10.48550/arXiv.2011.09144)

### Links
- [Homepage](https://staff.itee.uq.edu.au/marius/NIDS_datasets/)
- [Version 1 Infopage](https://doi.org/10.48610/69b5a53)
- [Version 2 Infopage](https://doi.org/10.48610/631a24a)
- [BoT-IoT Homepage](https://research.unsw.edu.au/projects/bot-iot-dataset)
- [ToN-IoT Homepage](https://research.unsw.edu.au/projects/toniot-datasets)
- [Unrelated](https://xkcd.com/927/)

### Related Entries
- [UNSW-NB15](unsw_nb15.md)
- [CSE-CIC-IDS2018](cse_cic_ids2018.md)

### Data Examples
Snippet of NF-UQ-NIDS taken from `e3bd3035f88e55fa_MOHANAD_A4706/data/NF-UQ-NIDS.csv`
```
212.92.117.95,60829,172.31.68.10,3389,6,0.0,1460,1873,8,7,222,4292940,0,Benign,NF-CSE-CIC-IDS2018
1.186.229.23,49772,172.31.68.10,23,6,77.0,44,0,1,0,2,0,0,Benign,NF-CSE-CIC-IDS2018
172.31.68.10,51753,23.219.88.74,80,6,7.0,1151,1657,17,15,219,4179184,0,Benign,NF-CSE-CIC-IDS2018
172.31.68.10,51754,23.219.88.74,80,6,7.0,1151,1657,17,15,219,4179184,0,Benign,NF-CSE-CIC-IDS2018
172.31.68.10,51763,209.85.202.102,80,6,7.126,1135,1450,17,15,219,4178758,0,Benign,NF-CSE-CIC-IDS2018
172.31.68.10,51762,209.85.202.102,80,6,7.126,1135,1450,17,15,219,4178691,0,Benign,NF-CSE-CIC-IDS2018
172.31.68.10,51761,209.85.202.95,443,6,91.126,126,86,2,1,24,4294811,0,Benign,NF-CSE-CIC-IDS2018
172.31.68.10,51755,216.58.211.162,443,6,91.126,126,86,2,1,24,4294811,0,Benign,NF-CSE-CIC-IDS2018
118.174.147.62,57359,172.31.68.10,3389,6,0.0,1504,1913,9,8,30,4292006,0,Benign,NF-CSE-CIC-IDS2018
172.31.68.10,51767,74.125.197.147,443,6,91.126,126,86,2,1,24,4294858,0,Benign,NF-CSE-CIC-IDS2018
```

NetFlow v1 features taken from `e3bd3035f88e55fa_MOHANAD_A4706/data/NetFlow_v1_Features.csv`
```
Feature,Description
IPV4_SRC_ADDR,IPv4 source address
IPV4_DST_ADDR,IPv4 destination address
L4_SRC_PORT,IPv4 source port number
L4_DST_PORT,IPv4 destination port number
PROTOCOL,IP protocol identifier byte
TCP_FLAGS,Cumulative of all TCP flags
L7_PROTO,Layer 7 protocol (numeric)
IN_BYTES,Incoming number of bytes
OUT_BYTES,Outgoing number of bytes
IN_PKTS,Incoming number of packets
OUT_PKTS,Outgoing number of packets
FLOW_DURATION_MILLISECONDS,Flow duration in milliseconds
```

Snippet of NF-UQ-NIDS-v2 taken from `9810e03bba4983da_MOHANAD_A4706/data/NF-UQ-NIDS-v2.csv`
```
192.168.1.31,44464,192.168.1.193,1040,6,0.0,44,1,40,1,22,2,20,0,0,0,0,0,44,40,40,44,44.0,40.0,0,0,0,0,352000,320000,2,0,0,0,0,1024,0,0,0,0,0,0,0.0,0,Benign,NF-ToN-IoT-v2
192.168.100.147,22188,192.168.100.7,80,17,188.0,84,3,0,0,0,0,0,4293906,1061,0,64,64,28,28,0,28,2856.0,0.0,0,0,0,0,224000,0,3,0,0,0,0,0,0,0,0,0,0,0,0.0,1,DDoS,NF-BoT-IoT-v2
192.168.100.150,41472,192.168.100.3,80,17,188.0,56,2,0,0,0,0,0,4294062,905,0,64,64,28,28,0,28,2828.0,0.0,0,0,0,0,224000,0,2,0,0,0,0,0,0,0,0,0,0,0,0.0,1,DDoS,NF-BoT-IoT-v2
192.168.1.39,60288,192.168.1.1,53,17,0.0,68,1,100,1,0,0,0,0,0,0,0,0,100,68,68,100,68.0,100.0,0,0,0,0,544000,800000,2,0,0,0,0,0,0,0,0,1143,1,35,0.0,1,xss,NF-ToN-IoT-v2
52.14.136.135,52346,172.31.69.28,80,6,7.178,521,5,1147,5,219,219,27,4294920,46,46,127,127,975,40,40,975,521.0,1147.0,0,0,0,0,88000,192000,8,0,1,1,0,65535,26883,0,0,0,0,0,0.0,1,DDoS,NF-CSE-CIC-IDS2018-v2
192.168.1.31,56884,192.168.1.49,2034,6,0.0,44,1,0,0,2,2,0,0,0,0,0,0,44,44,0,44,44.0,0.0,0,0,0,0,352000,0,1,0,0,0,0,1024,0,0,0,0,0,0,0.0,0,Benign,NF-ToN-IoT-v2
192.168.100.150,51388,192.168.100.3,80,6,7.0,320,3,44,1,22,6,18,4292826,2141,0,64,64,140,40,40,140,140180.0,44.0,0,0,0,0,720000,352000,2,2,0,0,0,512,29200,0,0,0,0,0,0.0,1,Reconnaissance,NF-BoT-IoT-v2
192.168.100.147,25087,192.168.100.5,80,17,188.0,56,2,0,0,0,0,0,4293998,969,0,64,64,28,28,0,28,2828.0,0.0,0,0,0,0,224000,0,2,0,0,0,0,0,0,0,0,0,0,0,0.0,1,DDoS,NF-BoT-IoT-v2
59.166.0.8,2426,149.171.126.3,6881,6,0.0,1540,16,1644,18,27,27,27,0,0,0,31,32,329,52,52,329,1540.0,1644.0,506,3,506,3,12320000,13152000,30,0,4,0,0,10136,10136,64000,250,0,0,0,0.0,0,Benign,NF-UNSW-NB15-v2
192.168.1.30,2529,192.168.1.180,12336,6,0.0,48,1,0,0,2,2,0,0,0,0,0,0,48,48,0,48,48.0,0.0,0,0,0,0,384000,0,1,0,0,0,0,4096,0,0,0,0,0,0,0.0,1,scanning,NF-ToN-IoT-v2
```

Netflow v2 features taken from `9810e03bba4983da_MOHANAD_A4706/data/NetFlow_v2_Features.csv`
```
Feature,Description
IPV4_SRC_ADDR,IPv4 source address
IPV4_DST_ADDR,IPv4 destination address
L4_SRC_PORT,IPv4 source port number
L4_DST_PORT,IPv4 destination port number
PROTOCOL,IP protocol identifier byte
L7_PROTO,Layer 7 protocol (numeric)
IN_BYTES,Incoming number of bytes
OUT_BYTES,Outgoing number of bytes
IN_PKTS,Incoming number of packets
OUT_PKTS,Outgoing number of packets
FLOW_DURATION_MILLISECONDS,Flow duration in milliseconds
TCP_FLAGS,Cumulative of all TCP flags
CLIENT_TCP_FLAGS,Cumulative of all client TCP flags
SERVER_TCP_FLAGS,Cumulative of all server TCP flags
DURATION_IN,Client to Server stream duration (msec)
DURATION_OUT,Client to Server stream duration (msec)
MIN_TTL,Min flow TTL
MAX_TTL,Max flow TTL
LONGEST_FLOW_PKT,Longest packet (bytes) of the flow
SHORTEST_FLOW_PKT,Shortest packet (bytes) of the flow
MIN_IP_PKT_LEN,Len of the smallest flow IP packet observed
MAX_IP_PKT_LEN,Len of the largest flow IP packet observed
SRC_TO_DST_SECOND_BYTES,Src to dst Bytes/sec
DST_TO_SRC_SECOND_BYTES,Dst to src Bytes/sec
RETRANSMITTED_IN_BYTES,Number of retransmitted TCP flow bytes (src->dst)
RETRANSMITTED_IN_PKTS,Number of retransmitted TCP flow packets (src->dst)
RETRANSMITTED_OUT_BYTES,Number of retransmitted TCP flow bytes (dst->src)
RETRANSMITTED_OUT_PKTS,Number of retransmitted TCP flow packets (dst->src)
SRC_TO_DST_AVG_THROUGHPUT,Src to dst average thpt (bps)
DST_TO_SRC_AVG_THROUGHPUT,Dst to src average thpt (bps)
NUM_PKTS_UP_TO_128_BYTES,Packets whose IP size <= 128
NUM_PKTS_128_TO_256_BYTES,Packets whose IP size > 128 and <= 256
NUM_PKTS_256_TO_512_BYTES,Packets whose IP size > 256 and <= 512
NUM_PKTS_512_TO_1024_BYTES,Packets whose IP size > 512 and <= 1024
NUM_PKTS_1024_TO_1514_BYTES,Packets whose IP size >��1024 and <= 1514
TCP_WIN_MAX_IN,Max TCP Window (src->dst)
TCP_WIN_MAX_OUT,Max TCP Window (dst->src)
ICMP_TYPE,ICMP Type * 256 + ICMP code
ICMP_IPV4_TYPE,ICMP Type
DNS_QUERY_ID,DNS query transaction Id
DNS_QUERY_TYPE,"DNS query type (e.g. 1=A, 2=NS..)"
DNS_TTL_ANSWER,TTL of the first A record (if any)
FTP_COMMAND_RET_CODE,FTP client command return code
```