---
title: CSE-CIC-IDS2018
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)
- [Example Data](#example-data)

| <!-- -->                 | <!-- -->                                                                                                 |
|--------------------------|----------------------------------------------------------------------------------------------------------|
| **Network Data Source**  | pcaps, NetFlows                                                                                          |
| **Network Data Labeled** | Yes, NetFlows are labeled                                                                                |
| **Host Data Source**     | Ubuntu event logs, Windows event logs                                                                    |
| **Host Data Labeled**    | No                                                                                                       |
|                          |                                                                                                          |
| **Overall Setting**      | Enterprise IT                                                                                            |
| **OS Types**             | Windows 7/8.1/10/Vista/Server 2016 <br> Ubuntu 14.04/16.04 <br> MacOS<br/> Kali & Windows 8.1 (Attacker) |
| **Number of Machines**   | 450                                                                                                      |
| **Total Runtime**        | ~5 days                                                                                                  |
| **Year of Collection**   | 2018                                                                                                     |
| **Attack Categories**    | Bruteforce<br/>Heartbleed<br/>Botnet<br/>DoS/DDoS<br/>Web-Based<br/>Infiltration from Inside             |
| **Benign Activity**      | Synthetic, models complex behavior                                                                       |
|                          |                                                                                                          |
| **Packed Size**          | 220 GB                                                                                                   |
| **Unpacked Size**        | n/a                                                                                                      |
| **Download Link**        | [Instructions at bottom of page](https://www.unb.ca/cic/datasets/ids-2018.html)                          |

***

### Overview

A collaboration between the Communications Security Establishment (CSE) and the Canadian Institute for Cybersecurity (CIC), this dataset uses the notion of profiles to generate cybersecurity datasets in a systematic manner, including various attack types and a large and diverse infrastructure.
It is a continuation of previous efforts (CIC IDS2017), featuring similar attacks and benign behavior, but being significantly larger in scale (14 vs. 450 victim machines, 1 vs. 6 victim networks).
While being one of the primary benchmark datasets in the current field of NIDS research, researchers have discovered errors within this dataset, affecting aspects like attack orchestration, feature generation, or labeling.

### Environment

The attacking infrastructure contains 50 machines, the victim infrastructure consists of 5 departments with a total of 420 PCs and 30 servers.
An overview is provided by the diagram below.
Presumably, vulnerable software versions have been installed to facilitate certain exploits, but this is more suggested than specified in their description.

![CIC IDS 2018 Network Diagram]({{ "/assets/img/cse_cic_ids_2018_diagram.svg" | relative_url }})

### Activity

Simulated behavior is defined in the form of profiles, divided into benign (B) and malicious (M) profiles.
B-profiles are derived from observing human behavior, from which some features are learned/extracted.
M-profiles consist of seven different attack scenarios, each based on a certain attack type:

- Bruteforce
- Heartbleed
- Botnet
- DoS
- DDoS
- Web-Based
- Infiltration from inside network

The total capturing period lasted ~5 days, with attacks being performed on every day except the first.
Details for each attack as well as the timing are available on the linked homepage.

### Contained Data

The dataset includes the network traffic and log files of each victim machine, combined with 80 network features extracted from captured traffic using [CICFlowMeter](https://www.unb.ca/cic/research/applications.html#CICFlowMeter).
Data is divided into two main directories, `Network Traffic and Log Data` as well as `Processed Traffic Data for ML Algorithms`, with data being organized per day, respectively.
The former contains raw data in the form of unlabeled network traffic (pcap) and event logs (Windows/Ubuntu).
The latter consists of labeled features derived from the aforementioned network traffic (although the labeling logic is not transparently documented);
these features are what is most commonly leveraged when using this dataset.
Each feature is explained in detail on the homepage linked below.

The aforementioned flaws of this dataset, such as some simulation artifacts making detection artificially easy, are for example laid out in paper [2] referenced below.

### Papers

- [[1] Toward Generating a New Intrusion Detection Dataset and Intrusion Detection Traffic Characterization (2017)](https://doi.org/10.5220/0006639801080116)
- [[2] Error Prevalence in NIDS datasets: A Case Study on CIC-IDS-2017 and CSE-CIC-IDS-2018 (2022)](https://doi.org/10.1109/CNS56114.2022.9947235)

### Links

- [Homepage](https://www.unb.ca/cic/datasets/ids-2018.html)
    - For download, install AWS CLI and
      run `aws s3 sync --no-sign-request --region <your-region> "s3://cse-cic-ids2018/" dest-dir`, where your-region is
      your AWS region and destination-dir is the target directory.
    - If cou only need the labeled features, use `s3://cse-cic-ids2018/Processed Traffic Data for ML Algorithms` as your URL
- [Secondary Source](https://registry.opendata.aws/cse-cic-ids2018/)

### Related Entries
- [CIC IDS2017](cic_ids2017.md)
- [NF-UQ-NIDS](nf_uq_nids.md)

### Example Data

Labeled features from `Processed Traffic Data for ML Algorithms/Thursday-01-03-2018_TrafficForML_CICFlowMeter.csv`

```
Dst Port,Protocol,Timestamp,Flow Duration,Tot Fwd Pkts,Tot Bwd Pkts,TotLen Fwd Pkts,TotLen Bwd Pkts,Fwd Pkt Len Max,Fwd Pkt Len Min,Fwd Pkt Len Mean,Fwd Pkt Len Std,Bwd Pkt Len Max,Bwd Pkt Len Min,Bwd Pkt Len Mean,Bwd Pkt Len Std,Flow Byts/s,Flow Pkts/s,Flow IAT Mean,Flow IAT Std,Flow IAT Max,Flow IAT Min,Fwd IAT Tot,Fwd IAT Mean,Fwd IAT Std,Fwd IAT Max,Fwd IAT Min,Bwd IAT Tot,Bwd IAT Mean,Bwd IAT Std,Bwd IAT Max,Bwd IAT Min,Fwd PSH Flags,Bwd PSH Flags,Fwd URG Flags,Bwd URG Flags,Fwd Header Len,Bwd Header Len,Fwd Pkts/s,Bwd Pkts/s,Pkt Len Min,Pkt Len Max,Pkt Len Mean,Pkt Len Std,Pkt Len Var,FIN Flag Cnt,SYN Flag Cnt,RST Flag Cnt,PSH Flag Cnt,ACK Flag Cnt,URG Flag Cnt,CWE Flag Count,ECE Flag Cnt,Down/Up Ratio,Pkt Size Avg,Fwd Seg Size Avg,Bwd Seg Size Avg,Fwd Byts/b Avg,Fwd Pkts/b Avg,Fwd Blk Rate Avg,Bwd Byts/b Avg,Bwd Pkts/b Avg,Bwd Blk Rate Avg,Subflow Fwd Pkts,Subflow Fwd Byts,Subflow Bwd Pkts,Subflow Bwd Byts,Init Fwd Win Byts,Init Bwd Win Byts,Fwd Act Data Pkts,Fwd Seg Size Min,Active Mean,Active Std,Active Max,Active Min,Idle Mean,Idle Std,Idle Max,Idle Min,Label
[...]
3389,6,01/03/2018 09:56:59,4046191,14,7,1386,392,680,0,99,189.2048137,291,0,56,105.3976597,439.4256228,5.190066411,202309.55,254579.8433,957090,27,4046191,311245.4615,336198.2491,1235902,49275,3933933,655655.5,326972.6235,957090,165703,0,0,0,0,292,152,3.460044274,1.730022137,0,680,80.81818182,161.4669762,26071.58442,0,0,1,1,0,0,0,1,0,84.66666667,99,56,0,0,0,0,0,0,14,1386,7,392,8192,62614,7,20,0,0,0,0,0,0,0,0,Benign
58655,6,01/03/2018 09:56:59,86620951,2,0,0,0,0,0,0,0,0,0,0,0,0,0.023089102,86600000,0,86600000,86600000,86600000,86600000,0,86600000,86600000,0,0,0,0,0,0,0,0,0,40,0,0.023089102,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,62617,-1,0,20,0,0,0,0,86600000,0,86600000,86600000,Benign
50657,6,01/03/2018 09:56:59,0,2,0,0,0,0,0,0,0,0,0,0,0,NaN,Infinity,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,4816,-1,0,20,0,0,0,0,0,0,0,0,Benign
443,6,01/03/2018 09:56:59,17,1,1,0,0,0,0,0,0,0,0,0,0,0,117647.0588,17,0,17,17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,58823.52941,58823.52941,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,64237,4816,0,20,0,0,0,0,0,0,0,0,Benign
50656,6,01/03/2018 09:56:59,21,1,1,0,0,0,0,0,0,0,0,0,0,0,95238.09524,21,0,21,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,47619.04762,47619.04762,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,946,254,0,20,0,0,0,0,0,0,0,0,Benign
3389,6,01/03/2018 09:57:00,1402669,8,7,1148,1581,677,0,143.5,228.1296624,1173,0,225.8571429,430.0986044,1945.576611,10.69389856,100190.6429,251930.1473,969023,49,1402669,200381.2857,385946.3919,1073843,49,1338992,223165.3333,365735.7739,969023,63653,0,0,0,0,168,148,5.703412566,4.990485995,0,1173,170.5625,319.4332416,102037.5958,0,0,0,1,0,0,0,0,0,181.9333333,143.5,225.8571429,0,0,0,0,0,0,8,1148,7,1581,8192,62852,5,20,0,0,0,0,0,0,0,0,Infilteration
53,17,01/03/2018 09:57:00,303,1,1,46,62,46,46,46,0,62,62,62,0,356435.6436,6600.660066,303,0,303,303,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,3300.330033,3300.330033,46,62,51.33333333,9.237604307,85.33333333,0,0,0,0,0,0,0,0,1,77,46,62,0,0,0,0,0,0,1,46,1,62,-1,-1,0,8,0,0,0,0,0,0,0,0,Infilteration
[...]
```

Ubuntu event logs taken from `Network Traffic and Log data/Friday-16-02-2018/logs/U172.31.69.25`

```
[...]
Feb 16 07:39:01 ip-172-31-69-25 CRON[11625]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && /usr/lib/php/sessionclean)
Feb 16 07:48:09 ip-172-31-69-25 dhclient[922]: DHCPREQUEST of 172.31.69.25 on eth0 to 172.31.69.1 port 67 (xid=0x6df277b)
Feb 16 07:48:09 ip-172-31-69-25 dhclient[922]: DHCPACK of 172.31.69.25 from 172.31.69.1
Feb 16 07:48:09 ip-172-31-69-25 dhclient[922]: bound to 172.31.69.25 -- renewal in 1760 seconds.
Feb 16 08:09:01 ip-172-31-69-25 CRON[11722]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && /usr/lib/php/sessionclean)
Feb 16 08:15:12 ip-172-31-69-25 systemd[1]: Received SIGINT.
Feb 16 08:15:12 ip-172-31-69-25 systemd[1]: Stopped target Cloud-init target.
Feb 16 08:15:12 ip-172-31-69-25 systemd[1]: Stopping ACPI event daemon...
Feb 16 08:15:12 ip-172-31-69-25 systemd[1]: Stopping Session 819 of user ubuntu.
Feb 16 08:15:12 ip-172-31-69-25 systemd[1]: Stopped Execute cloud user/final scripts.
Feb 16 08:15:12 ip-172-31-69-25 systemd[1]: Stopped Apply the settings specified in cloud-config.
Feb 16 08:15:12 ip-172-31-69-25 systemd[1]: Stopped target Timers.
Feb 16 08:15:12 ip-172-31-69-25 systemd[1]: Stopped Timer to automatically refresh installed snaps.
Feb 16 08:15:12 ip-172-31-69-25 systemd[1]: Stopped Daily Cleanup of Temporary Directories.
Feb 16 08:15:12 ip-172-31-69-25 kernel: [1031302.416958] device eth0 left promiscuous mode
Feb 16 08:15:12 ip-172-31-69-25 systemd[1]: Stopping Session 1 of user ubuntu.
[...]
```