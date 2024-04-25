---
title: ISCX IDS 2012
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                       |
|--------------------------|--------------------------------------------------------------------------------|
| **Network Data Source**  | pcaps                                                                          |
| **Network Data Labeled** | Yes                                                                            |
| **Host Data Source**     | -                                                                              |
| **Host Data Labeled**    | -                                                                              |
|                          |                                                                                |
| **Overall Setting**      | Enterprise IT                                                                  |
| **OS Types**             | Windows XP SP1/SP2<br/>Windows 7<br/>Windows Server 2003<br/>Ubuntu 10.04      |
| **Number of Machines**   | 23                                                                             |
| **Total Runtime**        | 7 days                                                                         |
| **Year of Collection**   | 2012                                                                           |
| **Attack Categories**    | Infiltration from Inside<br/>DoS/DDoS<br/>Brute Force                          |
| **Benign Activity**      | Synthetic, dedicated profiles generating traffic on various protocols/services |
|                          |                                                                                |
| **Packed Size**          | 84 GB                                                                          |
| **Unpacked Size**        | 87 GB                                                                          |
| **Download Link**        | Tricky, see links below                                                        |

***

### Overview

This dataset is a product of the authors defining a number of criteria a NIDS evaluation dataset should fulfil, followed
by the creation of such a dataset, using the notion of alpha- and beta-profiles to describe attacker and normal
behavior, respectively.
Special attention was paid to the creation of the latter to ensure realistic traffic generation, which was done by
observing their own operational network, analyzing frequency and composition of used services and abstracting them into
numerical descriptions.

### Environment

The testbed architecture consists of 21 interconnected Windows workstations running Windows XP SP1/2 and Windows 7.
There are a total of six networks, with these 21 workstations being divided between the first four.
The fifth network contains two servers running Ubuntu 10.04 and Windows Server 2003, providing company functionality
like email services and serving websites.
The sixth network is designed for monitoring and maintenance purposes.

### Activity

How beta-profiles (aka user behavior) are realized for each protocol (HTTP, SMTP/IMAP, FTP, SSH)within that testbed is
explained in chapter 3 and 4 of the referenced paper.
The testbed ran for exactly seven days, during which four separate attack campaigns (the alpha-profiles) were executed,
with each campaign consisting of five stages:

- Information gathering and reconnaissance
- Vulnerability identification and scanning
- Gaining access and compromising a system
- Maintaining access and creating backdoors
- Covering tracks

Each scenario is explained in more detail in sections 5.1 to 5.4 of the paper. The scenarios are:

- Infiltrating the network from the inside
- HTTP DoS
- DDoS using an IRC botnet
- brute force SSH

### Contained Data

Data is divided into seven pcap files, one for each day.
Additionally, for each day there are labeled flows available as `.xml` files (see example data).
These should enable to label the available pcap data at least partially.

### Papers

- [Toward Developing a Systematic Approach to Generate Benchmark Datasets for Intrusion Detection (2012)](https://doi.org/10.1016/j.cose.2011.12.012)

### Links

- [Homepage](https://www.unb.ca/cic/datasets/ids.html)
    - download source appears unstable, use `wget` on loop until one of the attempts gets through (took me ~20)
        - `wget http://205.174.165.80/CICDataset/ISCX-IDS-2012/Dataset/labeled_flows_xml.zip`
        - `wget http://205.174.165.80/CICDataset/ISCX-IDS-2012/Dataset/testbed-11jun.pcap`
        - `wget http://205.174.165.80/CICDataset/ISCX-IDS-2012/Dataset/testbed-12jun.pcap`
        - `wget http://205.174.165.80/CICDataset/ISCX-IDS-2012/Dataset/testbed-13jun.pcap`
        - `wget http://205.174.165.80/CICDataset/ISCX-IDS-2012/Dataset/testbed-14jun.pcap`
        - `wget http://205.174.165.80/CICDataset/ISCX-IDS-2012/Dataset/testbed-15jun.pcap`
        - `wget http://205.174.165.80/CICDataset/ISCX-IDS-2012/Dataset/testbed-16jun.pcap`
        - `wget http://205.174.165.80/CICDataset/ISCX-IDS-2012/Dataset/testbed-17jun.pcap`

### Data Examples

Example labeled flow taken from `labeled_flows_xml/TestbedTueJun15-1Flows.xml`

```xml
<TestbedTueJun15-1Flows>
<appName>SSH</appName>
<totalSourceBytes>358</totalSourceBytes>
<totalDestinationBytes>257</totalDestinationBytes>
<totalDestinationPackets>3</totalDestinationPackets>
<sensorInterfaceId>1</sensorInterfaceId>
<totalSourcePackets>5</totalSourcePackets>
<sourcePayloadAsBase64></sourcePayloadAsBase64>
<sourcePayloadAsUTF></sourcePayloadAsUTF>
<destinationPayloadAsBase64></destinationPayloadAsBase64>
<destinationPayloadAsUTF></destinationPayloadAsUTF>
<direction>R2L</direction>
<sourceTCPFlagsDescription>F,S,A</sourceTCPFlagsDescription>
<destinationTCPFlagsDescription>F,S,P,A</destinationTCPFlagsDescription>
<source>212.77.187.249</source>
<protocolName>tcp_ip</protocolName>
<sourcePort>22373</sourcePort>
<destination>192.168.5.122</destination>
<destinationPort>22</destinationPort>
<startDateTime>2010-06-15T02:58:25</startDateTime>
<stopDateTime>2010-06-15T02:58:25</stopDateTime>
<Tag>Attack</Tag>
</TestbedTueJun15-1Flows>
```