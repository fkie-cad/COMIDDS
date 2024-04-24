---
title: UNSW-NB15
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                                                                              |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **Network Data Source**  | pcaps, custom network features                                                                                                        |
| **Network Data Labeled** | Yes                                                                                                                                   |
| **Host Data Source**     | -                                                                                                                                     |
| **Host Data Labeled**    | -                                                                                                                                     |
|                          |                                                                                                                                       |
| **Overall Setting**      | Miscellaneous                                                                                                                         |
| **OS Types**             | Undisclosed                                                                                                                           |
| **Number of Machines**   | <45                                                                                                                                   |
| **Total Runtime**        | 31 hours                                                                                                                              |
| **Year of Collection**   | 2015                                                                                                                                  |
| **Attack Categories**    | Scanning<br/>Backdoors<br/>DoS<br/>Exploits<br/>Reconnaissance<br/>Shellcode<br/>Worms<br/>Fuzzing                                    |
| **Benign Activity**      | Synthetic, via IXIA PerfectStorm                                                                                                            |
|                          |                                                                                                                                       |
| **Packed Size**          | ~100 GB                                                                                                                               |
| **Unpacked Size**        | n/a                                                                                                                                   |
| **Download Link**        | [goto](https://unsw-my.sharepoint.com/:f:/g/personal/z5025758_ad_unsw_edu_au/EnuQZZn3XuNBjgfcUu4DIVMBLCHyoLHqOswirpOQifr1ag?e=gKWkLS) |

***

### Overview
The UNSW-NB15 dataset, developed at the University of New South Wales (UNSW), aims to provide an at the time modern network benchmark dataset.
It improves upon existing datasets like KDD98 by including newer attacks, which are realized using the IXIA PerfectStorm tool, providing both normal and malicious behavior.
Data is mostly intended for anomaly-related use-cases by leveraging features the authors derived from network traffic, though the included raw pcaps should also allow for application of signature-based IDS solutions.


### Environment
The general setup consists of three virtual servers, two routers and an unspecified number of clients, divided into three networks and orchestrated as shown in the diagram below.
Server 1 and 3 generate normal traffic, while server 2 generates malicious traffic.
The paper lists the number of "distinct IP addresses" as 45, but the total number of machines is most definitely lower.

![UNSW-NB15 Network Architecture]({{ "/assets/img/unsw_nb15_network_architecture.svg" | relative_url }})

It seems to be implied that all traffic from router 2 is (also?) passed to router 1, where all traffic is dumped in the form of pcaps.
Section 4.A is not entirely clear in this regard.
Further documentation, especially regarding OS types, is not provided.

### Activity
Both benign and malicious activity is managed and executed by the IXIA PerfectStorm tool, specifically its traffic generator.
However, details regarding either process are not given, it is only stated that "the attack behaviour is nourished from the CVE site for the purpose of a real representation of a modern threat environment".
Attacks are grouped into one of nine categories:
- Fuzzers
- Analysis
- Backdoors
- DoS
- Exploits
- Generic
- Reconnaissance
- Shellcode
- Worms

Additionally, IXIA supplies a ground truth file, listing information like start time or source port and address.
Two simulation runs were performed, which differ only in the frequency of their attacks.
During the first run (16 hours), one attack is executed per second.
During the second run (15 hours), that number increases to ten attacks per second.

### Contained Data
As mentioned, pcaps of presumably the entire network are collected at a central location (Router 1) using tcpdump.
From these files, 49 features are derived, which are grouped into:
- 5 flow features (e.g., Source IP address)
- 13 basic features (e.g., Source to destination bytes)
- 8 content features (e.g., Source TCP sequence number)
- 9 time features (e.g. record start time)
- 12 additional features

All features are explained in section 4.E and 4.F of the paper.
In total, 2.540.044 records were derived, available in the form of `.csv` files.
These were then labelled using the ground truth supplied by IXIA PerfectStorm;
labeling per entry consists of a binary label (0 for normal, 1 for malicious) and an attack category (from those listed above).

Records are divided into four files, with a separate partition intended for training/testing also being available.
Other available files are:
- Ground truth provided by IXIA
- Raw pcaps (grouped by run)
- Various BRO files/logs, for example regarding ssh, http, or smtp (grouped by run and hour, not labeled)
- Presumably automated report on pcap files per run (~1000 pages each with little interesting information)

### Papers
- [UNSQ-NB15: A Comprehensive Data Set for Network Intrusion Detection Systems (2015)](https://doi.org/10.1109/MilCIS.2015.7348942)

### Links
- [Homepage](https://research.unsw.edu.au/projects/unsw-nb15-dataset)
- READMEs
  - [General](https://unsw-my.sharepoint.com/personal/z5025758_ad_unsw_edu_au/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fz5025758%5Fad%5Funsw%5Fedu%5Fau%2FDocuments%2FUNSW%2DNB15%20dataset%2FReadMe%2Epdf&parent=%2Fpersonal%2Fz5025758%5Fad%5Funsw%5Fedu%5Fau%2FDocuments%2FUNSW%2DNB15%20dataset)
  - [Features](https://unsw-my.sharepoint.com/personal/z5025758_ad_unsw_edu_au/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fz5025758%5Fad%5Funsw%5Fedu%5Fau%2FDocuments%2FUNSW%2DNB15%20dataset%2FCSV%20Files%2FThe%20UNSW%2DNB15%20description%2Epdf&parent=%2Fpersonal%2Fz5025758%5Fad%5Funsw%5Fedu%5Fau%2FDocuments%2FUNSW%2DNB15%20dataset%2FCSV%20Files)
- [IXIA PerfectStorm](https://www.keysight.com/us/en/products/network-test/network-test-hardware/perfectstorm.html)

### Related Entries
- [NF-UQ-NIDS](nf_uq_nids.md)

### Data Examples
Records consisting of 49 + 2 features, taken from `CSV Files/UNSW-NB15_4.csv`
```
59.166.0.9,7045,149.171.126.7,25,tcp,FIN,0.201886,37552,3380,31,29,18,8,smtp,1459437.5,130766.8672,52,42,255,255,1422136554,3572668484,722,80,0,0,456.043567,15.530109,1424250009,1424250009,3.943843,4.912488,0.00059,0.000473,0.000117,0,0,,, ,2,2,7,4,1,1,3,,0
59.166.0.9,9685,149.171.126.2,80,tcp,FIN,5.864748,19410,1087890,31,29,2,370,http,26404.54492,1481982.875,364,746,255,255,389619597,394688654,53,1458,1,0,1031.366423,690.219581,1424250003,1424250009,16.155447,7.871279,0.000771,0.000638,0.000133,0,0,1,, ,3,1,4,4,1,1,1,,0
59.166.0.2,1421,149.171.126.4,53,udp,CON,0.001391,146,178,31,29,0,0,dns,419841.8438,511861.9688,2,2,0,0,0,0,73,89,0,0,0,0,1424250009,1424250009,0.009,0.002,0,0,0,0,0,,, ,3,5,2,7,1,1,4,,0
59.166.0.2,21553,149.171.126.2,25,tcp,FIN,0.053948,37812,3380,31,29,19,8,smtp,5503373.5,489360.125,54,42,255,255,4047523379,1903327524,700,80,0,0,65.909688,3.155258,1424250009,1424250009,1.011547,1.302561,0.000674,0.00054,0.000134,0,0,,, ,1,1,4,7,1,1,3,,0
59.166.0.8,45212,149.171.126.4,53,udp,CON,0.000953,146,178,31,29,0,0,dns,612801.6875,747114.375,2,2,0,0,0,0,73,89,0,0,0,0,1424250009,1424250009,0.009,0.004,0,0,0,0,0,,, ,2,5,2,1,1,1,2,,0
59.166.0.0,59922,149.171.126.8,6881,tcp,FIN,8.633186,25056,1094788,31,29,38,390,-,23166.41797,1013311.125,446,858,255,255,497111133,526810925,56,1276,0,0,7751.70264,5572.343447,1424250000,1424250009,19.443407,10.084887,0.000654,0.000516,0.000138,0,0,,, ,9,7,2,3,2,1,6,,0
175.45.176.0,49582,149.171.126.12,80,tcp,FIN,0.189983,13304,268,254,252,6,1,http,529100,9432.422852,18,6,255,255,157871242,468891365,739,45,1,0,842.127346,66.237773,1424250009,1424250009,11.175471,35.431199,0.062013,0.007572,0.054441,0,1,1,, ,1,1,1,1,1,1,1,Exploits,1
175.45.176.1,0,149.171.126.11,0,sctp,INT,0.000009,440,0,254,0,0,0,-,195555552,0,2,0,0,0,0,0,220,0,0,0,0,0,1424250010,1424250010,0.009,0,0,0,0,0,2,,, ,1,1,1,1,1,1,2, Fuzzers ,1
175.45.176.1,0,149.171.126.11,0,sctp,INT,0.000009,440,0,254,0,0,0,-,195555552,0,2,0,0,0,0,0,220,0,0,0,0,0,1424250010,1424250010,0.009,0,0,0,0,0,2,,, ,1,1,1,1,1,1,2,Exploits,1
175.45.176.1,0,149.171.126.11,0,sctp,INT,0.000009,440,0,254,0,0,0,-,195555552,0,2,0,0,0,0,0,220,0,0,0,0,0,1424250010,1424250010,0.009,0,0,0,0,0,2,,, ,1,1,1,1,1,1,2,Exploits,1
```

Ground truth provided by IXIA, taken from `CSV Files/NUSW-NB15_GT.csv` (probably a typo in the name?)
```
Start time,Last time,Attack category,Attack subcategory,Protocol,Source IP,Source Port,Destination IP,Destination Port,Attack Name,Attack Reference,.
1421927414,1421927416,Reconnaissance,HTTP,tcp,175.45.176.0,13284,149.171.126.16,80,Domino Web Server Database Access: /doladmin.nsf (https://strikecenter.bpointsys.com/bps/strikes/recon/http/domino/access_domino_doladmin_nsf.xml),-,.
1421927415,1421927415,Exploits,Unix 'r' Service,udp,175.45.176.3,21223,149.171.126.18,32780,Solaris rwalld Format String Vulnerability (https://strikecenter.bpointsys.com/bps/strikes/exploits/rservices/solaris_rwall_format_string.xml),CVE 2002-0573 (http://cve.mitre.org/cgi-bin/cvename.cgi?name=2002%2d0573)BID 4639 (http://www.securityfocus.com/bid/4639)CVSS-High (https://strikecenter.bpointsys.com/bps/reference/CVSS/7.5%20%28AV%3aN%2fAC%3aL%2fAu%3aN%2fC%3aP%2fI%3aP%2fA%3aP%29),.
1421927416,1421927416,Exploits,Browser,tcp,175.45.176.2,23357,149.171.126.16,80,Windows Metafile (WMF) SetAbortProc() Code Execution [009] (https://strikecenter.bpointsys.com/bps/strikes/exploits/browser/wmf_009.xml),CVE 2005-4560 (http://cve.mitre.org/cgi-bin/cvename.cgi?name=2005%2d4560)BID 16074 (http://www.securityfocus.com/bid/16074)OSVDB 21987 (http://www.osvdb.org/21987)CVSS-High (https://strikecenter.bpointsys.com/bps/reference/CVSS/7.5%20%28AV%3aN%2fAC%3aL%2fAu%3aN%2fC%3aP%2fI%3aP%2fA%3aP%29),.
1421927417,1421927417,Exploits,Miscellaneous Batch,tcp,175.45.176.2,13792,149.171.126.16,5555,HP Data Protector Backup (https://strikecenter.bpointsys.com/bps/strikes/exploits/misc/cve_2011_1729.xml),CVE 2011-1729 (http://cve.mitre.org/cgi-bin/cvename.cgi?name=2011%2d1729)BID 47638 (http://www.securityfocus.com/bid/47638)OSVDB 72188 (http://www.osvdb.org/72188)CVSS-Critical (https://strikecenter.bpointsys.com/bps/reference/CVSS/10.0%20%28AV%3aN%2fAC%3aL%2fAu%3aN%2fC%3aC%2fI%3aC%2fA%3aC%29),.
1421927418,1421927418,Exploits,Cisco IOS ,tcp,175.45.176.2,26939,149.171.126.10,80,Cisco IOS HTTP Authentication Bypass Level 64 (https://strikecenter.bpointsys.com/bps/strikes/exploits/ios/cisco_auth_bypass_level_64.xml),CVE 2001-0537 (http://cve.mitre.org/cgi-bin/cvename.cgi?name=2001%2d0537)BID 2936 (http://www.securityfocus.com/bid/2936)OSVDB 578 (http://www.osvdb.org/578)CVSS-High (https://strikecenter.bpointsys.com/bps/reference/CVSS/9.3%20%28AV%3aN%2fAC%3aM%2fAu%3aN%2fC%3aC%2fI%3aC%2fA%3aC%29),.
1421927419,1421927419,DoS,Miscellaneous,tcp,175.45.176.0,39500,149.171.126.15,80,Cisco DCP2100 SADownStartingFrequency Denial of Service (https://strikecenter.bpointsys.com/bps/strikes/denial/misc/cisco_dcp2100_denial_of_service.xml),http://www.exploit-db.com/exploits/21523/ (http%3a%2f%2fwww.exploit%2ddb.com%2fexploits%2f21523%2f)CVSS-High (https://strikecenter.bpointsys.com/bps/reference/CVSS/7.8%20%28AV%3aN%2fAC%3aL%2fAU%3aN%2fC%3aN%2fI%3aN%2fA%3aC%29),.
1421927419,1421927422,DoS,Miscellaneous,tcp,175.45.176.0,23910,149.171.126.15,80,Cisco DCP2100 SADownStartingFrequency Denial of Service (https://strikecenter.bpointsys.com/bps/strikes/denial/misc/cisco_dcp2100_denial_of_service.xml),http://www.exploit-db.com/exploits/21523/ (http%3a%2f%2fwww.exploit%2ddb.com%2fexploits%2f21523%2f)CVSS-High (https://strikecenter.bpointsys.com/bps/reference/CVSS/7.8%20%28AV%3aN%2fAC%3aL%2fAU%3aN%2fC%3aN%2fI%3aN%2fA%3aC%29),.
1421927420,1421927420,Generic, IXIA,tcp,175.45.176.0,29309,149.171.126.14,3000,Alt-N_MDaemon_WorldClient_Service_Memory_Corruption_attack (https://strikecenter.bpointsys.com/bps/strikes/generic/ixia/alt-n_mdaemon_worldclient_service_memory_corruption_attack.xml),CVE 2008-2631 (http://cve.mitre.org/cgi-bin/cvename.cgi?name=2008%2d2631)OSVDB 45923 (http://www.osvdb.org/45923)CVSS-Moderate (https://strikecenter.bpointsys.com/bps/reference/CVSS/5.0%20%28AV%3aN%2fAC%3aL%2fAu%3aN%2fC%3aN%2fI%3aN%2fA%3aP%29),.
1421927421,1421927421,Exploits,Browser,tcp,175.45.176.0,61089,149.171.126.18,80,Microsoft Internet Explorer Frameset Memory Corruption (https://strikecenter.bpointsys.com/bps/strikes/exploits/browser/ms06_042_html_frameset_memory_corruption.xml),CVE 2006-3637 (http://cve.mitre.org/cgi-bin/cvename.cgi?name=2006%2d3637)BID 18227 (http://www.securityfocus.com/bid/18227)OSVDB 27853 (http://www.osvdb.org/27853)CVSS-Moderate (https://strikecenter.bpointsys.com/bps/reference/CVSS/5.1%20%28AV%3aN%2fAC%3aH%2fAu%3aN%2fC%3aP%2fI%3aP%2fA%3aP%29),.
```