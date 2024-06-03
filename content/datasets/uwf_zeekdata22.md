---
title: UWF-ZeekData22
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
| **Network Data Source**  | pcaps, Zeek logs                                                               |
| **Network Data Labeled** | Yes                                                                            |
| **Host Data Source**     | -                                                                              |
| **Host Data Labeled**    | -                                                                              |
|                          |                                                                                |
| **Overall Setting**      | Enterprise IT                                                                  |
| **OS Types**             | Windows 10/2008 Metasploitable3<br/>Debian 11<br/>Ubuntu 14.04 Metasploitable3 |
| **Number of Machines**   | 6                                                                              |
| **Total Runtime**        | 64 days                                                                        |
| **Year of Collection**   | 2022                                                                           |
| **Attack Categories**    | All MITRE tactics                                                              |
| **User Emulation**       | n/a                                                                            |
|                          |                                                                                |
| **Packed Size**          | -                                                                              |
| **Unpacked Size**        | 209 GB                                                                         |
| **Download Link**        | [goto](https://datasets.uwf.edu/data/UWF-ZeekData22/)                          |

***

### Overview
The University of West Florida Zeek Dataset (UWF-ZeekData22) is consists of 64 days network traffic and related Zeek logs, collected from a "cyber wargaming course" held at the same university.
This course leveraged the UWF's cyber range, a virtualized and relatively diverse environment of different systems which participants were instructed to attack and defend.
The datasets defining feature is the inclusion of MITRE tactic labels assigned to each packet or log, potentially allowing for attack chain detection or similar use cases.
However, the vast majority (>99.9%) of malicious traffic consists of simple reconnaissance, and, apart from statistics, there is very little information about individual attacks.
The authors also detail the process of collecting these large amounts of data with a dedicated solution (Apache Hadoop), though this is considered out of scope for this survey.

### Environment
As mentioned, course participants leveraged the universities cyber range.
Although the authors state that their dataset contains thousands of distinct IP addresses, this is most likely caused by the fact that each group of students (81 in total) was assigned their own environment (as opposed to one actually large network).
Each individual network hosts, presumably, six machines with different versions of Windows and Linux operating systems, running various, partially vulnerable, services - presumably, because Section 4 of the underlying paper [1] is pretty unclear in this regard.

Traffic is captured on one of these VMs and sent to a Hadoop instance, a distributed file system designed for storing and processing large datasets.
The same VM also generated various Zeek logs, which were forwarded in the same manner.

### Activity
The collection period lasted from 2021/12/12 to 2022/02/20, with a break of six days, for a total of 64 days.
While attacks cover the entire range of MITRE tactics (14 at the time of writing), no detail at all is provided regarding the way in which these attack were executed;
only the number of instances per attack tactis is available:
- Reconnaissance: 9.278.722
- Discovery: 2.086
- Credential Access: 31
- Privilege Escalation: 13
- Exfiltration: 7
- Lateral Movement: 4
- Resource Development: 3
- Initial Access: 1
- Persistence: 1
- Defense Evasion: 1

In other words, the vast majority of malicious traffic consists most likely of port scans and similar trivial operations.
Additionally, while there seems to be some form of benign activity, it is in no way documented.

### Contained Data
Data is generally available in three different formats, all of which are labelled with the associated MITRE tactic:
- pcaps: Contains captured traffic.
Note that these are in a [custom binary format](https://docs.securityonion.net/en/latest/stenographer.html) generated by Security Onion.
These files are divided into thousands of smaller files, each covering roughly one minute of traffic.
- parquet: A binary column-oriented data storage format (basically a faster version of CSV when working with large files).
Contained information is very similar to that of network flows (see example of CSV files below).
There are eight files in total, each covering eight days of traffic.
- CSV: A subset of aforementioned parquet files, which, according to the authors, were mainly made available for people who do not have access to "Big Data" technologies.
These files contain data from 2022/02/10, 0300-0600, 0900-1000, and 1400-1500, with one file per hour, thus five files in total.
Each file contains one million entries with a benign/attack ratio of about 80/20.
For attacks, only the tactics "Reconnaissance" and "Discovery" are included.

It is unclear where exactly Zeek logs can be found, though I am assuming they are part of the PCAP files.
The authors leverage what they call "mission logs" to perform labeling, though the nature of these logs is not further detailed.
Section 6.1 in [1] seems to suggest that these are manually created by participants, who document their current activity in the form of timestamps, ports, IPs, tactics, etc.

### Papers
- [[1] Introducing UWF-ZeekData22: A Comprehensive Network Traffic Dataset Based on the MITRE ATT&CK Framework (2022)](https://doi.org/10.3390/data8010018)

### Links
- [Homepage](https://datasets.uwf.edu/)
  - [Types of collected Zeek logs](https://datasets.uwf.edu/tables/table1.html)
  - [Attributes per Zeek log type](https://datasets.uwf.edu/tables/table2.html)

### Data Examples
Traffic information in CSV format taken from `csv/part-00000-d32a9d5e-45b7-4e51-807e-1af297aba2df-c000.csv`

<!--  {% raw %} -->
```
resp_pkts,service,orig_ip_bytes,local_resp,missed_bytes,protocol,duration,conn_state,dest_ip,orig_pkts,community_id,resp_ip_bytes,dest_port,orig_bytes,local_orig,datetime,history,resp_bytes,uid,src_port,ts,src_ip,mitre_attack_tactics
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
2,dns,186,false,0,udp,0.002279996871948242,SF,143.88.5.1,2,1:Z2qpnUv+rxq4N1rn7Go962U/gi8=,186,53,130,false,2022-02-10T03:58:29.979Z,Dd,130,CwO2bA321vyBxBjtxb,36073,1.644465509979958E9,143.88.5.12,Reconnaissance
[...]
```
<!--  {% endraw %} -->