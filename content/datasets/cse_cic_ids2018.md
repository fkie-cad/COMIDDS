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
| **Network Log Source**   | pcaps, network features                                                                                  |
| **Network Logs Labeled** | Only features are labeled                                                                                |
| **Host Log Source**      | Ubuntu event logs, Windows event logs                                                                    |
| **Host Logs Labeled**    | No                                                                                                       |
|                          |                                                                                                          |
| **Overall Setting**      | Enterprise IT                                                                                            |
| **OS Types**             | Windows 7/8.1/10/Vista/Server 2016 <br> Ubuntu 14.04/16.04 <br> MacOS<br/> Kali & Windows 8.1 (Attacker) |
| **Number of Machines**   | 450                                                                                                      |
| **Total Runtime**        | ~5 days                                                                                                  |
| **Year of Collection**   | 2018                                                                                                     |
| **Attack Categories**    | Bruteforce<br/>Heartbleed<br/>Botnet<br/>DoS/DDoS<br/>Web-Based<br/>Infiltration from Inside             |
| **User Emulation**       | Yes, models complex behavior                                                                             |
|                          |                                                                                                          |
| **Packed Size**          | 220 GB                                                                                                   |
| **Unpacked Size**        | _n/a_                                                                                                    |
| **Download Link**        | [Instructions at bottom of page](https://www.unb.ca/cic/datasets/ids-2018.html)                          |

***

### Overview

A collaboration between the Communications Security Establishment (CSE) and the Canadian Institute for Cybersecurity (
CIC), this dataset uses the notion of profiles to generate cybersecurity datasets in a systematic manner, including
various attack types and a large and diverse infrastructure.
It is a continuation of previous efforts (CIC IDS2017), and, oddly enough, cites the exact same paper, even though at
least some key features like network structure do not match up.

### Environment

The attacking infrastructure contains 50 machines, the victim infrastructure consists of 5 departments with a total of
420 PCs and 30 servers.
An overview is provided by the diagram below (image quality courtesy of the authors).
Presumably, vulnerable software versions have been installed to facilitate certain exploits, but this is more...
suggested than specified in their description.

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

The dataset includes the network traffic and log files of each victim machine, combined with 80 network features
extracted from captured traffic using [CICFlowMeter](https://www.unb.ca/cic/research/applications.html#CICFlowMeter).
Raw data consists of unlabeled network traffic (pcap) and event logs (Windows/Ubuntu), and is organized per day.
From the former, features are extracted and labeled, with each feature being explained in detail on the homepage linked
below.

### Papers

- [Toward Generating a New Intrusion Detection Dataset and Intrusion Detection Traffic Characterization (2017)](https://doi.org/10.5220/0006639801080116)
- [Error Prevalence in NIDS datasets: A Case Study on CIC-IDS-2017 and CSE-CIC-IDS-2018 (2022)](https://doi.org/10.1109/CNS56114.2022.9947235)

### Links

- [Homepage](https://www.unb.ca/cic/datasets/ids-2018.html)
    - For download, install AWS CLI and
      run `aws s3 sync --no-sign-request --region <your-region> "s3://cse-cic-ids2018/" dest-dir`, where your-region is
      your AWS region and destination-dir is the target directory.
- [Secondary Source](https://registry.opendata.aws/cse-cic-ids2018/)

### Related Entries
- [CIC IDS2017](cic_ids2017.md)
- [NF-UQ-NIDS](nf_uq_nids.md)

### Example Data

Ubuntu event logs taken from `Friday-16-02-2018/logs/U172.31.69.25`

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

Windows event logs taken from `Friday-16-02-2018/logs/DESKTOP-AN3U28N-172.31.64.17.evtx` (manually converted to `.csv`)

```
[...]
Informationen,26.01.2018 17:28:05,Microsoft-Windows-WindowsUpdateClient,44,Windows Update-Agent,Windows Update hat mit dem Herunterladen eines Updates begonnen.
Informationen,26.01.2018 17:28:05,Microsoft-Windows-WindowsUpdateClient,44,Windows Update-Agent,Windows Update hat mit dem Herunterladen eines Updates begonnen.
Informationen,26.01.2018 17:28:02,Service Control Manager,7040,Keine,"Der Starttyp des Diensts ""Background Intelligent Transfer Service"" wurde von demand start in auto start geändert."
Informationen,26.01.2018 17:10:01,Service Control Manager,7040,Keine,"Der Starttyp des Diensts ""Windows Update"" wurde von disabled in demand start geändert."
Informationen,26.01.2018 17:00:00,EventLog,6013,Keine,Die aktive Systemzeit ist 12069 Sekunden.
Informationen,26.01.2018 14:39:06,Service Control Manager,7040,Keine,"Der Starttyp des Diensts ""Background Intelligent Transfer Service"" wurde von auto start in demand start geändert."
Informationen,26.01.2018 13:49:37,Service Control Manager,7045,Keine,"Im System wurde ein Dienst installiert.

Dienstname:  MpKsl84e93293
Dienstdateiname:  C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{017B94DD-13C1-4C32-8EE5-436E8971A9E1}\MpKsl84e93293.sys
Diensttyp:  kernel mode driver
Dienststarttyp:  system start
Dienstkonto:  "
Informationen,26.01.2018 13:39:02,Service Control Manager,7026,Keine,"Der folgende Boot- oder Systemstarttreiber konnte nicht geladen werden: 
cdrom
dam"
Informationen,26.01.2018 13:39:01,Microsoft-Windows-Winlogon,7001,(1101),Benutzeranmeldebenachrichtigung für Programm zur Verbesserung der Benutzerfreundlichkeit
Warnung,26.01.2018 13:38:58,Microsoft-Windows-TaskScheduler,414,Fehlerhafte Taskkonfiguration,Der Aufgabenplanungsdienst hat eine Fehlkonfiguration in Definition NT TASK\OneDrive Standalone Update Task-S-1-5-21-913095808-1976597276-3100954228-1002gefunden. Zusätzliche Daten: Fehlerwert: %localappdata%\Microsoft\OneDrive\OneDriveStandaloneUpdater.exe.
Warnung,26.01.2018 13:38:58,Microsoft-Windows-TaskScheduler,414,Fehlerhafte Taskkonfiguration,Der Aufgabenplanungsdienst hat eine Fehlkonfiguration in Definition NT TASK\OneDrive Standalone Update Task-S-1-5-21-913095808-1976597276-3100954228-1001gefunden. Zusätzliche Daten: Fehlerwert: %localappdata%\Microsoft\OneDrive\OneDriveStandaloneUpdater.exe.
Informationen,26.01.2018 13:38:58,Microsoft-Windows-DHCPv6-Client,51046,Dienststatusereignis,Der DHCPv6-Clientdienst wird gestartet.
[...]
```