---
title: SOCBED Example Dataset
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                       |
|--------------------------|----------------------------------------------------------------|
| **Network Data Source**  | Traffic via packetbeat                                         |
| **Network Data Labeled** | No (but I labeled a separate run manually)                     |
| **Host Data Source**     | Various system logs                                            |
| **Host Data Labeled**    | No (but I labeled a separate run manually)                     |
|                          |                                                                |
| **Overall Setting**      | Enterprise IT                                                  |
| **OS Types**             | Windows 10<br/>Ubuntu 16.04<br/>IPFire<br/>Kali2021 (Attacker) |
| **Number of Machines**   | 6 + N clients                                                  |
| **Total Runtime**        | 2 hours                                                        |
| **Year of Collection**   | 2021                                                           |
| **Attack Categories**    | Diverse                                                        |
| **Benign Activity**      | Synthetic                                                      |
|                          |                                                                |
| **Packed Size**          | 78 MB                                                          |
| **Unpacked Size**        | 1,3 GB                                                         |
| **Download Link**        | [goto](https://github.com/fkie-cad/socbed-eval-acsac-2021)     |

***

### Overview

A framework aiming to provide a reproducible and adaptable way to generate cybersecurity datasets by providing a testbed
consisting of a number of virtual machines mimicking a small company network and an external attacker.
It includes emulated user behavior (sending mails, manipulating files) and some services typically found in a company
network.
For several different attacks (like SQL injection or interaction with a meterpreter instance), an interface is provided,
as well as the possibility to automate their execution within a simulation.

The dataset here was generated using this testbed, though it must be noted that it should only serve as an example to
demonstrate the capabilities of SOCBED.
Specific needs can and should be met by using SOCBED to generate a custom dataset.

### Environment

Infrastructure consists three network zones:

- Internal: Contains Clients (Win10), Log Server and Internal Server (both Ubuntu 16.04), and a Company Router (IPFire)
- DMZ: Contains DMZ Server (Ubuntu 16.04)
- Internet: Contains Internet Router (IPFire) and Attacker (Kali 2021)

### Activity

Ten separate runs were performed, during each of which various attacks from all MITRE tactics were executed over a
period of ~two hours, followed by downloading collected logs before shutting all machines down again.
During the entire duration of each run, simulated users performed various actions such as interacting with files,
browsing, or sending mails.

### Contained Data

During the simulation, logs are collected from all machines in the Internal and DMZ zone:

- Windows machines (Winlogbeat/Auditbeat): Kernel, services, sysmon, powershell
- DMZ Server (Rsyslog): Kernel, default services, apache, postfix, dovecot
- Internal Server (Rsyslog): Kernel, default services, samba
- Company Router (Rsyslog, packetbeat): Kernel, default services, IPFire firewall, suricata

Simulations were run with both default and best-practice logging configurations, respectively.
Labels are not provided, though I have labeled a separate run (with the same setup) myself.

### Papers

- [Reproducible and Adaptable Log Data Generation for Sound Cybersecurity Experiments (2021)](https://doi.org/10.1145/3485832.3488020)

### Links

- [SOCBED on GitHub](https://github.com/fkie-cad/socbed)
- [Dataset Download](https://github.com/fkie-cad/socbed-eval-acsac-2021)

### Data Examples

Syslogs (also containing one Suricata alert) taken from `host1_bestpractice/syslog_09.jsonl`

```
[...]
{
  "@timestamp": "2021-06-19T02:56:15.992Z",
  "@version": "1",
  "facility": 21,
  "facility_label": "local5",
  "host": "172.16.0.1",
  "logsource": "companyrouter",
  "message": "[1:2016672:3] ET WEB_SERVER SQL Errors in HTTP 200 Response (error in your SQL syntax) [Classification: Potentially Bad Traffic] [Priority: 2] {TCP} 172.17.0.2:80 -> 172.18.0.3:42484\n",
  "pid": "2106",
  "priority": 171,
  "program": "suricata",
  "severity": 3,
  "severity_label": "Error",
  "timestamp": "2021-06-19T04:56:15.992108+02:00",
  "timestamp8601": "2021-06-19T04:56:15.992108+02:00",
  "type": "syslog_raw"
}
{
  "@timestamp": "2021-06-19T02:45:18.604Z",
  "@version": "1",
  "facility": 2,
  "facility_label": "mail",
  "host": "172.17.0.2",
  "logsource": "dmzserver",
  "message": "lmtp(client2@localdomain): g2AeIAlazWA7BAAAwzMyhQ: msgid=unspecified: saved mail to INBOX\n",
  "priority": 22,
  "program": "dovecot",
  "severity": 6,
  "severity_label": "Informational",
  "timestamp": "2021-06-19T04:45:18.604803+02:00",
  "timestamp8601": "2021-06-19T04:45:18.604803+02:00",
  "type": "syslog_raw"
}
[...]
```

Single winlogbeat event taken from `host1_bestpractice/winlogbeat_09.jsonl`

```json
[...]
{
  "@timestamp": "2021-06-19T02:50:26.996Z",
  "agent": {
    "ephemeral_id": "db0de894-44ce-49eb-b537-4cc28fcacc81",
    "hostname": "CLIENT1",
    "id": "72f2d3ff-866e-409e-a0c4-fc667a6fec06",
    "name": "CLIENT1",
    "type": "winlogbeat",
    "version": "7.10.2"
  },
  "destination": {
    "domain": "-",
    "ip": "172.17.0.2",
    "port": 25
  },
  "ecs": {
    "version": "1.5.0"
  },
  "event": {
    "action": "Network connection detected (rule: NetworkConnect)",
    "category": [
      "network"
    ],
    "code": 3,
    "created": "2021-06-19T02:50:29.268Z",
    "kind": "event",
    "module": "sysmon",
    "provider": "Microsoft-Windows-Sysmon",
    "type": [
      "connection",
      "start",
      "protocol"
    ]
  },
  "host": {
    "name": "CLIENT1.breach.local"
  },
  "log": {
    "level": "information"
  },
  "message": "Network connection detected:\nRuleName: SMTP\nUtcTime: 2021-06-19 02:50:26.996\nProcessGuid: {f7f24c5a-5a05-60cd-aacb-110000000000}\nProcessId: 6176\nImage: C:\\Python37\\python.exe\nUser: BREACH\\client1\nProtocol: tcp\nInitiated: true\nSourceIsIpv6: false\nSourceIp: 172.16.1.1\nSourceHostname: CLIENT1.breach.local\nSourcePort: 52999\nSourcePortName: -\nDestinationIsIpv6: false\nDestinationIp: 172.17.0.2\nDestinationHostname: -\nDestinationPort: 25\nDestinationPortName: smtp",
  "network": {
    "community_id": "1:7d8WkHFy3depS7hvt1MpG1Yo7eo=",
    "direction": "outbound",
    "protocol": "smtp",
    "transport": "tcp",
    "type": "ipv4"
  },
  "process": {
    "entity_id": "{f7f24c5a-5a05-60cd-aacb-110000000000}",
    "executable": "C:\\Python37\\python.exe",
    "name": "python.exe",
    "pid": 6176
  },
  "related": {
    "ip": [
      "172.16.1.1",
      "172.17.0.2"
    ],
    "user": "client1"
  },
  "rule": {
    "name": "SMTP"
  },
  "source": {
    "domain": "CLIENT1.breach.local",
    "ip": "172.16.1.1",
    "port": 52999
  },
  "user": {
    "domain": "BREACH",
    "name": "client1"
  },
  "winlog": {
    "api": "wineventlog",
    "channel": "Microsoft-Windows-Sysmon/Operational",
    "computer_name": "CLIENT1.breach.local",
    "event_data": {
      "SourcePortName": "-"
    },
    "event_id": 3,
    "opcode": "Info",
    "process": {
      "pid": 2140,
      "thread": {
        "id": 2628
      }
    },
    "provider_guid": "{5770385f-c22a-43e0-bf4c-06f5698ffbd9}",
    "provider_name": "Microsoft-Windows-Sysmon",
    "record_id": 1906,
    "task": "Network connection detected (rule: NetworkConnect)",
    "user": {
      "domain": "NT AUTHORITY",
      "identifier": "S-1-5-18",
      "name": "SYSTEM",
      "type": "User"
    },
    "version": 5
  }
}
[...]
```

Single winlogbeat event that would trigger a Sigma alert taken from `host1_bestpractice/sigma_09.jsonl`

```json
[...]
{
  "event": {
    "@timestamp": "2021-06-19T02:41:27.390Z",
    "agent": {
      "ephemeral_id": "db0de894-44ce-49eb-b537-4cc28fcacc81",
      "hostname": "CLIENT1",
      "id": "72f2d3ff-866e-409e-a0c4-fc667a6fec06",
      "name": "CLIENT1",
      "type": "winlogbeat",
      "version": "7.10.2"
    },
    "ecs": {
      "version": "1.5.0"
    },
    "event": {
      "action": "Registry value set (rule: RegistryEvent)",
      "code": 13,
      "created": "2021-06-19T02:45:33.098Z",
      "kind": "event",
      "module": "sysmon",
      "provider": "Microsoft-Windows-Sysmon"
    },
    "host": {
      "name": "CLIENT"
    },
    "log": {
      "level": "information"
    },
    "message": "Registry value set:\nRuleName: T1060,RunKey\nEventType: SetValue\nUtcTime: 2021-06-19 02:41:27.390\nProcessGuid: {f7f24c5a-5956-60cd-2a00-000000000300}\nProcessId: 2060\nImage: C:\\Program Files\\Windows Defender\\MsMpEng.exe\nTargetObject: HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\WindowsDefender\nDetails: \"%%ProgramFiles%%\\Windows Defender\\MSASCuiL.exe\"",
    "pre_detection_id": "4f4f1bd3-f207-4ced-a70a-88391b36ee97",
    "process": {
      "entity_id": "{f7f24c5a-5956-60cd-2a00-000000000300}",
      "executable": "C:\\Program Files\\Windows Defender\\MsMpEng.exe",
      "name": "MsMpEng.exe",
      "pid": 2060
    },
    "registry": {
      "hive": "HKLM",
      "key": "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\WindowsDefender",
      "path": "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\WindowsDefender",
      "value": "WindowsDefender"
    },
    "rule": {
      "name": "T1060,RunKey"
    },
    "winlog": {
      "api": "wineventlog",
      "channel": "Microsoft-Windows-Sysmon/Operational",
      "computer_name": "CLIENT",
      "event_data": {
        "Details": "\"%%ProgramFiles%%\\Windows Defender\\MSASCuiL.exe\"",
        "EventType": "SetValue",
        "TargetObject": "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\WindowsDefender"
      },
      "event_id": 13,
      "opcode": "Info",
      "process": {
        "pid": 1320,
        "thread": {
          "id": 2848
        }
      },
      "provider_guid": "{5770385f-c22a-43e0-bf4c-06f5698ffbd9}",
      "provider_name": "Microsoft-Windows-Sysmon",
      "record_id": 491,
      "task": "Registry value set (rule: RegistryEvent)",
      "user": {
        "domain": "NT AUTHORITY",
        "identifier": "S-1-5-18",
        "name": "SYSTEM",
        "type": "User"
      },
      "version": 2
    }
  },
  "rules": [
    "Autorun Keys Modification"
  ]
}
[...]
```