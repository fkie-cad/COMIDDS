---
title: NGIDS Dataset
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                                      |
|--------------------------|-----------------------------------------------------------------------------------------------|
| **Network Data Source**  | pcaps                                                                                         |
| **Network Data Labeled** | Ground truth provided                                                                         |
| **Host Data Source**     | Features derived from host events                                                             |
| **Host Data Labeled**    | Yes                                                                                           |
|                          |                                                                                               |
| **Overall Setting**      | Enterprise IT                                                                                 |
| **OS Types**             | Ubuntu 14.04                                                                                  |
| **Number of Machines**   | n/a                                                                                           |
| **Total Runtime**        | ~5 days                                                                                       |
| **Year of Collection**   | 2016                                                                                          |
| **Attack Categories**    | DDoS<br/>Shellcode<br/>Worms<br/>Reconnaissance<br/>Exploits<br/>"Generic"                    |
| **Benign Activity**      | Synthetic, using IXIA PerfectStorm                                                            |
|                          |                                                                                               |
| **Packed Size**          | 941 MB                                                                                        |
| **Unpacked Size**        | 13,4 GB                                                                                       |
| **Download Link**        | [goto](https://unsworks.unsw.edu.au/bitstreams/0ac2820a-5131-43ab-90b2-c624c8d73649/download) |

***

### Overview

The Next-Generation Intrusion Detection System Dataset (NGIDS-DS) was created as part of a doctor thesis.
It attempts to improve upon major datasets of its time (namely KDD'98 and ADFA-LD), following a set of "requirements"
laid out in the paper, which are all aimed towards generating a more realistic dataset.
It is a collection of host and network logs from a simulated enterprise environment, generally intended to be used with
anomaly-based detection methods, with the paper defining a novel "combined feature" for this purpose, merging information about a system call and its execution time.
Their requirements for a simulation are:

- complete capture of OS audit logs and network packets
- maximum number of attacks included
- current (as in, relevant) attack behaviors
- real-world normal traffic dynamics with operation timings (aka working hours etc.) and industry complexity
- maintenance of cyber infrastructure performance during complete capture
- ground truth information included to assist labeling process

Some of these feel a bit arbitrary, e.g., what even is the "maximum" number of attacks.
And listing "infrastructure performance" as a requirement was most likely only done because other datasets don't
specifically measure this.

### Environment

The simulation is divided into networks 1 and 2, with 1 representing the main work environment, and 2 acting as critical
infrastructure of a given enterprise, depicted in the picture below.

![NGIDS Network Diagram]({{ "/assets/img/ngids_ds.svg" | relative_url }})

Machine A collects host logs, while machine B collects network packets (as pcaps) moving from network 1 to network 2.

### Activity

NGIDS-DS leverages the commercial
hardware [IXIA Perfect Storm](https://www.keysight.com/us/en/products/network-test/network-test-hardware/perfectstorm.html),
which acts as an all-in-one solution:

- generates normal traffic
    - this traffic can be based on profiles mimicking certain enterprise behaviors (e-commerce, bank, military, etc.)
- executes attacks based on a number of CVEs, where the authors chose the following main categories:
    - Exploit
    - DDoS
    - Backdoor
    - Shellcode
    - Generic
    - Reconnaissance
    - Worm
- generates ground truth for said attacks

Further details regarding user behavior is not provided.
The entire simulation ran for a duration of approximately five days, from March 11, 2016, to March 16, 2016.

### Contained Data

The dataset consists of two versions, V1 and V2, with the main difference being that only V1 contains network logs,
while V2 uses an expanded set of features for their host logs (the previously mentioned "combined feature").
In either version, raw host logs are not available.

Network packets are not labeled, but can be using the provided ground truth, consisting of IP, port, timestamp and
relevant attack information.
Features derived from host logs are labeled with both a binary label (benign/malicious) and the corresponding attack
class, if it is malicious.

### Papers

- [Developing Reliable Anomaly Detection Systems for Critical Hosts: A Proactive Defense Paradigm (2018)](https://doi.org/10.26190/unsworks/20924)

### Links

- [Homepage](http://hdl.handle.net/1959.4/101582)

### Data Examples

V1 host logs taken from `NGIDS-DS-v1/host logs/66.csv`

```
[...]
14/03/2016,11:58:59,2110,/usr/bin/compiz,3,74431854,normal,normal,0
14/03/2016,11:58:59,2110,/usr/bin/compiz,3,74431915,normal,normal,0
14/03/2016,11:58:59,2111,/usr/bin/compiz,168,74433043,normal,normal,0
14/03/2016,11:58:59,2111,/usr/bin/compiz,265,74431886,normal,normal,0
14/03/2016,11:58:59,2319,/usr/bin/unity-scope-loader,265,74431815,normal,normal,0
14/03/2016,11:58:59,2319,/usr/bin/unity-scope-loader,292,74431819,normal,normal,0
14/03/2016,11:59:00,1081,/usr/bin/Xorg,104,74432291,Denial of Service,IIS Web Server,1
14/03/2016,11:59:00,1081,/usr/bin/Xorg,104,74432442,Denial of Service,IIS Web Server,1
14/03/2016,11:59:00,1081,/usr/bin/Xorg,104,74432456,Denial of Service,IIS Web Server,1
14/03/2016,11:59:00,1081,/usr/bin/Xorg,104,74432515,Denial of Service,IIS Web Server,1
[...]
```

Ground truth for V1 network logs taken from `NGIDS-DS-v1/ground_truth.csv`

```
[...]
14/03/2016,9:36:00,Backdoors,All Batch,phpmyadmin 3.5.2.2 Backdoor Access and Code Execution (https://strikecenter.bpointsys.com/bps/strikes/backdoors/cve_2012_5159_phpmhyadmin_backdoor.xml),CVE 2012-5159 (http://cve.mitre.org/cgi-bin/cvename.cgi?name=2012%2d5159)BID 55672 (http://www.securityfocus.com/bid/55672)OSVDB 85739 (http://www.osvdb.org/85739)CVSS-High (https://strikecenter.bpointsys.com/bps/reference/CVSS/7.5%20%28AV%3aN%2fAC%3aL%2fAu%3aN%2fC%3aP%2fI%3aP%2fA%3aP%29),IP 175.45.176.0:0->10.40.85.32:0 175.45.176.0:10388->10.40.85.32:80
15/03/2016,12:28:48,Backdoors,All Batch,Android AndroidKungFu Malware Command and Control (https://strikecenter.bpointsys.com/bps/strikes/backdoors/android_droidkungfu_command_and_control.xml),http://about-threats.trendmicro.com/malware.aspx?language=au&name=ANDROIDOS_LENA.B (http%3a%2f%2fabout%2dthreats.trendmicro.com%2fmalware.aspx%3flanguage%3dau%26name%3dANDROIDOS_LENA.B), 175.45.176.3:35200->10.40.85.32:7500
15/03/2016,3:36:00,Backdoors,All Batch,Cisco Network Registrar Default Credentials Backdoor Access (https://strikecenter.bpointsys.com/bps/strikes/backdoors/cve_2011_2024_cisco_network_registrar_auth_bypass.xml),CVE 2011-2024 (http://cve.mitre.org/cgi-bin/cvename.cgi?name=2011%2d2024)BID 48076 (http://www.securityfocus.com/bid/48076)OSVDB 72720 (http://www.osvdb.org/72720)CVSS-Critical (https://strikecenter.bpointsys.com/bps/reference/CVSS/10.0%20%28AV%3aN%2fAC%3aL%2fAu%3aN%2fC%3aC%2fI%3aC%2fA%3aC%29),IP 175.45.176.0:0->10.40.85.32:0 175.45.176.0:54326->10.40.85.32:8080
15/03/2016,4:19:12,Backdoors,All Batch,BlackEnergy Botnet Command and Control Communications (https://strikecenter.bpointsys.com/bps/strikes/backdoors/blackenergy_botnet_command_and_control_communications.xml),http://atlas-public.ec2.arbor.net/docs/BlackEnergy+DDoS+Bot+Analysis.pdf (http%3a%2f%2fatlas%2dpublic.ec2.arbor.net%2fdocs%2fBlackEnergy%2bDDoS%2bBot%2bAnalysis.pdf), 175.45.176.0:18585->10.40.85.32:16840
[...]
```

V1 host and ground truth feature explanation taken from `NGIDS-DS-v1/feature_descr.csv`

```
Files,Feature No,Feature Name,Type,Description
99 host logs csv files,1,date,date,Contains the date on which the particular activity of the NGIDS-DS is performed
,2,time,time,Contains the time on which the activity of the NGIDS-DS is executed
,3,pro_id,number,Represents the process unique identification executed in the host during the simulation 
,4,path,nominal,It contains the execution path of any process executed in the host
,5,sys_call,number,Contains the system calls identifiers executed by the processes
,6,event_id,number,Represents the event's unique identification which happened in the host 
,7,attack_cat,nominal,"It contains the names of the main categories of the attacks such as  Expliots, DoS, Worms, Malware, Fuzzers, Backdoors, Shellcode, Reconnaissance and Generic. Also contains ""null"" where label=0 which means normal activity record"
,8,attack_subcat,nominal,"It contain the sub type of attack of main attack category such as the subcategory “Browser” belongs to the main category “Exploits”. Also contains ""null"" where label=0 which means normal activity record"
,9,label,binary,Contain 0 or 1 to show the main category of the activity whether normal or abnormal 
,,,,
ground_truth.csv ,1,date,date,Contains the date on which the particular activity of the NGIDS-DS is performed
,2,time,time,Contains the time on which the activity of the NGIDS-DS is executed
,3,attack_cat,nominal,"It contains the names of the main categories of the attacks such as  Expliots, DoS, Worms, Malware, Fuzzers, Backdoors, Shellcode, Reconnaissance and Generic. "
,4,attack_subcat,nominal,It contain the sub type of attack of main attack category such as the subcategory “Browser” belongs to the main category “Exploits”. 
,5,attack_name,nominal,It contain the exact literature name of any attack present in NGIDS-DS
,6,attack_refrence,nominal,It shows the complete reference of any attack
,7,ips,nominal,"It contains the information about protocols such as TCP,UDP, ports and IPs during the transactions of the simulation"
```

V2 host logs taken from `NGIDS-DS-v2/test/0_4.csv`

```
[...]
12/03/2016,10:02:07,4519,/usr/sbin/apache2,78,26315221,normal,normal,0,44488,1,52
12/03/2016,10:02:07,4519,/usr/sbin/apache2,78,26315381,normal,normal,0,44489,1,52
12/03/2016,10:02:07,4519,/usr/sbin/apache2,78,26315386,normal,normal,0,44490,1,52
12/03/2016,10:02:07,4519,/usr/sbin/apache2,78,26315394,normal,normal,0,44491,1,52
12/03/2016,10:02:07,4519,/usr/sbin/apache2,78,26315543,normal,normal,0,44492,1,52
12/03/2016,10:02:07,4519,/usr/sbin/apache2,78,26315571,normal,normal,0,44493,1,52
12/03/2016,10:02:08,1081,/usr/lib/libreoffice/program/soffice.bin,104,26315894,Exploits,Office Document Batch,1,44494,1,69
12/03/2016,10:02:08,1081,/usr/lib/libreoffice/program/soffice.bin,146,26315890,Exploits,Office Document Batch,1,44495,1,86
12/03/2016,10:02:08,1081,/usr/lib/libreoffice/program/soffice.bin,54,26315715,Exploits,Office Document Batch,1,44496,1,35
12/03/2016,10:02:08,1081,/usr/lib/libreoffice/program/soffice.bin,54,26315745,Exploits,Office Document Batch,1,44497,1,35
12/03/2016,10:02:08,2110,/usr/lib/libreoffice/program/soffice.bin,102,26315691,Exploits,Office Document Batch,1,44498,1,69
[...]
```

V2 feature explanation taken from `NGIDS-DS-v1/readme.txt`

```
c1	Contains the date on which the particular activity of the NGIDS-DS is performed
c2	Contains the time on which the activity of the NGIDS-DS is executed
c3	Represents the process unique identification executed in the host during the simulation 
c4	It contains the execution path of any process executed in the host
c5	Contains the system calls identifiers executed by the processes
c6	Represents the event's unique identification which happened in the host 
c7	It contains the names of the main categories of the attacks such as  Expliots, DoS, Worms, Malware, Fuzzers, Backdoors, Shellcode, Reconnaissance and Generic. 		Also contains "null" where label=0 which means normal activity record
c8	It contain the sub type of attack of main attack category such as the subcategory “Browser” belongs to the main category “Exploits”. Also contains "null" where 	label=0 which means normal activity record
c9	Contain 0 or 1 to show the main category of the activity whether normal or abnormal 
c10	Irrelevant but created to find c12 (i.e., Joint feature and for details kindly consider PhD thesis "Developing Reliable Anomaly Detection System for Critical
        Hosts: A Proactive Defense Paradigm", Chapter 4 Section 4.3)
c11	Irrelevant but created to find c12 (i.e., Joint feature and for details kindly consider PhD thesis "Developing Reliable Anomaly Detection System for Critical
        Hosts: A Proactive Defense Paradigm", Chapter 4 Section 4.3)
c12	Joint Feature and for details kindly consider PhD thesis "Developing Reliable Anomaly Detection System for Critical
        Hosts: A Proactive Defense Paradigm", Chapter 4 Section 4.3)
```