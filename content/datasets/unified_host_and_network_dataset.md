---
title: Unified Host and Network Dataset
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                              |
|--------------------------|-------------------------------------------------------|
| **Network Data Source**  | NetFlows                                              |
| **Network Data Labeled** | No                                                    |
| **Host Data Source**     | Windows events (auth & proc)                          |
| **Host Data Labeled**    | No                                                    |
|                          |                                                       |
| **Overall Setting**      | Enterprise IT                                         |
| **OS Types**             | Undisclosed Windows Versions<br/>Undisclosed other OS |
| **Number of Machines**   | n/a                                                   |
| **Total Runtime**        | 90 days                                               |
| **Year of Collection**   | 2017                                                  |
| **Attack Categories**    | None                                                  |
| **Benign Activity**      | Real users                                            |
|                          |                                                       |
| **Packed Size**          | n/a                                                   |
| **Unpacked Size**        | n/a                                                   |
| **Download Link**        | see below                                             |

***

### Overview

The Unified Host and Network Dataset contains data collected from the Los Alamos National Laboratory (LANL) operational
enterprise network over the course of roughly 90 days.
It contains no (known) attacks, and identifying values have been anonymized.

### Environment

As mentioned, the environment is the LANLs production network.
Details, other than "some machines run Windows", are not disclosed.

### Activity

No known malicious activity was performed during the collection period of 90 days.

### Contained Data

Host logs are a subset of all host event logs collected from all computers running Windows on the LANL's enterprise
network, collected with Windows Logging Service (WLS).
The collected events are related to process activity (only start/end) and authentication, a detailed list of all events
and associated attributes is available in the paper linked below.

Network data comes in the form of network flows and is collected from all devices connected to the network, not just
those running Windows.
Raw data consisted of NetFlow V9 records, but the data made available only contains a selection of the original
features, namely StartTime, EndTime, SrcIP, DstIP, Protocol, SrcPort, DstPort, Packets and Bytes.

As mentioned, the network dataset contains many non-Windows devices, making the two datasets not fully inclusive.
However, de-identified values do match across these datasets.

Network and host event data must be respectively downloaded using the following commands.

```bash
for i in $(seq -w 2 90); do wget -c https://csr.lanl.gov/data/unified-host-network-dataset-2017/1699547691/1KV676mDmMtzH0VsFMrq_aRXDWs=/netflow/netflow_day-$i.bz2; done
for i in $(seq -w 1 90); do wget -c https://csr.lanl.gov/data/unified-host-network-dataset-2017/1699547691/1KV676mDmMtzH0VsFMrq_aRXDWs=/wls/wls_day-$i.bz2; done
```

Note: Their service is currently unavailable, preventing downloads :(

### Papers

- [Unified Host and Network Dataset (2017)](https://doi.org/10.48550/arXiv.1708.07518)

### Links

- [Homepage](https://csr.lanl.gov/data/2017/)

### Related Entries
- Other LANL datasets:
    - [Comprehensive, Multi-Source Cybersecurity Events](comp_multi_source_cybersec_events.md)
    - [User-Computer Authentication Associations in Time](user_computer_associations.md)

### Data Examples

Example network event data

```
Time, Duration, SrcDevice, DstDevice, Protocol, SrcPort, DstPort, SrcPackets, DstPackets, SrcBytes, DstBytes
761,4434,Comp132598,Comp817788,6,Port12597,22,89159,85257,15495068,69768940
764,13161,Comp178973,Comp164069,17,137,137,325,0,30462,0
765,14369,Comp492856,Mail,6,Port30344,443,227,214,32300,9844
765,14431,Comp782574,Mail,6,Port28068,443,1637,3313,75302,1220077
765,17056,Comp378125,Mail,6,Port28068,443,3848,4096,177008,1441295
765,17087,Comp378125,Mail,6,Port41392,443,571,275,60842,12650
765,18105,Comp492856,Mail,6,Port30344,443,292,298,40698,13708
765,18633,Comp378125,Mail,6,Port41392,443,622,310,70370,20963
765,22042,Comp782574,Mail,6,Port28068,443,2142,4299,98532,1423831
[...]
```

Example host event data

```json
[...]
{
  "EventID": 4769,
  "UserName": "User624729",
  "ServiceName": "Comp883934$",
  "DomainName": "Domain002",
  "Status": "0x0",
  "Source": "Comp309534",
  "Computer": "ActiveDirectory",
  "Time": 2
}
{
  "EventID": 4776,
  "UserName": "Scanner",
  "DomainName": "Domain002",
  "Status": "0x0",
  "Computer": "ActiveDirectory",
  "AuthenticationPackage": "MICROSOFT_AUTHENTICATION_PACKAGE_V1_0",
  "Time": 2
}
{
  "EventID": 4672,
  "UserName": "ActiveDirectory$",
  "LogonID": "0x2e66398d",
  "DomainName": "Domain002",
  "Computer": "ActiveDirectory",
  "Time": 2
}
{
  "EventID": 4624,
  "UserName": "ActiveDirectory$",
  "LogonID": "0x2e66398d",
  "DomainName": "Domain002",
  "LogonTypeDescription": "Network",
  "Computer": "ActiveDirectory",
  "AuthenticationPackage": "Kerberos",
  "Time": 2,
  "LogonType": 3
}
[...]
```