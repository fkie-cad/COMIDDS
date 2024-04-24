---
title: Kyoto Honeypot Dataset
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                |
|--------------------------|-------------------------------------------------------------------------|
| **Network Data Source**  | Features extracted from network traffic                                 |
| **Network Data Labeled** | Yes                                                                     |
| **Host Data Source**     | -                                                                       |
| **Host Data Labeled**    | -                                                                       |
|                          |                                                                         |
| **Overall Setting**      | Diverse                                                                 |
| **OS Types**             | Windows XP/2000 Server/Vista<br/>MacOs<br/>Solaris 8<br/>Various others |
| **Number of Machines**   | 32                                                                      |
| **Total Runtime**        | 9 years                                                                 |
| **Year of Collection**   | 2006-2015                                                               |
| **Attack Categories**    | n/a (it's a honeypot)                                                   |
| **Benign Activity**      | Synthetic, automated "normal traffic generation"                        |
|                          |                                                                         |
| **Packed Size**          | 5 GB                                                                    |
| **Unpacked Size**        | n/a                                                                     |
| **Download Link**        | [goto](http://www.takakura.com/Kyoto_data/new_data201704/)              |

***

### Overview

This dataset originated from a collection of honeypots located at the University of Kyoto, from which traffic data was
collected over the span over 9 years (2006-2015).
It is made available with the intent to provide insights into the state of cyberattacks at the time, and to facilitate
IDS research.

### Environment

The environment consists of a total of 348 honeypots, though 318 of those originate from two machines which they call "
black hole sensors" covering 318 IP addresses.
The remaining machines are a diverse mix of Windows, Linux, macOS, IoT and home devices in various states of patching,
distributed over 5 different networks.

### Activity

Due to the nature of honeypots, malicious activity can only be described in retrospect.
Most honeypots were immediately reset upon becoming an attack victim, others were allowed to run over a longer period of
time (though outgoing traffic was filtered to prevent things like active botnets).
Two additional servers are responsible for "normal traffic generation" by generating mail and DNS traffic, combined with
some other protocols like ssh, http and https.

### Contained Data

All data originating from these servers is labeled as normal, while all data to and from honeypots is generally
considered malicious.
This malicious data was then analyzed using a variety of IDSs and AntiVirus tools to assign them an attack category.

Data is only available in the form of features, which are divided into 14 "conventional" and 10 additional features.
Further explanations for each feature are available in the docs linked below or in sections 4.1 and 4.2 of the paper.

- Conventional:
    - Duration
    - Service
    - Source Bytes
    - Destination Bytes
    - Count
    - Same_srv_rate
    - Srv_serror_rate
    - Dst_host_count
    - Dst_host_svr_count
    - Dst_host_same_src_port_rate
    - Dst_host_serror_rate
    - Dst_host_svr_serror_rate
    - Flag
- Additional
    - IDS_detection
    - Malware_detection
    - Ashula_detection
    - Label
    - Source_IP_Address
    - Source_Port_Number
    - Destination_IP_Address
    - Destination_Port_Number
    - Start_Time
    - Protocol

Note that source and destination IPs have been anonymized.
More insights, such as attack distributions by country etc. are also available in the referenced paper.

### Papers

- [Statistical Analysis of Honeypot Data and Building of Kyoto 2006+ Dataset for NIDS Evaluation (2011)](https://doi.org/10.1145/1978672.1978676)

### Links

- [Homepage](http://www.takakura.com/Kyoto_data/)
    - [Most recent dataset download](http://www.takakura.com/Kyoto_data/new_data201704/)
    - [Docs](http://www.takakura.com/Kyoto_data/BenchmarkData-Description-New.pdf)

### Data Examples

Example taken from `2015/05/20150520.txt`

```
[...]
0.000000	dns	0	0	0	0.00	0.00	0.12	0	0	0.00	0.00	0.00	S0	0	0	0	-1	fd43:4d02:8d72:8f3f:273a:25b1:314f:1212	38486	fd43:4d02:8d72:04f3:7d37:277a:6087:47da	137	11:05:40	udp
0.000071	dns	58	107	4	0.25	0.00	0.22	1	1	0.00	0.00	0.00	SF	0	0	0	-1	fd43:4d02:8d72:7667:3669:284c:0f52:08a0	32457	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	53	11:05:40	udp
0.000351	dns	42	101	6	1.00	0.00	0.20	93	93	0.00	0.00	0.00	SF	0	0	0	-1	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	54475	fd43:4d02:8d72:5785:7d6b:2761:7dcb:3c86	53	11:05:40	udp
0.000363	dns	42	101	7	1.00	0.00	0.18	93	93	0.00	0.00	0.00	SF	0	0	0	-1	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	59322	fd43:4d02:8d72:5785:7d6b:2761:7dcb:3c86	53	11:05:40	udp
0.000465	dns	45	105	8	1.00	0.00	0.17	93	93	0.00	0.00	0.00	SF	0	0	0	-1	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	58057	fd43:4d02:8d72:5785:7d6b:2761:7dcb:3c86	53	11:05:40	udp
0.640337	ssh	605	2605	5	0.60	0.00	0.00	54	53	0.00	0.00	0.00	RSTO	0	0	0	-1	fd43:4d02:8d72:4662:19cd:2ab9:03ed:0054	39607	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	22	11:05:40	tcp
0.646751	ssh	605	2605	6	0.67	0.00	0.00	55	54	0.00	0.00	0.00	RSTO	6-128-1(1)	0	0	-1	fd43:4d02:8d72:4662:19cd:2ab9:03ed:0054	39862	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	22	11:05:40	tcp
0.839961	ssh	605	2605	3	1.00	0.00	0.00	42	42	0.00	0.00	0.00	RSTO	0	0	0	-1	fd43:4d02:8d72:6ee8:116b:6e61:64f6:3353	50071	fd43:4d02:8d72:bb50:7d0e:2711:613e:31fe	22	11:05:40	tcp
3.005500	other	0	0	0	0.00	0.00	1.00	0	13	0.00	0.00	1.00	REJ	0	0	0	-1	fd43:4d02:8d72:2673:49a0:3330:5412:0335	55017	fd43:4d02:8d72:1088:7d76:27d5:6108:2f85	25	11:05:40	tcp
0.000300	dns	42	101	5	1.00	0.00	0.22	93	93	0.00	0.00	0.00	SF	0	0	0	-1	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	56458	fd43:4d02:8d72:5785:7d6b:2761:7dcb:3c86	53	11:05:41	udp
0.000313	dns	45	105	6	1.00	0.00	0.20	93	93	0.00	0.00	0.00	SF	0	0	0	-1	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	37735	fd43:4d02:8d72:5785:7d6b:2761:7dcb:3c86	53	11:05:41	udp
0.648476	ssh	605	2605	5	0.60	0.00	0.00	54	53	0.00	0.00	0.00	RSTO	0	0	0	-1	fd43:4d02:8d72:4662:19cd:2ab9:03ed:0054	40173	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	22	11:05:41	tcp
0.831881	ssh	605	2605	3	1.00	0.00	0.00	42	42	0.00	0.00	0.00	RSTO	0	0	0	-1	fd43:4d02:8d72:6ee8:116b:6e61:64f6:3353	50246	fd43:4d02:8d72:bb50:7d0e:2711:613e:31fe	22	11:05:41	tcp
2.899109	other	0	0	0	0.00	0.00	0.00	57	59	0.00	0.93	0.90	S0	0	0	0	-1	fd43:4d02:8d72:676c:4a2d:0292:59f1:17b0	2196	fd43:4d02:8d72:da1f:7d5c:27c8:61d5:034a	445	11:05:41	tcp
0.000302	dns	42	101	5	1.00	0.00	0.14	93	93	0.00	0.00	0.00	SF	0	0	0	-1	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	65107	fd43:4d02:8d72:5785:7d6b:2761:7dcb:3c86	53	11:05:42	udp
0.000317	dns	42	101	6	1.00	0.00	0.12	93	93	0.00	0.00	0.00	SF	0	0	0	-1	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	59953	fd43:4d02:8d72:5785:7d6b:2761:7dcb:3c86	53	11:05:42	udp
0.000329	dns	45	105	7	1.00	0.00	0.11	93	93	0.00	0.00	0.00	SF	0	0	0	-1	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	40839	fd43:4d02:8d72:5785:7d6b:2761:7dcb:3c86	53	11:05:42	udp
0.637261	ssh	605	2605	4	0.75	0.00	0.00	54	53	0.00	0.00	0.00	RSTO	0	0	0	-1	fd43:4d02:8d72:4662:19cd:2ab9:03ed:0054	40716	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	22	11:05:42	tcp
0.642879	ssh	605	2605	5	0.80	0.00	0.00	55	54	0.00	0.00	0.00	RSTO	0	0	0	-1	fd43:4d02:8d72:4662:19cd:2ab9:03ed:0054	40444	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	22	11:05:42	tcp
0.832930	ssh	605	2605	2	1.00	0.00	0.00	42	42	0.00	0.00	0.00	RSTO	0	0	0	-1	fd43:4d02:8d72:6ee8:116b:6e61:64f6:3353	50404	fd43:4d02:8d72:bb50:7d0e:2711:613e:31fe	22	11:05:42	tcp
3.010032	other	0	0	0	0.00	0.00	0.50	0	0	0.00	0.00	0.00	S0	0	0	0	-1	fd43:4d02:8d72:146f:1575:0fd7:0557:3579	59593	fd43:4d02:8d72:99d9:7de7:279d:6081:1b1d	86	11:05:42	tcp
0.000311	dns	45	105	5	1.00	0.00	0.00	93	93	0.00	0.00	0.00	SF	0	0	0	-1	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	64619	fd43:4d02:8d72:5785:7d6b:2761:7dcb:3c86	53	11:05:43	udp
0.000389	dns	42	101	6	1.00	0.00	0.00	93	93	0.00	0.00	0.00	SF	0	0	0	-1	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	28278	fd43:4d02:8d72:5785:7d6b:2761:7dcb:3c86	53	11:05:43	udp
0.000471	dns	45	105	7	1.00	0.00	0.00	93	93	0.00	0.00	0.00	SF	0	0	0	-1	fd43:4d02:8d72:bce0:7dd7:27f8:6161:37ad	12111	fd43:4d02:8d72:5785:7d6b:2761:7dcb:3c86	53	11:05:43	udp
[...]
```