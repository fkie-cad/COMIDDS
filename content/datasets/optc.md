---
title: OpTC
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Example Data](#example-data)

| <!-- -->                 | <!-- -->                                                                               |
|--------------------------|----------------------------------------------------------------------------------------|
| **Network Data Source**  | NetFlows                                                                               |
| **Network Data Labeled** | Yes                                                                                    |
| **Host Data Source**     | eCar events                                                                            |
| **Host Data Labeled**    | Yes                                                                                    |
|                          |                                                                                        |
| **Overall Setting**      | Enterprise IT                                                                          |
| **OS Types**             | Windows 10                                                                             |
| **Number of Machines**   | 1000 (only data for 500 included)                                                      |
| **Total Runtime**        | 6 days                                                                                 |
| **Year of Collection**   | 2019                                                                                   |
| **Attack Categories**    | Powershell Empire<br/>Malicious Upgrades                                               |
| **Benign Activity**      | Synthetic                                                                              |
|                          |                                                                                        |
| **Packed Size**          | n/a                                                                                    |
| **Unpacked Size**        | 1 TB                                                                                   |
| **Download Link**        | [GDrive](https://drive.google.com/drive/u/0/folders/1n3kkS3KR31KUegn42yk3-e6JkZvf0Caa) |

***

### Overview

The Operationally Transparent Cyper (OpTC) dataset was primarily created as a "byproduct" of determining the scalability
of DARPAs Transparent Computing (TC) program technologies.
Together with the organisations Boston Fusion, Five Directions and BAE, their testbed was scaled from two to 1000
hosts - this was then used for evaluation of components like endpoint telemetry and analysis engines.
During this evaluation, a red term performed an attack campaign mimicking the likes of an APT group.

### Environment

The testbed consists of 1000 hosts running Windows 10, though the dataset "only" contains data for 500 of them.

### Activity

Throughout the entire evaluation, benign activity/traffic was generated.
The first period consisted of only that benign activity, the second one added activity of a red team performing a
variety of attacks, the details of which can be found in the ground truth file linked below.

### Contained Data

From each of these host, events were collected, aggregated and transformed into the eCar format.
This format is an extension of [MITRE's CAR model](https://car.mitre.org/wiki/Data_Model), which originally only
contains an _object_, an _action_ and a _fields_ parameter, linking an object - e.g. FILE - to an action - e.g. CREATE,
with the fields parameter providing some limited additional information.
The extended form simply adds several more fields like PID or an actorID;
more information can be found using the links below.
In addition to this, the dataset contains events captured by Bro (now known as Zeek), which is a network security
monitoring platform.

eCar data can be found in the `eCar` directory, which is divided into three folders, with each folder's content then
being further divided by day and machine:

- `benign/` contains events from the first (benign) period.
- `evaluation/` contains events from the second period where both benign and malicious activity took place.
- `short/` contains events with missing information.

Bro (Zeek) data can be found in the `bro` directory and contains these events grouped by day and time.
Finally, the `ecar-bro` directory contains eCar events, but annotated with bro-IDs to link between eCar and bro
records - though it isn't entirely clear if those are the _same_ or _different_ eCar events.
If they are the same, it wouldn't really make sense to have duplicate data like this.

Unfortunately, there seems to be no labeling beyond the one implied by the folder structure, and the authors suggest to
use the provided ground truth file to label events manually.

### Papers

- [Analyzing the Usefulness of the DARPA OpTC Dataset in Cyber Threat Detection Research (2021)](https://doi.org/10.1145/3450569.3463573)

### Links

- [Homepage](https://github.com/FiveDirections/OpTC-data#operationally-transparent-cyber-optc-data-release)
- [OpTC Red Team Ground Truth](https://github.com/FiveDirections/OpTC-data/blob/master/OpTCRedTeamGroundTruth.pdf)
- [eCar Model Description](https://github.com/FiveDirections/OpTC-data/blob/master/ecar.md)

### Example Data

Snippet of eCar event example taken from `ecar/evaluation/23Sep19-red/AIA-201-225/*.json`.

```json
{
  "action": "START",
  "actorID": "4740cf20-06d5-4c6b-9c0d-a83b43480987",
  "hostname": "SysClient0220.systemia.com",
  "id": "53125c09-52bd-4716-89eb-326b331450e9",
  "object": "FLOW",
  "objectID": "4ac9bdec-8b6a-4582-b556-28cee4851ed3",
  "pid": 856,
  "ppid": 548,
  "principal": "NT AUTHORITY\\NETWORK SERVICE",
  "properties": {
    "acuity_level": "1",
    "dest_ip": "224.0.0.251",
    "dest_port": "5353",
    "direction": "inbound",
    "image_path": "\\Device\\HarddiskVolume1\\Windows\\system32\\svchost.exe",
    "l4protocol": "17",
    "src_ip": "10.20.2.172",
    "src_port": "5353"
  },
  "tid": -1,
  "timestamp": "2019-09-23T09:12:26.333-04:00"
}
{
  "action": "CREATE",
  "actorID": "2d56a9f8-9eb0-4b02-a48c-a1413dbaa59c",
  "hostname": "SysClient0209.systemia.com",
  "id": "72e84ab9-084a-4734-81c2-06674bc38068",
  "object": "THREAD",
  "objectID": "5d693438-5cfa-442e-a5c1-162699e4114c",
  "pid": 88,
  "ppid": 552,
  "principal": "NT AUTHORITY\\SYSTEM",
  "properties": {
    "acuity_level": "5",
    "image_path": "\\Device\\HarddiskVolume1\\Windows\\system32\\svchost.exe",
    "src_pid": "88",
    "src_tid": "4052",
    "stack_base": "ffffd10156e71000",
    "stack_limit": "ffffd10156e6b000",
    "start_address": "7ff89f304980",
    "subprocess_tag": "2a",
    "tgt_pid": "88",
    "tgt_tid": "304",
    "user_stack_base": "10cef300000",
    "user_stack_limit": "10cef2f8000"
  },
  "tid": 4052,
  "timestamp": "2019-09-23T09:42:51.804-04:00"
}
```

Bro (Zeek) events taken from `bro/2019-09-20/dns.11_00_00-12_00_00.log`.

```
[...]
1569063646.431642	CBGOhR1146Tjd6hkmb	88.232.210.2	55943	142.20.61.130	53	udp	15762	-	centosweb02.systemia.com	1	C_INTERNET	1	A	0	NOERROR	T	F	F	T	0	142.20.61.158	3600.000000	F
1569063647.841992	C3Z44Y2HbZS4cLRxK7	142.20.61.130	58989	192.33.4.12	53	udp	35012	-	piwik.dkd.de	1	C_INTERNET	1	A	3	NXDOMAIN	F	F	F	F	0	-	-	F
[...]
```

eCar-bro events taken from `ecar-bro/evaluation/23Sep19-red/AIA-201-225/ecarbro.json`.

```json
[
  ...
]
{
  "timestamp": "2019-09-23T14:55:18.164-04:00",
  "id": "8e8b8298-d173-4e01-a871-8e10cb2c0be2",
  "hostname": "SysClient0216.systemia.com",
  "objectID": "7536160e-4cc3-438d-8073-9a94cf85e8d5",
  "object": "FLOW",
  "action": "INFO",
  "actorID": "4ddb9762-2c0e-44e3-874c-4c5eebf5912a",
  "pid": 1648,
  "ppid": 5736,
  "tid": -1,
  "principal": "SYSTEMIACOM\\thaglund",
  "properties": {
    "acuity_level": "1",
    "bro_uid": "CWpSLE2BloALIy1DAb",
    "dest_ip": "139.67.157.5",
    "dest_port": "443",
    "direction": "outbound",
    "image_path": "\\\\?\\C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe",
    "l4protocol": "6",
    "src_ip": "142.20.56.217",
    "src_port": "63055"
  }
}
{
  "timestamp": "2019-09-23T14:55:18.166-04:00",
  "id": "6d21878f-9541-42d4-a82b-b0f6a4f19a86",
  "hostname": "SysClient0216.systemia.com",
  "objectID": "be2ecdb0-a4eb-49d9-ba00-cfc66df03e2f",
  "object": "FLOW",
  "action": "INFO",
  "actorID": "4ddb9762-2c0e-44e3-874c-4c5eebf5912a",
  "pid": 1648,
  "ppid": 5736,
  "tid": -1,
  "principal": "SYSTEMIACOM\\thaglund",
  "properties": {
    "acuity_level": "1",
    "bro_uid": "CTjNQd1FBaiEF4CZHf",
    "dest_ip": "139.67.157.5",
    "dest_port": "443",
    "direction": "outbound",
    "image_path": "\\\\?\\C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe",
    "l4protocol": "6",
    "src_ip": "142.20.56.217",
    "src_port": "63056"
  }
}

[
  ...
]
```