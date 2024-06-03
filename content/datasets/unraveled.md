---
title: Unraveled
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)
- [Example Data](#example-data)
    - [Host Logs](#host-logs)
    - [Network Flows](#network-flows)

| <!-- -->                 | <!-- -->                                                                |
|--------------------------|-------------------------------------------------------------------------|
| **Network Data Source**  | pcaps, snort logs                                                       |
| **Network Data Labeled** | Yes                                                                     |
| **Host Data Source**     | Syslog, audit, auth                                                     |
| **Host Data Labeled**    | Yes                                                                     |
|                          |                                                                         |
| **Overall Setting**      | Enterprise IT                                                           |
| **OS Types**             | Windows 10<br/>Ubuntu 18.04<br/>Kali2020                                |
| **Number of Machines**   | 27+                                                                     |
| **Total Runtime**        | 6 weeks                                                                 |
| **Year of Collection**   | 2021                                                                    |
| **Attack Categories**    | Reconnaissance<br/>Persistence<br/>Lateral Movement<br/>Defense Evasion |
| **Benign Activity**      | Synthetic, models complex behavior                                      |
|                          |                                                                         |
| **Packed Size**          | n/a                                                                     |
| **Unpacked Size**        | 22 GB                                                                   |
| **Download Link**        | [goto](https://dapt2021.s3.amazonaws.com/README.txt)                    |

***

### Overview

Unraveled is a semisynthetic dataset generated from an artificial medium-sized company established on a cloud platform.
It includes simulated user behavior as well as attacks performed by three different attack groups (amateur, skilled,
APT).
It's distinguishing features are the inclusion of defender behavior, which leads to changes in the attackers tactics,
and the addition of separate labeling for "activity", "stage", "defenderResponse" and "signature", which will be
explained in the next section.

### Environment

The network consists of a corporate and a production network, separated by a firewall.
Snort is used as a Network Intrusion Detection System (NIDS), and a blue team is simulated to monitor these logs and
take certain actions for detected malicious activity.
Corporate network machines run Windows 10, Ubuntu 18.04 LTS and Kali2020, production servers all run Ubuntu.
More details are available on the linked GitLab page.

### Activity

Three different attacker groups (Amateur, Skilled Hacker, APT Group) each perform a sequence of steps with varying
success.
The most complex scenario, APT group, consists of the following steps:

- Reconnaissance
- Establish Foot
- Lateral Movement
- Data Exfiltration
- Cover Up

Some actions lead to reactions from the blue team, which causes the attacker to change behavior (though I suspect that
this is fully scripted? Otherwise, I don't know how they labeled this).
A very detailed description of the entire attack model is available on the linked GitLab page.

### Contained Data

Network flows are captured for all machines, system logs are only collected within the corporate network.
Data is separated into

- Raw data:
    - pcap
    - host logs (auth, audit, etc.)
    - several snort files
- Processed data:
    - Flows derived from pcap using NFStream as `.csv`
    - host logs (auth, audit, etc.)
    - One aggregated snort file

Additionally, processed data generally consists of features and is labeled with four different labels:

- Activity (Mitre technique, if applicable)
- Stage (Reconnaissance, Establish Foothold, Maintain Access, Lateral Movement, and Cover-Up)
- DefenderResponse (Benign - not considered malicious by defender, Detected - detected but no action taken, Mitigated -
  some action like blocking traffic or creds reset has been taken)
- Signature (Attacker group responsible, AH, SH or APT)

Raw data consists of pcap files and host logs, while processed data is labelled and a lot smaller due to pcap being
converted to flows (using NFStream).
The latter is available in `.csv` format, with each column representing a feature.
Notably, only very few of the provided processed host log files seem to contain any malicious entries.

### Papers

- [Unraveled - A Semi-Synthetic Dataset for Advanced Persistent Threats (2023)](https://doi.org/10.1016/j.comnet.2023.109688)

### Links

- [Homepage on Gitlab](https://gitlab.com/asu22/unraveled)
- [Raw Data Download Guide](https://dapt2021.s3.amazonaws.com/README.txt)
  - While not included in this guide, consider using the `--no-sign-request` option to avoid having to provide AWS credentials

### Related Entries

- [DAPT 2020, an earlier approach by the same authors](dapt2020.md)

### Example Data

#### Host Logs

Processed audit logs taken from `host_logs/audit/10_1_1_11-audit_labeled`.
It seems like all audit logs include _only_ benign events.

```
LogEvent,Activity,Stage,DefenderResponse,Signature
[...]
type=USER_AUTH msg=audit(1621837965.990:502): pid=14120 uid=1000 auid=1000 ses=3464 msg='op=PAM:authentication acct="ubuntu" exe="/usr/lib/policykit-1/polkit-agent-helper-1" hostname=? addr=? terminal=? res=success',Normal,Benign,Benign,None
type=USER_ACCT msg=audit(1621837965.990:503): pid=14120 uid=1000 auid=1000 ses=3464 msg='op=PAM:accounting acct="ubuntu" exe="/usr/lib/policykit-1/polkit-agent-helper-1" hostname=? addr=? terminal=? res=success',Normal,Benign,Benign,None
type=USER_CMD msg=audit(1621838003.205:504): pid=14150 uid=1000 auid=1000 ses=2 msg='cwd="/home/ubuntu" cmd=726D202F7661722F6C6F672F617574682E6C6F67202F7661722F6C6F672F617574682E6C6F672E31202F7661722F6C6F672F64706B672E6C6F67202F7661722F6C6F672F6661696C6C6F67202F7661722F6C6F672F6C6173746C6F67202F7661722F6C6F672F7379736C6F67202F7661722F6C6F672F7379736C6F672E31202F7661722F6C6F672F7379736C6F672E322E677A202F7661722F6C6F672F7379736C6F672E332E677A202F7661722F6C6F672F74616C6C796C6F67 terminal=pts/5 res=success',Normal,Benign,Benign,None
type=CRED_REFR msg=audit(1621838003.205:505): pid=14150 uid=0 auid=1000 ses=2 msg='op=PAM:setcred acct="root" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/5 res=success',Normal,Benign,Benign,None
type
[...]
```

Processed auth logs taken from `host_logs/auth/10_1_3_8-auth_labeled`.
This is the only auth log file containing malicious events.

```
LogEvent,Activity,Stage,DefenderResponse,Signature
[...]
Jun 25 15:29:53 ubuntu sshd[16151]: lastlog_openseek: Couldn't stat /var/log/lastlog: No such file or directory,Normal,Benign,Benign,None
Jun 25 15:29:53 ubuntu sshd[16151]: lastlog_openseek: Couldn't stat /var/log/lastlog: No such file or directory,Normal,Benign,Benign,None
Jun 25 15:36:16 ubuntu sshd[25268]: Accepted password for ubuntu from 127.0.0.1 port 47452 ssh2,Maintain Access,Lateral Movement,Benign,APT
Jun 25 15:36:16 ubuntu sshd[25268]: pam_unix(sshd:session): session opened for user ubuntu by (uid=0),Maintain Access,Lateral Movement,Benign,APT
[...]
```

Processed filebeat logs taken from `host_logs/filebeat/10_1_3_8-filebeat_labeled`.
It seems like all filebeat logs include _only_ benign events, though the commit message suggests otherwise?

```
LogEvent,Activity,Stage,DefenderResponse,Signature
[...]
2021-06-04:15:20:26,221 DEBUG    [connectionpool.py:208] Starting new HTTP connection (1): 127.0.0.1,Normal,Benign,Benign,None
2021-06-04:15:20:26,326 DEBUG    [connectionpool.py:396] http://127.0.0.1:51475 "POST /session HTTP/1.1" 500 105,Normal,Benign,Benign,None
2021-06-04:15:20:26,327 DEBUG    [remote_connection.py:440] Finished Request,Normal,Benign,Benign,None
2021-06-04:15:20:26,328 ERROR    [worker_check_mail.py:116] Mail check activity failed for mail38@thedapt.xyzdue to Message: Process unexpectedly closed with status 1,Normal,Benign,Benign,None
[...]
```

Processed syslog logs taken from `host_logs/filebeat/10_1_3_8-syslog_labeled`.
It seems like all syslog logs include _only_ benign events, though the commit message suggests otherwise?

```
LogEvent,Activity,Stage,DefenderResponse,Signature
[...]
Jul  3 01:03:44 ubuntu filebeat[13913]: 2021-07-03T01:03:44.915-0700#011INFO#011[monitoring]#011log/log.go:144#011Non-zero metrics in the last 30s#011{"monitoring": {"metrics": {"beat":{"cpu":{"system":{"ticks":645930,"time":{"ms":2}},"total":{"ticks":2017830,"time":{"ms":23},"value":2017830},"user":{"ticks":1371900,"time":{"ms":21}}},"handles":{"limit":{"hard":4096,"soft":1024},"open":12},"info":{"ephemeral_id":"255c4c91-be62-4348-b048-c88527cdbcc5","uptime":{"ms":3372390426}},"memstats":{"gc_next":19127600,"memory_alloc":11066584,"memory_total":205016881504,"rss":31166464},"runtime":{"goroutines":31}},"filebeat":{"events":{"added":1,"done":1},"harvester":{"open_files":1,"running":1}},"libbeat":{"config":{"module":{"running":0}},"output":{"events":{"acked":1,"active":0,"batches":1,"total":1},"read":{"bytes":6},"write":{"bytes":1148}},"pipeline":{"clients":1,"events":{"active":0,"published":1,"total":1},"queue":{"acked":1}}},"registrar":{"states":{"current":3,"update":1},"writes":{"success":1,"total":1}},"system":{"load":{"1":0.07,"15":0,"5":0.02,"norm":{"1":0.07,"15":0,"5":0.02}}}}}},Normal,Benign,Benign,None
Jul  3 01:04:14 ubuntu filebeat[13913]: 2021-07-03T01:04:14.912-0700#011INFO#011[monitoring]#011log/log.go:144#011Non-zero metrics in the last 30s#011{"monitoring": {"metrics": {"beat":{"cpu":{"system":{"ticks":645930},"total":{"ticks":2017840,"time":{"ms":12},"value":2017840},"user":{"ticks":1371910,"time":{"ms":12}}},"handles":{"limit":{"hard":4096,"soft":1024},"open":12},"info":{"ephemeral_id":"255c4c91-be62-4348-b048-c88527cdbcc5","uptime":{"ms":3372420426}},"memstats":{"gc_next":19127600,"memory_alloc":12944560,"memory_total":205018759480,"rss":31166464},"runtime":{"goroutines":31}},"filebeat":{"events":{"added":1,"done":1},"harvester":{"open_files":1,"running":1}},"libbeat":{"config":{"module":{"running":0}},"output":{"events":{"acked":1,"active":0,"batches":1,"total":1},"read":{"bytes":6},"write":{"bytes":1149}},"pipeline":{"clients":1,"events":{"active":0,"published":1,"total":1},"queue":{"acked":1}}},"registrar":{"states":{"current":3,"update":1},"writes":{"success":1,"total":1}},"system":{"load":{"1":0.04,"15":0,"5":0.02,"norm":{"1":0.04,"15":0,"5":0.02}}}}}},Normal,Benign,Benign,None
Jul  3 01:04:34 ubuntu systemd[1]: Started Run anacron jobs.,Normal,Benign,Benign,None
Jul  3 01:04:34 ubuntu anacron[25525]: Anacron 2.3 started on 2021-07-03,Normal,Benign,Benign,None
[...]
```

Processes Windows logs taken from `host_logs/windows/10_1_3_17-windows-securityevents-user_labeled.csv`.

```
Keywords,Date and Time,Source,Event ID,Task Category,Activity,Stage,DefenderResponse,Signature
[...]
Audit Success,7/17/2021 10:31:05 PM,Microsoft-Windows-Security-Auditing,4648,Logon,"A logon was attempted using explicit credentials.,Valid Accounts,Lateral Movement,Benign,APT

Subject:
	Security ID:		SYSTEM
	Account Name:		DESKTOP-56DUI1B$
	Account Domain:		WORKGROUP
	Logon ID:		0x3E7
	Logon GUID:		{00000000-0000-0000-0000-000000000000}

Account Whose Credentials Were Used:
	Account Name:		sshd_4656
	Account Domain:		VIRTUAL USERS
	Logon GUID:		{00000000-0000-0000-0000-000000000000}

Target Server:
	Target Server Name:	localhost
	Additional Information:	localhost

Process Information:
	Process ID:		0x1230
	Process Name:		C:\Windows\System32\OpenSSH\sshd.exe

Network Information:
	Network Address:	-
	Port:			-

This event is generated when a process attempts to log on an account by explicitly specifying that account’s credentials.  This most commonly occurs in batch-type configurations such as scheduled tasks, or when using the RUNAS command.",Valid Accounts,Lateral Movement,Benign,APT
[...]
```

#### Network Flows

Network flows taken from `network-flows/Week5_Day2_06222021/net1013x_Flow_labeled.csv`.
Explanation for fields can be found on the homepage.

```
id,expiration_id,src_ip,src_mac,src_oui,src_port,dst_ip,dst_mac,dst_oui,dst_port,protocol,ip_version ...
[...]
15,0,10.1.3.14,fa:16:3e:2b:10:fa,fa:16:3e,38376,239.255.255.250,01:00:5e:7f:ff:fa,01:00:5e,1900,17,4,0,0,1624347417421,1624347420424,3003,4,852,1624347417421,1624347420424,3003,4,852,0,0,0,0,0,213,213.0,0.0,213,213,213.0,0.0,213,0,0.0,0.0,0,1001,1001.0,0.0,1001,1001,1001.0,0.0,1001,0,0.0,0.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,SSDP,System,0,nan,nan,nan,nan,nan,Normal,Benign,Benign,None
16,0,10.1.3.8,fa:16:3e:f6:2f:13,fa:16:3e,55016,10.8.10.84,fa:16:3e:2b:10:fa,fa:16:3e,443,6,4,0,0,1624347422390,1624347482454,60064,33,4421,1624347422390,1624347482454,60064,17,2049,1624347422391,1624347482454,60063,16,2372,54,133.96969696969697,217.5596879089283,1251,54,120.52941176470588,112.63553926662024,410,66,148.25,294.9925422786143,1251,0,1877.0,5033.51343977416,15103,0,3754.0,6697.141001950012,15104,0,4004.2000000000007,6854.507257480814,15104,2,0,0,0,30,10,2,2,1,0,0,0,14,6,2,1,1,0,0,0,16,4,0,1,TLS,Web,0,nan,89be98bbd4f065fe510fca4893cf8d9b,f4febc55ea12b31ae17cfb7e614afda8,nan,nan,Encrypted Channel: Symmetric Cryptography,Establish Foothold,Benign,APT
[...]
```